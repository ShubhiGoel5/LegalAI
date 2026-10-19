#!/usr/bin/env python3
"""
Load the Indian law library into Supabase (law_documents + law_chunks).

Sources (downloaded by scripts/download_indian_datasets.py):
- data/indian_constitution.json: Preamble and Articles 1-35 (Parts I-III)
- data/indian_penal_code.json:    Indian Penal Code, 1860

Applies database/migration_search.sql first, then replaces any rows this script
loaded before, so it is safe to run again.

Usage:
    python scripts/download_indian_datasets.py
    python scripts/load_indian_law.py
"""
import json
import os
import sys
from pathlib import Path

import psycopg2
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
SOURCE_SITE = "seed:load_indian_law"

load_dotenv(ROOT / ".env")

DB_CONFIG = {
    "host": os.getenv("SUPABASE_DB_HOST"),
    "port": int(os.getenv("SUPABASE_DB_PORT", "5432")),
    "dbname": os.getenv("DB_NAME", "postgres"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("SUPABASE_DB_PASSWORD"),
    "sslmode": os.getenv("DB_SSL_MODE", "require"),
}


def constitution_chunks(data):
    """Turn COI.json into one chunk per article."""
    articles, parts = data[0], data[1]
    part_of = {}
    for part in parts:
        for art_no in part.get("Articles", []):
            part_of[art_no] = f"Part {part['PartNo']}: {part['Name'].title()}"

    chunks = []
    for art in articles:
        if art.get("Status") == "Omitted":
            continue
        art_no = art["ArtNo"]
        is_preamble = art_no == "0"
        lines = []
        if art.get("ArtDesc"):
            lines.append(art["ArtDesc"])
        for clause in art.get("Clauses") or []:
            lines.append(f"({clause['ClauseNo']}) {clause['ClauseDesc']}")
            for sub in clause.get("SubClauses") or []:
                if sub.get("Status") == "Omitted":
                    continue
                lines.append(f"    ({sub['SubClauseNo']}) {sub['SubClauseDesc']}")
            if clause.get("FollowUp"):
                lines.append(clause["FollowUp"])
        for exp in art.get("Explanations") or []:
            lines.append(f"Explanation {exp.get('ExplanationNo', '')}: {exp.get('Explanation', '')}".strip())
        heading = "Preamble" if is_preamble else f"Article {art_no}"
        chunks.append({
            "chapter": "Preamble" if is_preamble else part_of.get(art_no),
            "section": None,
            "article": heading,
            "title": "Preamble" if is_preamble else art["Name"].rstrip("."),
            "parent_context": art.get("SubHeading"),
            "content": f"{heading}. {art['Name']}\n" + "\n".join(lines) if not is_preamble else "\n".join(lines),
        })
    return chunks


def ipc_chunks(data):
    """Turn ipc.json into one chunk per section."""
    chunks = []
    for sec in data:
        desc = (sec.get("section_desc") or "").strip()
        if not desc:
            continue
        number = f"Section {sec['Section']}"
        chunks.append({
            "chapter": f"Chapter {sec.get('chapter')}: {str(sec.get('chapter_title', '')).capitalize()}",
            "section": number,
            "article": None,
            "title": sec.get("section_title", "").strip(),
            "parent_context": None,
            "content": f"{number}. {sec.get('section_title', '').strip()}\n{desc}",
        })
    return chunks


LAWS = [
    {
        "file": "indian_constitution.json",
        "parse": constitution_chunks,
        "title": "Constitution of India",
        "law_number": "Constitution of India, 1950",
        "law_type": "constitution",
        "issuer": "Constituent Assembly of India",
        "effective_date": "1950-01-26",
        "domains": ["constitutional"],
        "source_url": "https://legislative.gov.in/constitution-of-india/",
        "summary": "Preamble and Parts I-III (Union and its territory, Citizenship, Fundamental Rights), Articles 1-35.",
    },
    {
        "file": "indian_penal_code.json",
        "parse": ipc_chunks,
        "title": "Indian Penal Code, 1860",
        "law_number": "Act No. 45 of 1860",
        "law_type": "act",
        "issuer": "Parliament of India",
        "effective_date": "1862-01-01",
        "domains": ["criminal"],
        "source_url": "https://www.indiacode.nic.in/",
        "summary": "Indian Penal Code, 1860. Replaced by the Bharatiya Nyaya Sanhita, 2023 for offences committed on or after 1 July 2024.",
    },
]


def main():
    missing = [k for k in ("SUPABASE_DB_HOST", "SUPABASE_DB_PASSWORD") if not os.getenv(k)]
    if missing:
        sys.exit(f"Missing {', '.join(missing)} in .env")

    conn = psycopg2.connect(**DB_CONFIG)
    try:
        with conn, conn.cursor() as cur:
            cur.execute((ROOT / "database" / "migration_search.sql").read_text(encoding="utf-8"))
        print("Search function and triggers ready")

        for law in LAWS:
            path = DATA_DIR / law["file"]
            if not path.exists():
                sys.exit(f"{path} not found; run scripts/download_indian_datasets.py first")
            chunks = law["parse"](json.loads(path.read_text(encoding="utf-8")))

            # One transaction per law: replace previous copy, insert document + chunks
            with conn, conn.cursor() as cur:
                cur.execute(
                    "DELETE FROM law_chunks WHERE law_id IN "
                    "(SELECT id FROM law_documents WHERE law_number = %s AND source_site = %s)",
                    (law["law_number"], SOURCE_SITE),
                )
                cur.execute(
                    "DELETE FROM law_documents WHERE law_number = %s AND source_site = %s",
                    (law["law_number"], SOURCE_SITE),
                )
                full_text = "\n\n".join(c["content"] for c in chunks)
                cur.execute(
                    """
                    INSERT INTO law_documents (title, law_number, law_type, issuer, effective_date,
                        status, domains, full_text, summary, source_url, source_site,
                        article_count, word_count)
                    VALUES (%s, %s, %s, %s, %s, 'active', %s, %s, %s, %s, %s, %s, %s)
                    RETURNING id
                    """,
                    (law["title"], law["law_number"], law["law_type"], law["issuer"],
                     law["effective_date"], law["domains"], full_text, law["summary"],
                     law["source_url"], SOURCE_SITE, len(chunks), len(full_text.split())),
                )
                law_id = cur.fetchone()[0]
                cur.executemany(
                    """
                    INSERT INTO law_chunks (law_id, chapter, section, article, title, content,
                        parent_context, domains)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    """,
                    [(law_id, c["chapter"], c["section"], c["article"], c["title"],
                      c["content"], c["parent_context"], law["domains"]) for c in chunks],
                )
            print(f"Loaded {law['title']}: {len(chunks)} chunks")

        with conn.cursor() as cur:
            cur.execute("SELECT (SELECT count(*) FROM law_documents), (SELECT count(*) FROM law_chunks)")
            docs, total = cur.fetchone()
        print(f"Library now has {docs} documents and {total} chunks")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
