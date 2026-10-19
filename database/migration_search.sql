-- ============================================
-- Full-text search for the Indian law library
-- Safe to run more than once.
-- ============================================

-- Keep tsv columns filled automatically on insert/update
CREATE OR REPLACE FUNCTION law_chunks_tsv_update() RETURNS trigger AS $$
BEGIN
    NEW.tsv := setweight(to_tsvector('english', coalesce(NEW.title, '')), 'A')
            || setweight(to_tsvector('english', coalesce(NEW.section, '') || ' ' || coalesce(NEW.article, '')), 'A')
            || setweight(to_tsvector('english', coalesce(NEW.content, '')), 'B');
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_law_chunks_tsv ON law_chunks;
CREATE TRIGGER trg_law_chunks_tsv
    BEFORE INSERT OR UPDATE OF title, section, article, content ON law_chunks
    FOR EACH ROW EXECUTE FUNCTION law_chunks_tsv_update();

CREATE OR REPLACE FUNCTION law_documents_tsv_update() RETURNS trigger AS $$
BEGIN
    NEW.tsv := setweight(to_tsvector('english', coalesce(NEW.title, '')), 'A')
            || setweight(to_tsvector('english', coalesce(NEW.summary, '')), 'B');
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_law_documents_tsv ON law_documents;
CREATE TRIGGER trg_law_documents_tsv
    BEFORE INSERT OR UPDATE OF title, summary ON law_documents
    FOR EACH ROW EXECUTE FUNCTION law_documents_tsv_update();

-- Backfill rows inserted before the triggers existed
UPDATE law_chunks SET content = content WHERE tsv IS NULL;
UPDATE law_documents SET title = title WHERE tsv IS NULL;

-- Ranked search used by src/api/main.py:search_laws().
-- Words are OR-ed so partial matches still rank; domains is TEXT[] in init.sql.
DROP FUNCTION IF EXISTS search_law(TEXT, TEXT[], INT);
CREATE OR REPLACE FUNCTION search_law(
    query TEXT,
    filter_domains TEXT[] DEFAULT NULL,
    match_count INT DEFAULT 10
)
RETURNS TABLE (
    chunk_id UUID,
    law_id UUID,
    law_title TEXT,
    law_number TEXT,
    article TEXT,
    chunk_title TEXT,
    content TEXT,
    domains TEXT[],
    rank REAL
) AS $$
    WITH q AS (
        SELECT websearch_to_tsquery('english', regexp_replace(trim(query), '\s+', ' or ', 'g')) AS tsq
    )
    SELECT lc.id, lc.law_id, ld.title, ld.law_number,
           coalesce(lc.article, lc.section), lc.title, lc.content,
           lc.domains::TEXT[], ts_rank(lc.tsv, q.tsq)
    FROM law_chunks lc
    JOIN law_documents ld ON ld.id = lc.law_id
    CROSS JOIN q
    WHERE lc.tsv @@ q.tsq
      AND (filter_domains IS NULL OR lc.domains::TEXT[] && filter_domains)
    ORDER BY ts_rank(lc.tsv, q.tsq) DESC
    LIMIT match_count;
$$ LANGUAGE sql STABLE;
