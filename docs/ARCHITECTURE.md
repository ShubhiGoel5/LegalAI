# Legal AI Agent — System Architecture

## Overview

A multi-tenant Legal AI platform for Indian companies. Companies interact via Cloud API to get AI-powered legal assistance — contract review, legal Q&A, compliance checking, and document drafting.

**Business Model:** SaaS API — companies authenticate with API keys, billed per usage tier.

---

## 1. System Architecture

```
                    ┌─────────────────────────┐
                    │      CLIENT APPS         │
                    │                          │
                    │  Web Dashboard (Next.js) │
                    │  Chat Widget (Embed JS)  │
                    │  REST API (Direct)       │
                    │  Mobile SDK (Future)     │
                    └───────────┬──────────────┘
                                │
                                │ HTTPS / WSS
                                ▼
┌───────────────────────────────────────────────────────────┐
│                    API GATEWAY LAYER                       │
│                                                           │
│  ┌─────────────┐  ┌──────────┐  ┌──────────┐  ┌───────┐  │
│  │ Supabase    │  │ Rate     │  │ API Key  │  │Request│  │
│  │ Auth        │  │ Limiter  │  │ Validator│  │Logger │  │
│  │ (GoTrue)    │  │ (Redis)  │  │          │  │       │  │
│  └─────────────┘  └──────────┘  └──────────┘  └───────┘  │
│                                                           │
│  Supabase Edge Functions (auth, routing, billing meter)   │
└───────────────────────────┬───────────────────────────────┘
                            │
                            ▼
┌───────────────────────────────────────────────────────────┐
│                   AGENT ORCHESTRATOR                       │
│                   (FastAPI + LangGraph)                     │
│                                                           │
│  ┌─────────────────────────────────────────────────────┐  │
│  │                  Agent Router                        │  │
│  │  Analyzes intent → routes to specialized agent       │  │
│  └──────────┬──────────┬──────────┬──────────┬─────────┘  │
│             │          │          │          │             │
│     ┌───────▼──┐ ┌─────▼────┐ ┌──▼───────┐ ┌▼─────────┐  │
│     │ Legal    │ │ Contract │ │Compliance│ │ Document │  │
│     │ Q&A      │ │ Review   │ │ Audit    │ │ Drafter  │  │
│     │ Agent    │ │ Agent    │ │ Agent    │ │ Agent    │  │
│     └───────┬──┘ └────┬─────┘ └──┬───────┘ └┬─────────┘  │
│             │         │          │          │             │
│     ┌───────▼─────────▼──────────▼──────────▼─────────┐  │
│     │              Shared Services                     │  │
│     │                                                  │  │
│     │  ┌──────────┐ ┌──────────┐ ┌──────────────────┐  │  │
│     │  │ Citation │ │ Halluc.  │ │ Context Manager  │  │  │
│     │  │ Verifier │ │ Guard    │ │ (Memory/History) │  │  │
│     │  └──────────┘ └──────────┘ └──────────────────┘  │  │
│     └──────────────────────────────────────────────────┘  │
└───────────────────────────┬───────────────────────────────┘
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
┌──────────────────┐ ┌──────────┐ ┌──────────────────┐
│   RAG ENGINE     │ │   LLM    │ │   TOOL LAYER     │
│                  │ │  ROUTER  │ │                   │
│ Query Rewrite    │ │          │ │ OCR (Surya)       │
│ Hybrid Search    │ │ Claude   │ │ PDF Parser        │
│ Reranker         │ │ Sonnet   │ │ Doc Generator     │
│ Context Builder  │ │ (primary)│ │ Web Search        │
│                  │ │          │ │ Calculator        │
└────────┬─────────┘ └────┬─────┘ └──────────────────┘
         │                │
         └────────┬───────┘
                  ▼
┌───────────────────────────────────────────────────────────┐
│                     SUPABASE LAYER                         │
│                                                           │
│  ┌─────────────────────────────────────────────────────┐  │
│  │                  PostgreSQL                          │  │
│  │                                                     │  │
│  │  ┌───────────┐  ┌───────────┐  ┌─────────────────┐  │  │
│  │  │ Tenant    │  │ Law DB    │  │ pgvector        │  │  │
│  │  │ Tables    │  │ (shared)  │  │ (embeddings)    │  │  │
│  │  │ (RLS)     │  │           │  │                 │  │  │
│  │  └───────────┘  └───────────┘  └─────────────────┘  │  │
│  └─────────────────────────────────────────────────────┘  │
│                                                           │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│  │  Auth    │  │ Storage  │  │ Realtime │  │  Edge    │  │
│  │ (GoTrue) │  │ (S3)     │  │ (WSS)    │  │Functions │  │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘  │
└───────────────────────────────────────────────────────────┘
```

---

## 2. Data Architecture

### 2.1 Multi-Tenant Isolation

```
                    ┌──────────────────┐
                    │   Shared Layer    │
                    │                  │
                    │  law_documents   │  ← All Indian laws
                    │  law_chunks      │  ← Embedded chunks
                    │  law_relations   │  ← Law cross-references
                    └──────────────────┘
                             │
                    READ-ONLY access via RLS
                             │
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  Tenant A    │    │  Tenant B    │    │  Tenant C    │
│              │    │              │    │              │
│ company_id=A │    │ company_id=B │    │ company_id=C │
│              │    │              │    │              │
│ - documents  │    │ - documents  │    │ - documents  │
│ - chunks     │    │ - chunks     │    │ - chunks     │
│ - sessions   │    │ - sessions   │    │ - sessions   │
│ - messages   │    │ - messages   │    │ - messages   │
│ - usage_logs │    │ - usage_logs │    │ - usage_logs │
└──────────────┘    └──────────────┘    └──────────────┘

RLS Policy: WHERE company_id = auth.jwt()->>'company_id'
```

### 2.2 Law Data Pipeline

```
┌────────────────┐     ┌──────────────┐     ┌──────────────┐
│  Source Sites  │     │  Crawler     │     │  Parser      │
│                │     │              │     │              │
│ India Code     │────▶│ crawler.py   │────▶│ law_parser   │
│ Legislative    │     │ (scrape)     │     │ (extract     │
│ Indian Kanoon  │     │              │     │  sections)   │
└────────────────┘     └──────────────┘     └──────┬───────┘
                                                   │
                                                   ▼
┌────────────────┐     ┌──────────────┐     ┌──────────────┐
│  Supabase      │     │  Embedder    │     │  Chunker     │
│  pgvector      │◀────│              │◀────│              │
│                │     │ BGE-M3 or    │     │ Split by     │
│ law_chunks +   │     │ OpenAI       │     │ article/     │
│ embedding      │     │              │     │ clause       │
└────────────────┘     └──────────────┘     └──────────────┘
```

### 2.3 Entity Relationship Diagram

```
companies ─────┬──── users
    │          │
    │          └──── api_keys
    │
    ├──── chat_sessions ──── messages
    │
    ├──── documents ──── company_chunks (pgvector)
    │
    └──── usage_logs

law_documents ──── law_chunks (pgvector)
       │
       └──── law_relations (cross-references)
```

---

## 3. Agent Architecture

### 3.1 Agent Router (Intent Classification)

```
User Input
    │
    ▼
┌───────────────────────────────┐
│  Intent Classifier (LLM)      │
│                               │
│  Classify into:               │
│  ├── LEGAL_QA                 │ → "How long is maternity leave?"
│  ├── CONTRACT_REVIEW          │ → "Review this contract"
│  ├── COMPLIANCE_CHECK         │ → "Is my company compliant?"
│  ├── DOCUMENT_DRAFT           │ → "Draft an employment contract"
│  ├── CASE_RESEARCH            │ → "Find similar precedents"
│  └── GENERAL_CHAT             │ → "Hello"
│                               │
│  Also extracts:               │
│  - Legal domain (labor, tax)  │
│  - Entities (company, person) │
│  - Urgency level              │
└───────────────┬───────────────┘
                │
                ▼
        Route to specialized agent
```

### 3.2 Legal Q&A Agent (Detail)

```
┌─────────────────────────────────────────────────────┐
│                LEGAL Q&A AGENT                       │
│                                                     │
│  Step 1: ANALYZE                                    │
│  ┌───────────────────────────────────┐              │
│  │ - Identify legal domain           │              │
│  │ - Extract key legal concepts      │              │
│  │ - Determine relevant laws         │              │
│  │ - Generate search queries (3-5)   │              │
│  └───────────────────┬───────────────┘              │
│                      ▼                              │
│  Step 2: RETRIEVE                                   │
│  ┌───────────────────────────────────┐              │
│  │ Hybrid Search:                    │              │
│  │ ├── Semantic (pgvector cosine)    │              │
│  │ ├── Keyword (ts_vector BM25)      │              │
│  │ └── Filter (domain, status)       │              │
│  │                                   │              │
│  │ → Retrieve top 20 chunks          │              │
│  │ → Rerank to top 5                 │              │
│  └───────────────────┬───────────────┘              │
│                      ▼                              │
│  Step 3: REASON                                     │
│  ┌───────────────────────────────────┐              │
│  │ LLM with retrieved context:       │              │
│  │ - Answer the legal question       │              │
│  │ - Cite specific articles          │              │
│  │ - Note any exceptions/conditions  │              │
│  │ - Flag if answer is uncertain     │              │
│  └───────────────────┬───────────────┘              │
│                      ▼                              │
│  Step 4: VERIFY                                     │
│  ┌───────────────────────────────────┐              │
│  │ Citation Checker:                 │              │
│  │ - Verify each citation exists     │              │
│  │ - Confirm quote matches source    │              │
│  │ - Check law is still active       │              │
│  │ - Flag expired/amended laws       │              │
│  └───────────────────┬───────────────┘              │
│                      ▼                              │
│  Step 5: FORMAT                                     │
│  ┌───────────────────────────────────┐              │
│  │ Response Builder:                 │              │
│  │ - Clear plain-English answer      │              │
│  │ - Structured citations            │              │
│  │ - Confidence level                │              │
│  │ - Related topics suggestion       │              │
│  │ - Disclaimer                      │              │
│  └───────────────────────────────────┘              │
└─────────────────────────────────────────────────────┘
```

### 3.3 Contract Review Agent (Detail)

```
┌─────────────────────────────────────────────────────┐
│              CONTRACT REVIEW AGENT                   │
│                                                     │
│  Step 1: INGEST                                     │
│  ┌───────────────────────────────────┐              │
│  │ Upload → Supabase Storage         │              │
│  │ PDF/DOCX/Image → OCR if needed    │              │
│  │ → Extract full text               │              │
│  └───────────────────┬───────────────┘              │
│                      ▼                              │
│  Step 2: CLASSIFY                                   │
│  ┌───────────────────────────────────┐              │
│  │ Contract Type Detection:          │              │
│  │ ├── Employment Contract           │              │
│  │ ├── Commercial Contract           │              │
│  │ ├── Lease / Sale Agreement        │              │
│  │ ├── Service Contract              │              │
│  │ └── Partnership / JV Agreement    │              │
│  │                                   │              │
│  │ → Load relevant law checklist     │              │
│  └───────────────────┬───────────────┘              │
│                      ▼                              │
│  Step 3: EXTRACT                                    │
│  ┌───────────────────────────────────┐              │
│  │ Key Clause Extraction:            │              │
│  │ - Parties (Party A, Party B)      │              │
│  │ - Term & Duration                 │              │
│  │ - Payment terms                   │              │
│  │ - Obligations & Rights            │              │
│  │ - Termination conditions          │              │
│  │ - Dispute resolution              │              │
│  │ - Penalties & Liabilities         │              │
│  │ - Confidentiality                 │              │
│  └───────────────────┬───────────────┘              │
│                      ▼                              │
│  Step 4: ANALYZE                                    │
│  ┌───────────────────────────────────┐              │
│  │ Risk Assessment:                  │              │
│  │                                   │              │
│  │ For each clause:                  │              │
│  │ ├── Compare with Indian law       │              │
│  │ ├── Check for missing clauses     │              │
│  │ ├── Identify unfair terms         │              │
│  │ ├── Flag legal violations         │              │
│  │ └── Score risk (LOW/MED/HIGH)     │              │
│  │                                   │              │
│  │ Missing Clause Check:             │              │
│  │ ├── Required by law but missing   │              │
│  │ ├── Best practice but missing     │              │
│  │ └── Recommended additions         │              │
│  └───────────────────┬───────────────┘              │
│                      ▼                              │
│  Step 5: REPORT                                     │
│  ┌───────────────────────────────────┐              │
│  │ Generate Review Report:           │              │
│  │                                   │              │
│  │ ┌─ Summary ──────────────────┐    │              │
│  │ │ Overall Risk: MEDIUM       │    │              │
│  │ │ Issues Found: 5            │    │              │
│  │ │ Critical: 1, Warning: 3    │    │              │
│  │ └────────────────────────────┘    │              │
│  │                                   │              │
│  │ ┌─ Issue Detail ─────────────┐    │              │
│  │ │ 🔴 Clause 7: Post-exit     │    │              │
│  │ │    non-compete is void     │    │              │
│  │ │    (s.27 Contract Act)     │    │              │
│  │ │    → Suggest: replace with │    │              │
│  │ │    confidentiality clause  │    │              │
│  │ └────────────────────────────┘    │              │
│  └───────────────────────────────────┘              │
└─────────────────────────────────────────────────────┘
```

---

## 4. RAG Engine (Deep Dive)

### 4.1 Embedding Strategy

```
Law Document
    │
    ▼
┌──────────────────────────────┐
│  Chunking Strategy            │
│                              │
│  Level 1: Per Article         │  "Section 5. Right to payment of maternity benefit..."
│  Level 2: Per Clause          │  "(1) Subject to the provisions of this Act..."
│  Level 3: Per Point           │  "(a) ..." (individual clause / proviso)
│                              │
│  Each chunk includes:         │
│  - Content (text)            │
│  - Parent article context    │
│  - Law metadata              │
│  - Cross-references          │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  Embedding Models             │
│                              │
│  Primary: BGE-M3              │  Self-hosted, free
│  - Dense embedding (1024d)   │  Semantic similarity
│  - Sparse embedding          │  Keyword matching
│  - ColBERT embedding         │  Late interaction
│                              │
│  Backup: OpenAI ada-002      │  If BGE insufficient
│  - 1536 dimensions           │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  Storage: pgvector            │
│                              │
│  law_chunks table:            │
│  - id, law_id, article       │
│  - content (full text)       │
│  - embedding vector(1024)    │
│  - sparse_vector (tsvector)  │
│  - metadata (jsonb)          │
│                              │
│  Indexes:                    │
│  - HNSW for dense search     │
│  - GIN for sparse/keyword    │
│  - B-tree for metadata       │
└──────────────────────────────┘
```

### 4.2 Hybrid Search Pipeline

```sql
-- Dense search (semantic)
WITH semantic AS (
  SELECT id, content, metadata,
         1 - (embedding <=> query_embedding) AS semantic_score
  FROM law_chunks
  WHERE category && ARRAY['labour']  -- metadata filter
  ORDER BY embedding <=> query_embedding
  LIMIT 20
),

-- Sparse search (keyword/BM25)
keyword AS (
  SELECT id, content, metadata,
         ts_rank_cd(search_vector, plainto_tsquery('english', :query)) AS keyword_score
  FROM law_chunks
  WHERE search_vector @@ plainto_tsquery('english', :query)
  ORDER BY keyword_score DESC
  LIMIT 20
),

-- Reciprocal Rank Fusion
combined AS (
  SELECT id, content, metadata,
         COALESCE(s.semantic_score, 0) * 0.7 +
         COALESCE(k.keyword_score, 0) * 0.3 AS combined_score
  FROM semantic s
  FULL OUTER JOIN keyword k USING (id, content, metadata)
  ORDER BY combined_score DESC
  LIMIT 10
)
SELECT * FROM combined;
```

### 4.3 Context Window Management

```
┌─────────────────────────────────────┐
│  Context Budget: 100K tokens         │
│                                     │
│  ┌─ System Prompt ──────── 2K ──┐   │
│  │ Legal AI personality & rules  │   │
│  └──────────────────────────────┘   │
│                                     │
│  ┌─ Conversation History ── 5K ──┐  │
│  │ Last 5-10 messages            │   │
│  └──────────────────────────────┘   │
│                                     │
│  ┌─ Retrieved Law Chunks ── 15K ─┐  │
│  │ Top 5-8 relevant chunks       │   │
│  │ With full article context     │   │
│  └──────────────────────────────┘   │
│                                     │
│  ┌─ Company Context ──── 5K ────┐   │
│  │ Company docs if relevant      │   │
│  └──────────────────────────────┘   │
│                                     │
│  ┌─ User Query ──────── 1K ─────┐   │
│  │ Current question              │   │
│  └──────────────────────────────┘   │
│                                     │
│  Reserved for response: ~70K        │
└─────────────────────────────────────┘
```

---

## 5. API Design

### 5.1 REST Endpoints

```
Authentication:
  POST   /v1/auth/register          # Company registration
  POST   /v1/auth/login              # User login
  POST   /v1/auth/api-keys           # Generate API key
  DELETE /v1/auth/api-keys/:id       # Revoke API key

Legal Q&A:
  POST   /v1/legal/ask               # Ask a legal question
  POST   /v1/legal/search            # Search law database
  GET    /v1/legal/laws/:id          # Get specific law document
  GET    /v1/legal/laws              # List/filter laws

Contract Review:
  POST   /v1/contracts/review        # Upload & review contract
  GET    /v1/contracts/:id/status    # Check review progress
  GET    /v1/contracts/:id/report   # Get review report

Compliance:
  POST   /v1/compliance/check        # Run compliance audit
  GET    /v1/compliance/checklists   # Get compliance checklists

Documents:
  POST   /v1/documents/draft         # Generate legal document
  GET    /v1/documents/templates     # List templates

Chat (Realtime):
  WS     /v1/chat                    # WebSocket chat session
  POST   /v1/chat/sessions           # Create chat session
  GET    /v1/chat/sessions/:id      # Get session history

Usage & Billing:
  GET    /v1/usage                   # Current period usage
  GET    /v1/usage/history           # Usage history
  GET    /v1/billing/invoices        # Invoices
```

### 5.2 Request/Response Examples

```json
// POST /v1/legal/ask
{
  "question": "How many weeks of paid maternity leave is an employee entitled to?",
  "context": {
    "company_type": "manufacturing",
    "employee_count": 500
  },
  "options": {
    "include_citations": true,
    "include_related": true,
    "language": "en"
  }
}

// Response
{
  "answer": "Under the Maternity Benefit Act, 1961 (as amended in 2017), a woman employee is entitled to up to 26 weeks of paid maternity leave, of which not more than 8 weeks may precede the expected date of delivery...",
  "confidence": 0.95,
  "citations": [
    {
      "law": "Maternity Benefit Act, 1961",
      "number": "Act No. 53 of 1961",
      "article": "Section 5",
      "clause": "Sub-section (3)",
      "text": "The maximum period for which any woman shall be entitled to maternity benefit shall be twenty-six weeks of which not more than eight weeks shall precede the date of her expected delivery...",
      "effective_date": "2017-04-01",
      "status": "active"
    }
  ],
  "related_topics": [
    "Eligibility: 80 days of work in the preceding 12 months",
    "Maternity benefit under the ESI Act, 1948",
    "Protection against dismissal during maternity leave"
  ],
  "disclaimer": "This response is for general information only and does not constitute legal advice. Please consult a qualified advocate for your specific situation.",
  "usage": {
    "tokens_used": 1847,
    "cost_usd": 0.0037
  }
}
```

```json
// POST /v1/contracts/review
// Content-Type: multipart/form-data
{
  "file": "<binary>",
  "contract_type": "labor",  // auto-detect if omitted
  "review_depth": "comprehensive",  // quick | standard | comprehensive
  "focus_areas": ["termination", "compensation", "compliance"]
}

// Response (async — returns job ID)
{
  "job_id": "rev_abc123",
  "status": "processing",
  "estimated_time": 30,  // seconds
  "webhook_url": "optional callback"
}

// GET /v1/contracts/rev_abc123/report
{
  "overall_risk": "MEDIUM",
  "score": 72,  // out of 100
  "summary": "The contract has 2 clauses that conflict with the law and 3 clauses that are unfavourable to the employee.",
  "issues": [
    {
      "severity": "CRITICAL",
      "clause": "Clause 7 - Non-compete",
      "issue": "Restrains the employee from joining a competitor for 24 months after leaving employment",
      "law_reference": "Section 27, Indian Contract Act, 1872",
      "recommendation": "Remove the post-employment restraint; rely on confidentiality and non-solicitation obligations instead"
    },
    {
      "severity": "WARNING",
      "clause": "Clause 9 - Termination",
      "issue": "No notice period specified for termination by either party",
      "law_reference": "Industrial Relations Code, 2020 (retrenchment conditions); applicable State Shops and Establishments Act",
      "recommendation": "Add a mutual notice period (e.g. 30 days) or pay in lieu of notice"
    }
  ],
  "missing_clauses": [
    "Provident Fund (EPF) and ESI contributions",
    "Leave entitlements (earned, sick and casual leave)",
    "Confidentiality and data protection clause"
  ],
  "compliance_status": {
    "labor_code": "PARTIAL",
    "insurance": "MISSING",
    "safety": "OK"
  }
}
```

---

## 6. Security Architecture

### 6.1 Data Protection

```
┌─────────────────────────────────────────┐
│           Security Layers                │
│                                         │
│  Layer 1: Transport                     │
│  └── TLS 1.3 (all connections)          │
│                                         │
│  Layer 2: Authentication                │
│  └── Supabase Auth (JWT + API keys)     │
│  └── API key hashed with bcrypt         │
│  └── JWT expiry: 1 hour                 │
│                                         │
│  Layer 3: Authorization                 │
│  └── RLS policies on every table        │
│  └── Role-based (admin/member/viewer)   │
│  └── Resource-level permissions         │
│                                         │
│  Layer 4: Data Isolation                │
│  └── company_id on every row            │
│  └── RLS enforced at DB level           │
│  └── Storage buckets per company        │
│                                         │
│  Layer 5: Encryption                    │
│  └── At-rest: Supabase managed          │
│  └── Sensitive fields: pgcrypto         │
│  └── File storage: encrypted buckets    │
│                                         │
│  Layer 6: Audit                         │
│  └── Every API call logged              │
│  └── Every document access tracked      │
│  └── Retention: 90 days                 │
└─────────────────────────────────────────┘
```

### 6.2 LLM Safety

```
┌─────────────────────────────────────────┐
│         LLM Safety Guards                │
│                                         │
│  ① Input Sanitization                   │
│  └── Strip injection attempts           │
│  └── Validate document content          │
│  └── Block prompt injection             │
│                                         │
│  ② Output Validation                    │
│  └── Citation verification              │
│  └── Hallucination detection            │
│  └── Legal accuracy check               │
│  └── Confidence scoring                 │
│                                         │
│  ③ Guardrails                           │
│  └── Never give advice on criminal law  │
│  └── Always include disclaimer          │
│  └── Flag low-confidence answers        │
│  └── Refuse to impersonate lawyer       │
│                                         │
│  ④ Monitoring                           │
│  └── Log all LLM interactions           │
│  └── Alert on unusual patterns          │
│  └── Track accuracy metrics             │
└─────────────────────────────────────────┘
```

---

## 7. Deployment Architecture

### Phase 1: MVP (0-100 users)

```
┌──────────────────────────────────────┐
│          Supabase Cloud               │
│          (Free → Pro $25/mo)          │
│                                      │
│  Postgres + pgvector + Auth          │
│  + Storage + Realtime                │
└──────────────────┬───────────────────┘
                   │
┌──────────────────┴───────────────────┐
│     Single VPS (Hetzner CX31)        │
│     4 vCPU, 16GB RAM, $15/mo         │
│                                      │
│  Docker Compose:                     │
│  ├── fastapi-app (Agent server)      │
│  ├── redis (Queue + Cache)           │
│  ├── celery-worker (Async tasks)     │
│  └── caddy (Reverse proxy + SSL)     │
└──────────────────────────────────────┘
```

### Phase 2: Growth (100-1000 users)

```
┌──────────────────────────────────────┐
│          Supabase Pro ($25/mo)        │
│          + Dedicated DB ($100/mo)     │
└──────────────────┬───────────────────┘
                   │
┌──────────────────┴───────────────────┐
│     Kubernetes (2-3 nodes)            │
│     or Docker Swarm                   │
│                                      │
│  ├── api-server (2-3 replicas)       │
│  ├── celery-worker (2-4 replicas)    │
│  ├── redis-cluster                   │
│  ├── embedding-server (BGE-M3)       │
│  └── monitoring (Grafana + Loki)     │
└──────────────────────────────────────┘
```

### Phase 3: Scale (1000+ users)

```
┌──────────────────────────────────────┐
│     Supabase Enterprise               │
│     or Self-hosted Supabase           │
│     + Read replicas                   │
└──────────────────┬───────────────────┘
                   │
┌──────────────────┴───────────────────┐
│     Multi-region deployment           │
│     CDN + Load Balancer              │
│     Auto-scaling worker pools        │
│     Dedicated embedding GPU server   │
└──────────────────────────────────────┘
```

---

## 8. Indian Law Data Structure

### 8.1 Law Hierarchy

```
Constitution of India
    │
    ├── Acts of Parliament (Central) / State Acts
    │   ├── Code on Wages, 2019
    │   ├── Industrial Relations Code, 2020
    │   ├── Code on Social Security, 2020
    │   ├── Occupational Safety, Health and Working Conditions Code, 2020
    │   ├── Companies Act, 2013
    │   ├── Indian Contract Act, 1872
    │   ├── Maternity Benefit Act, 1961
    │   ├── Bharatiya Nyaya Sanhita, 2023 (reference only)
    │   └── State Shops and Establishments Acts
    │
    ├── Rules & Regulations — Central / State Governments, regulators
    │   ├── Rules framed under the Labour Codes (Central and State)
    │   ├── Companies (Incorporation) Rules, 2014
    │   └── SEBI (Listing Obligations and Disclosure Requirements) Regulations, 2015
    │
    ├── Notifications / Orders / Circulars — Ministries, RBI, SEBI, MCA
    │   ├── MCA General Circulars
    │   ├── RBI Master Directions / Circulars
    │   └── SEBI Circulars
    │
    └── Gazette of India (official publication — egazette.gov.in)
        ├── Extraordinary notifications
        ├── Ordinary notifications
        └── Office memoranda (reference only)
```

**Sources:** India Code (indiacode.nic.in), Legislative Department (legislative.gov.in), eGazette (egazette.gov.in), Indian Kanoon (indiankanoon.org); Supreme Court and High Court judgments as a future source.

### 8.2 Priority Crawl List (MVP)

```
Phase 1 — Labour Law (HR / labour use case):
  ├── Code on Wages, 2019
  ├── Industrial Relations Code, 2020
  ├── Code on Social Security, 2020
  ├── Occupational Safety, Health and Working Conditions Code, 2020
  ├── Maternity Benefit Act, 1961
  ├── Sexual Harassment of Women at Workplace (Prevention,
  │   Prohibition and Redressal) Act, 2013 (POSH)
  ├── Payment of Gratuity Act, 1972
  ├── Employees' Provident Funds and Miscellaneous Provisions Act, 1952
  ├── Employees' State Insurance Act, 1948
  └── Central / State Rules under the Labour Codes

Phase 2 — Business Law:
  ├── Companies Act, 2013
  ├── Limited Liability Partnership Act, 2008
  ├── Foreign Exchange Management Act, 1999
  └── Competition Act, 2002

Phase 3 — Contract & Civil:
  ├── Indian Contract Act, 1872
  ├── Transfer of Property Act, 1882
  ├── Real Estate (Regulation and Development) Act, 2016
  └── Copyright Act, 1957

Phase 4 — Tax & Finance:
  ├── Income-tax Act, 1961 / Income-tax Act, 2025
  ├── Central Goods and Services Tax Act, 2017
  ├── Integrated Goods and Services Tax Act, 2017
  └── Companies (Indian Accounting Standards) Rules, 2015
```

---

## 9. Monitoring & Observability

```
┌─────────────────────────────────────────┐
│           Monitoring Stack               │
│                                         │
│  Metrics: Prometheus + Grafana          │
│  ├── API latency (p50, p95, p99)        │
│  ├── LLM response time                  │
│  ├── RAG retrieval quality              │
│  ├── Error rates                        │
│  └── Usage per tenant                   │
│                                         │
│  Logs: Loki + Grafana                   │
│  ├── All API requests                   │
│  ├── LLM prompts & responses            │
│  ├── Error traces                       │
│  └── Security events                    │
│                                         │
│  Alerts:                                │
│  ├── Error rate > 5%                    │
│  ├── LLM latency > 10s                 │
│  ├── Low RAG relevance score            │
│  ├── Quota exceeded                     │
│  └── Security anomalies                │
│                                         │
│  AI Quality:                            │
│  ├── Citation accuracy rate             │
│  ├── User satisfaction (thumbs)         │
│  ├── Hallucination detection rate       │
│  └── Answer completeness score          │
└─────────────────────────────────────────┘
```

---

## 10. Cost Analysis

### Per-Request Cost Breakdown

| Component | Cost/Request | Notes |
|---|---|---|
| Claude Sonnet (input) | $0.003 | ~1K input tokens avg |
| Claude Sonnet (output) | $0.005 | ~500 output tokens avg |
| Embedding | $0.0001 | OpenAI ada-002 |
| Supabase DB | $0.00001 | Negligible |
| Compute | $0.001 | VPS amortized |
| **Total** | **~$0.009** | **~₹0.75/request** |

### Monthly Cost at Scale

| Users | Requests/mo | LLM Cost | Infra | Total | Revenue (₹10,000/user/mo ≈ $120) |
|---|---|---|---|---|---|
| 10 | 5,000 | $45 | $40 | $85 | $1,200 |
| 50 | 25,000 | $225 | $65 | $290 | $6,000 |
| 100 | 50,000 | $450 | $100 | $550 | $12,000 |
| 500 | 250,000 | $2,250 | $300 | $2,550 | $60,000 |

**Margin: 75-95%** depending on scale.
