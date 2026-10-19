# ⚖️ Legal AI Agent

🇮🇳 Made in India · **Live:** [lega.onrender.com](https://lega.onrender.com)

**AI-powered legal assistant for Indian businesses, grounded in the Constitution of India and Indian statutes**

An AI platform for legal research, contract review, and legal document drafting — all in a VSCode-style interface.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?style=flat-square)
![Render](https://img.shields.io/badge/Deploy-Render-46E3B7?style=flat-square)

---

## ✨ Features

### 🤖 AI Agent (25 Tools)
- **Legal search** — Search across the Constitution of India, Central Acts, IPC/BNS and other Indian legal documents
- **Contract review** — Risk analysis, missing clauses, amendment suggestions
- **Compliance check** — Verify employment/commercial/service contracts against Indian law
- **Clause drafting** — Generate confidentiality, penalty, termination, force majeure clauses...
- **Contract summary** — Quick summary of parties, value, duration
- **Contract comparison** — Side-by-side diff of 2 contracts
- **Company memory** — Remembers company context across chat sessions
- **📂 Full document control** — Read, write, edit, delete, organize documents autonomously

### 🦾 Agentic AI — Full Document Control

Legal AI can autonomously manage your documents and contracts:

#### What it can do:
- 📂 **Browse and search** — List all documents, search by folder/keyword/type
- 📖 **Read any document** — View full content, extract specific sections
- ✏️ **Edit specific clauses** — Find & replace text, track all changes
- 📝 **Generate new documents** — Draft contracts, memos, reports from scratch using AI
- 🔍 **Compare documents** — Side-by-side diff with similarity score
- 📋 **Review contracts for risks** — Batch review multiple files at once
- 🗂️ **Organize with folders** — Create folders, move files, tag documents
- 📊 **Batch operations** — Review 10+ contracts simultaneously
- 📜 **Track edit history** — Full audit trail of who changed what and when
- 🗑️ **Soft delete** — Delete documents with 30-day recovery window

#### Example Commands:
```
"List all contracts"
"Read lease agreement number 123"
"Edit the penalty clause in this contract to comply with the law"
"Draft an NDA between company A and B, duration 2 years"
"Compare the old and new version of the labor contract"
"Review all 5 contracts in the Project X folder"
"Create folder 'Client ABC' and move 3 contracts into it"
"View the edit history of this document"
```

#### Multi-Step Autonomous Workflows:
The AI can chain multiple tools together to complete complex tasks:

```
User: "Edit the penalty clause in Contract ABC to comply with the law"
AI: 
  1. read_document → Gets current content
  2. search_law → Finds the relevant law (Section 74, Indian Contract Act: reasonable compensation)
  3. edit_document → Replaces old penalty clause with compliant version
  4. document_history → Shows what changed
```

```
User: "Draft an NDA between company A and B, save to Client A folder"
AI:
  1. generate_document → Creates NDA from requirements
  2. create_folder → Creates "Client A" folder (if doesn't exist)
  3. write_document → Saves NDA to folder
```

#### Document Tools (11 of the 25):
1. `list_documents` — List all documents/contracts with search & filter
2. `read_document` — Read full content or specific sections
3. `write_document` — Create new documents with metadata & tags
4. `edit_document` — Find & replace text, track changes
5. `compare_documents` — Diff two documents (summary/detailed/clause-by-clause)
6. `create_folder` — Create organizational folders for cases/projects
7. `move_document` — Move documents between folders
8. `delete_document` — Soft delete (recoverable for 30 days)
9. `generate_document` — AI drafts legal documents from requirements
10. `batch_review` — Review multiple documents for risks simultaneously
11. `document_history` — View full edit history and audit trail

## 📋 Contract Review AI

Upload contracts for instant AI-powered review:

- ⚠️ **Risk identification and scoring** — 10 risk categories analyzed
- ⚖️ **Indian law compliance check** — Indian Contract Act 1872, Labour Codes 2020, Companies Act 2013
- 💡 **Revision suggestions** — Specific amendments with legal references
- 📊 **Clause-by-clause analysis** — Risk levels: LOW / MEDIUM / HIGH / CRITICAL
- 📄 **8+ contract templates** — Ready-to-use Indian templates

### Risk Categories Analyzed

1. **Unfavorable clauses** — One-sided clauses favoring one party
2. **High violation penalty** — Penalty/liquidated damages beyond reasonable compensation (Section 74, Indian Contract Act 1872)
3. **Unreasonable duration** — Unreasonable deadlines/terms
4. **Missing protective clauses** — Missing protective clauses
5. **Conflict with law** — Clauses contradicting Indian law (e.g. void restraints of trade under Section 27, Indian Contract Act)
6. **Auto-renewal clauses** — Auto-renewal traps
7. **Liability limitations** — Liability limitations
8. **Confidentiality and IP** — IP/confidentiality issues
9. **Dispute resolution** — Dispute resolution (arbitration vs court)
10. **Force majeure** — Missing or weak force majeure

### Supported Contract Types
- Employment
- Lease
- Sale
- Service
- NDA / Confidentiality
- Loan
- Agency
- Partnership

### API Usage

**Review a contract:**
```bash
POST /v1/contracts/{contract_id}/review-ai
```

**Get review results:**
```bash
GET /v1/contracts/{contract_id}/review-ai
```

**Response structure:**
```json
{
  "contract_title": "Commercial Lease Agreement",
  "contract_type": "lease",
  "parties": ["Acme Pvt Ltd", "Sharma Properties"],
  "risk_score": 72,
  "risk_level": "HIGH",
  "summary": "Lease with a one-sided penalty clause and no force majeure...",
  "clauses": [
    {
      "clause_number": "Clause 5",
      "title": "Penalty for breach",
      "content": "Lessee must pay 12 months' rent as penalty for any breach...",
      "risk_level": "CRITICAL",
      "risk_score": 90,
      "issue": "Fixed penalty unrelated to actual loss",
      "law_reference": "Section 74, Indian Contract Act 1872: only reasonable compensation is recoverable",
      "suggestion": "Replace with a genuine pre-estimate of loss, proportionate to the breach",
      "category": "penalty"
    }
  ],
  "missing_clauses": [
    {
      "clause": "Force Majeure",
      "importance": "HIGH",
      "suggestion": "Add a force majeure clause (see Section 56, Indian Contract Act 1872)"
    }
  ],
  "compliance": {
    "indian_contract_act_1872": {"status": "PARTIAL", "issues": ["Penalty clause"]},
    "companies_act_2013": {"status": "N_A", "issues": []},
    "labour_codes_2020": {"status": "N_A", "issues": []},
    "consumer_protection_act_2019": {"status": "N_A", "issues": []}
  },
  "recommendations": [
    {
      "priority": 1,
      "action": "Amend Clause 5 to a reasonable liquidated damages amount",
      "reason": "Section 74, Indian Contract Act 1872"
    }
  ]
}
```

### 📊 Dashboard & Analytics
- Risk Dashboard — Overview of risks across all contracts
- Contract Calendar — Monthly contract schedule
- Usage Analytics — Usage stats, top queries
- Audit Log — Activity journal

### 🎯 Enterprise Features
- Batch upload (10 files at a time)
- Report export (.docx)
- Contract versioning & notes
- Smart suggestions (AI-powered contract improvements)
- Bulk analysis (analyze 20 contracts simultaneously)
- Universal search (contracts + docs + laws + chats)
- Template auto-fill
- Onboarding wizard

### 🏗️ Platform Administration

Self-hosted deployments include a full **Platform Super Admin** panel for system administration:

#### Access
Navigate to `/platform-admin` (requires superadmin role)

#### Features
- **📊 Dashboard** — Real-time platform statistics, usage trends, top companies
- **🏢 Multi-tenant Management** — Manage all companies, change plans, set quotas, activate/deactivate
- **👥 User Management** — View all users across tenants, change roles, manage permissions
- **⚙️ System Settings** — Configure LLM provider, file limits, registration settings, feature flags
- **💰 LLM Usage & Cost Tracking** — Token usage by provider/company, estimated monthly costs
- **📋 Audit Logs** — Full platform-level action logging with user attribution
- **🔧 Maintenance Tools** — DB statistics, cleanup scripts, reindex operations

The Platform Admin panel provides complete control over your self-hosted Legal AI deployment:

```bash
# Navigate to platform admin
https://lega.onrender.com/platform-admin

# Available stats:
- Total companies, users, documents, contracts
- Indian law database size (documents and chunks indexed)
- Daily/monthly query volumes
- Active users, storage usage
- Usage trends (30-day charts)
- Revenue estimates by plan

# Management capabilities:
- Create/edit/deactivate companies
- Change subscription plans (trial → starter → pro → enterprise)
- Adjust quota limits per company
- Reset user passwords, change roles
- View company-specific usage history
- Configure system-wide settings
- Track LLM costs per company
- Full audit trail of admin actions
```

### 📱 Modern UI
- VSCode-style 3-panel layout
- Dark/Light theme
- Mobile responsive (bottom tab bar)
- PWA installable
- SSE streaming chat
- Command palette (Ctrl+K)
- Keyboard shortcuts

### 🕷️ Data Crawler (Powered by CrawlKit)
Legal AI Agent can automatically crawl Indian legal websites to build and update your document database.

#### Supported Sources
- 📚 **India Code** (indiacode.nic.in) — Official repository of Central and State Acts
- 🏛️ **Legislative Department** (legislative.gov.in) — Constitution of India and Acts of Parliament
- ⚖️ **Indian Kanoon** (indiankanoon.org) — Acts and judgments
- 🌐 **Any legal website URL** — Custom legal document sources

#### Setup
1. Get your free API key at [crawlkit.org](https://crawlkit.org)
2. Add to `.env`:
   ```
   CRAWLKIT_API_KEY=your_api_key_here
   ```
3. Start crawling!

#### Usage

**Via API:**
```bash
POST /crawler/crawl
{
  "url": "https://www.indiacode.nic.in/handle/123456789/..."
}
```

**Via AI Chat:**
```
"Crawl the Act at https://www.indiacode.nic.in/handle/123456789/1362"
```

**Other endpoints:**
- `GET /crawler/sources` — List supported legal sources
- `POST /crawler/discover` — Discover legal document links from a page
- `POST /crawler/batch` — Batch crawl multiple URLs
- `GET /crawler/status` — Check CrawlKit configuration

CrawlKit has a free tier; see [crawlkit.org](https://crawlkit.org) for current limits and pricing.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11
- A [Supabase](https://supabase.com) project (PostgreSQL)
- An LLM API key: [Groq](https://console.groq.com) or [Gemini](https://aistudio.google.com) for the server default. Users can add their own Claude, OpenAI or Gemini key in Settings.

### 1. Clone & Install

```bash
git clone https://github.com/ShubhiGoel5/LegalAI.git
cd LegalAI
pip install -r requirements.txt
```

### 2. Configure

```bash
cp .env.example .env
# Fill in the Supabase and LLM values in .env
```

Use Supabase's **Session pooler** connection details for `SUPABASE_DB_HOST` and `DB_USER` (Connect → Session pooler).

### 3. Database Setup

```bash
# Create tables (runs database/init.sql)
python scripts/run_migration.py

# Load Indian law data (Constitution of India Parts I-III, IPC 1860)
python scripts/download_indian_datasets.py
python scripts/load_indian_law.py
```

### 4. Run

```bash
uvicorn src.api.main:app --host 0.0.0.0 --port 8080
```

Open http://localhost:8080 (landing page) or http://localhost:8080/static/app.html (app).

## ☁️ Deploy on Render

The repo includes `render.yaml`:

1. In Render, create a **Blueprint** (or Web Service) from this GitHub repo.
2. Set the environment variables marked `sync: false` in `render.yaml` (Supabase keys, DB host and password, `GROQ_API_KEY`).
3. Deploy. Check `https://<your-app>.onrender.com/health`. It should show `"database": "connected"`.

Render's free tier sleeps after 15 minutes without traffic. `.github/workflows/keep-alive.yml` pings `/health` every 10 minutes to keep it awake.

## 📁 Project Structure

```
├── src/
│   ├── api/
│   │   ├── main.py              # FastAPI app + all routes
│   │   ├── routes/              # Route modules
│   │   │   ├── auth.py          # Login, register, API keys
│   │   │   ├── contracts.py     # Contract CRUD
│   │   │   ├── documents.py     # Document upload
│   │   │   ├── chats.py         # Chat history
│   │   │   ├── company.py       # Company management
│   │   │   └── admin.py         # Admin dashboard
│   │   └── middleware/
│   │       ├── auth.py          # API key verification
│   │       └── logging.py       # Usage logging
│   ├── agents/
│   │   ├── legal_agent.py       # AI agent with 25 tools
│   │   └── company_memory.py    # Company context memory
│   ├── services/
│   │   ├── llm_provider.py      # Claude / OpenAI / Gemini / Groq / custom
│   │   └── contract_review.py   # AI contract review
│   └── data/contract_templates/ # 8 Indian contract templates
├── static/
│   ├── app.html                 # Main SPA (~6800 lines)
│   ├── index.html               # Landing page
│   ├── admin.html               # Company admin dashboard
│   ├── platform-admin.html      # Platform super admin
│   └── manifest.json            # PWA manifest
├── database/
│   ├── init.sql                 # Full schema
│   └── migration_search.sql     # Law search function & indexes
├── scripts/
│   ├── download_indian_datasets.py  # Download Constitution & IPC data
│   ├── load_indian_law.py       # Load law library into Supabase
│   └── run_migration.py         # Runs database/init.sql
├── .github/workflows/
│   ├── ci.yml                   # Tests
│   └── keep-alive.yml           # Keeps Render free tier awake
├── render.yaml                  # Render deployment
├── .env.example                 # Environment template
└── requirements.txt
```

## 🔧 API Endpoints

### Auth
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/v1/auth/register` | Register |
| POST | `/v1/auth/login` | Login |
| GET | `/v1/keys` | List API keys |
| POST | `/v1/keys` | Generate API key |

### AI Chat
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/v1/legal/ask` | Ask AI agent |
| POST | `/v1/legal/ask-stream` | Ask AI (SSE streaming) |

### Contracts
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/contracts` | List contracts |
| POST | `/v1/contracts` | Upload contract |
| POST | `/v1/contracts/batch-upload` | Batch upload contracts |
| POST | `/v1/contracts/{id}/review` | AI contract review |
| POST | `/v1/contracts/{id}/report` | Export Word report |
| POST | `/v1/contracts/{id}/diff` | Compare 2 contracts |
| GET | `/v1/contracts/{id}/suggestions` | AI suggestions |
| POST | `/v1/contracts/bulk-analyze` | Bulk analysis |
| GET | `/v1/contracts/calendar` | Contract calendar |
| GET | `/v1/contracts/risk-overview` | Risk overview |

### Search
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/legal/search` | Search laws |
| GET | `/v1/search/all` | Search everything |

### Analytics
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/analytics` | Usage statistics |
| GET | `/v1/audit-log` | Activity log |
| GET | `/v1/insights` | AI insights |

## 🤖 Multi-LLM Provider Support

**Bring Your Own LLM** — Connect your preferred AI provider with **API Key** or **OAuth**:

### Supported Providers

| Provider | Models | Auth Methods | Context |
|----------|--------|--------------|---------|
| 🔵 **Anthropic Claude** | Claude models | API Key | Large |
| 🟢 **OpenAI GPT** | GPT models | API Key, OAuth | Large |
| 🔴 **Google Gemini** | Gemini models | API Key, OAuth | Very large |
| 🟠 **Groq** | Llama 3.3 70B (server default) | API Key (env) | Large |
| ⚫ **Custom/Local** | Ollama, vLLM, LM Studio | API Key | Variable |

The available models are listed in the app (Settings → AI Provider) and by `GET /v1/llm/models`.

### Configuration

1. **Via Dashboard:** Settings → AI Provider → Choose provider → Enter API key
2. **Via API:** `POST /v1/llm/configure` with your API key
3. **OAuth (OpenAI/Gemini):** Click "Connect with [Provider]" → Authorize → Done

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/v1/llm/providers` | List all providers + models |
| POST | `/v1/llm/configure` | Set API key (manual) |
| POST | `/v1/llm/test` | Test current connection |
| GET | `/v1/llm/status` | Current provider status |
| GET | `/v1/llm/models` | List models |
| POST | `/v1/llm/model` | Set model |
| GET | `/v1/llm/oauth/{provider}/authorize` | Start OAuth flow |
| GET | `/v1/llm/oauth/callback` | OAuth callback |
| POST | `/v1/llm/oauth/{provider}/refresh` | Refresh OAuth token |

### Features

- ✅ **Unified Interface:** Agent works with any LLM — no code changes
- 🔒 **Encrypted Storage:** API keys encrypted with Fernet (AES-256)
- 🔄 **OAuth Support:** Automated token management for OpenAI & Google
- 🛠️ **Tool Normalization:** Function calling formats normalized across providers
- 💾 **Company-Level Config:** Each company can use different LLM
- 🔁 **Fallback:** If a company hasn't configured a provider, the server uses `GEMINI_API_KEY`, then `GROQ_API_KEY`

### Environment Variables

```bash
# Encryption key for API keys (generate with: python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())")
LLM_ENCRYPTION_KEY=your-32-byte-key

# OAuth credentials (optional, for OAuth flow)
OPENAI_CLIENT_ID=your-openai-client-id
OPENAI_CLIENT_SECRET=your-openai-client-secret
GEMINI_CLIENT_ID=your-google-client-id
GEMINI_CLIENT_SECRET=your-google-client-secret
OAUTH_REDIRECT_URI=http://localhost:8080/v1/llm/oauth/callback

# Server default LLM (used when a company hasn't configured a provider)
GEMINI_API_KEY=your-gemini-key        # tried first
GROQ_API_KEY=your-groq-key            # used if no Gemini key
```

## 💰 Pricing

| Tier | INR / month | USD / month | Queries/day | Contracts | Key Features |
|------|-------------|-------------|-------------|-----------|--------------|
| **Free** | ₹0 | $0 | 10 | 1 | Law search, 2 templates |
| **Starter** | ₹2,400 | $29 | 100 | 20 | AI review, all templates, up to 3 users |
| **Professional** | ₹8,200 | $99 | 500 | Unlimited | API, custom LLM, analytics, up to 10 users |
| **Enterprise** | ₹41,500 | $499 | Unlimited | Unlimited | SLA, dedicated support, white-label |

Prices exclude GST; 14-day free trial, no credit card. **Discounts:** annual −20% · startups under 2 years −30% · registered non-profits −50%. Prices come from `src/data/pricing.json`.

```bash
GET /v1/pricing  # Get pricing tiers
```

## 📄 Contract Templates

8 ready-to-use Indian contract templates:

| Template | Law Reference |
|----------|--------------|
| Employment Agreement | Code on Social Security 2020, OSH Code 2020 |
| Lease Agreement | Transfer of Property Act 1882 |
| Sale Agreement | Sale of Goods Act 1930 |
| Service Agreement | Indian Contract Act 1872, Income Tax Act 1961 (TDS) |
| Partnership Agreement | Indian Partnership Act 1932 |
| Non-Disclosure Agreement | Indian Contract Act 1872, IT Act 2000 |
| Loan Agreement | Indian Contract Act 1872, Negotiable Instruments Act 1881 |
| Agency Agreement | Indian Contract Act 1872 (Sections 182–238) |

All templates include `{{fillable_fields}}`, legal notes, and specific law article references.

```bash
GET /v1/templates              # List all templates
GET /v1/templates/{id}         # Get template content
POST /v1/templates/generate    # AI-fill template
```

## 🌐 Multi-Language (i18n)

English is the default. Hindi (`hi`) is supported by the language detector; add `src/i18n/hi.json` to provide translations.

```bash
# English (default)
curl "/v1/pricing?lang=en"

# Hindi
curl "/v1/pricing?lang=hi"
```

## 🛠️ Tech Stack

- **Backend:** FastAPI + Python
- **AI:** Multi-LLM (Claude, GPT, Gemini, Custom) via unified provider interface
- **Database:** PostgreSQL (Supabase) with pgvector
- **Search:** PostgreSQL full-text search + phrase matching + synonym expansion
- **Frontend:** Vanilla JS SPA (single HTML file)
- **Deploy:** Render (`render.yaml`)

## 📝 Indian Law Database

`scripts/load_indian_law.py` currently loads:
- **Constitution of India:** Preamble and Articles 1–35 (Parts I–III, including Fundamental Rights)
- **Indian Penal Code, 1860:** all sections (replaced by the Bharatiya Nyaya Sanhita, 2023 for offences on or after 1 July 2024)

Planned: the rest of the Constitution, BNS 2023, Indian Contract Act 1872, Companies Act 2013, the four Labour Codes, Income Tax and GST Acts, IT Act 2000 and DPDP Act 2023. More Central Acts can be added with the crawler (India Code).

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. Areas that need help:
- [ ] More Indian legal document sources (State Acts, Supreme Court and High Court judgments)
- [ ] Better NLP for Hindi and other Indian languages
- [ ] Test coverage
- [ ] Multi-language support

## 📄 License

MIT — free to use, including commercially.

## ⚠️ Disclaimer

This is an assistive tool and **does not replace** professional legal advice. Always consult a qualified lawyer for important legal decisions.


