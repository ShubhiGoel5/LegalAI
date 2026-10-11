# Legal AI Platform v2 — Full Legal Department Replacement

> **Vision:** Fully replace the traditional in-house legal function for Indian businesses — grounded in the Constitution of India, Acts of Parliament, State Acts, Rules, Regulations and Notifications.
> Not just a chatbot — a **Legal Operating System**. Made in India, for Indian law.

---

## 1. Product Vision

```
BEFORE (Traditional):                    AFTER (Legal AI Platform):
                                         
Law firm retainer ── ₹50K-2L/month       ┌─────────────────────────┐
In-house legal staff ── ₹40K-1L/month    │   LEGAL AI PLATFORM     │
                                         │                         │
Draft contract ──── 2-3 days             │   Draft ──── 5 minutes  │
Review contract ── 1-2 days              │   Review ─── 30 seconds │
Legal research ── several hours          │   Research ── instant   │
Draft HR policies ── 1 week              │   Policies ── 10 min    │
Advice ───── book appointment, wait      │   Advice ─── 24/7       │
                                         │                         │
Cost: ₹1L-3L/month                       │   Cost: ₹10K-25K/month  │
                                         └─────────────────────────┘
```

---

## 2. Platform Modules

```
┌─────────────────────────────────────────────────────────────┐
│                    LEGAL AI PLATFORM                         │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐   │
│  │  📄 DRAFT    │  │  🔍 REVIEW   │  │  💬 CONSULT      │   │
│  │  Document    │  │  Contract    │  │  Legal           │   │
│  │  drafting    │  │  review      │  │  advice          │   │
│  └──────────────┘  └──────────────┘  └──────────────────┘   │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐   │
│  │  📚 LIBRARY  │  │  ✅ COMPLY   │  │  📊 MANAGE       │   │
│  │  Templates & │  │  Legal       │  │  Company         │   │
│  │  laws        │  │  compliance  │  │  documents       │   │
│  └──────────────┘  └──────────────┘  └──────────────────┘   │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐                         │
│  │  🔄 BATCH    │  │  🔌 API      │                         │
│  │  Bulk        │  │  System      │                         │
│  │  processing  │  │  integration │                         │
│  └──────────────┘  └──────────────┘                         │
└─────────────────────────────────────────────────────────────┘
```

### Module 1: DRAFT
**Replaces:** Lawyers drafting contracts, admin staff drafting documents
```
Input:  Document type + required details
Output: Complete document (Word/PDF), compliant with Indian law

Supports:
├── Contracts (employment, services, sale of goods, lease, joint venture, agency/distribution)
├── Addenda (extension, amendment, supplement, settlement/closure)
├── Internal documents (standing orders, HR policies, office orders, notices, minutes)
├── External documents (official letters, powers of attorney, complaints)
├── HR documents (appointment letters, salary revisions, disciplinary action, termination, EPF/ESI)
└── Legal reports (compliance, audits, risk assessment)
```

### Module 2: REVIEW
**Replaces:** Lawyers reviewing contracts
```
Input:  Contract file (PDF/Word/image)
Output: Risk report + suggested amendments

Functions:
├── Detect clauses that violate the law (e.g. void restraints under Section 27, Indian Contract Act 1872)
├── Highlight unfavourable clauses (e.g. penalty clauses — Section 74, Indian Contract Act 1872)
├── Check for omissions (mandatory clauses, stamp duty, GST/TDS terms)
├── Compare against standard templates
├── Suggest specific amendments
├── Risk scoring (0-100)
└── Generate redline version (tracked changes)
```

### Module 3: CONSULT
**Replaces:** Legal consultants, legal helplines
```
Input:  Legal question (text/voice)
Output: Answer + precise citations of the relevant provisions

Functions:
├── Legal Q&A across 37+ practice areas
├── Accurate citation of Articles of the Constitution, sections of Acts, Rules
├── Fact-specific situation analysis
├── Suggested next steps
├── Consultation history (audit trail)
└── Multi-language (English/Hindi + regional Indian languages)
```

### Module 4: LIBRARY
**Replaces:** Legal bookshelf, paid legal research services
```
├── 600+ Indian legal texts (Constitution of India, Central & State Acts, Rules, Regulations,
│   Notifications, Circulars from RBI/SEBI/MCA)
├── Template library (50+ document templates)
├── Smart search (semantic + keyword)
├── Cross-reference (related laws)
├── Version tracking (amendments)
├── Bookmark & highlight
└── Auto-update when new laws are notified in the Gazette of India
```

### Module 5: COMPLY
**Replaces:** Legal compliance audits
```
Input:  Company information (industry, size, operations, state)
Output: Compliance checklist + violation alerts

Functions:
├── Industry-specific compliance checklist
├── Deadline reminders (GST, TDS, EPF/ESI, fire safety)
├── Scan internal policies against current law
├── Alerts when new laws affect the company
└── Periodic compliance reports
```

### Module 6: MANAGE
**Replaces:** Filing cabinets, Excel tracking
```
├── Company document repository (upload, classify, search)
├── Contract tracking (expiry, renewal)
├── Version control (who changed what, when)
├── Approval workflow (draft → review → approve)
├── Deadline reminders (contracts expiring, licences expiring)
└── Summary reports (number of contracts, status)
```

### Module 7: BATCH
**Replaces:** Admin/HR drafting hundreds of employment contracts
```
Input:  Template + Excel data (name, salary, position...)
Output: Complete documents in bulk

Use cases:
├── 500 appointment letters for new workers
├── 200 contract extension addenda
├── 100 salary revision letters
├── 50 termination notices
└── Batch export Word/PDF
```

### Module 8: API
```
REST API + WebSocket + SDK
├── Integrate with existing ERP/HRM systems
├── Webhook events (contract expiry, new laws)
├── Embeddable chat widget
├── Mobile SDK (iOS/Android)
└── Zapier / n8n integration
```

---

## 3. System Architecture v2

```
┌─────────────────────────────────────────────────────────────────┐
│                        CLIENT LAYER                              │
│                                                                 │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐           │
│  │   Web    │ │  Chat    │ │  Mobile  │ │  API     │           │
│  │Dashboard │ │ Widget   │ │  App     │ │ Direct   │           │
│  │(Next.js) │ │(Embed)   │ │(Future)  │ │(REST)    │           │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘           │
└───────┼─────────────┼────────────┼─────────────┼────────────────┘
        │             │            │             │
        └─────────────┴──────┬─────┴─────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                      API GATEWAY                                 │
│                                                                 │
│  ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌────────────────┐   │
│  │   Auth    │ │   Rate    │ │  Billing  │ │   Request      │   │
│  │ (Supabase │ │  Limiter  │ │  Meter    │ │   Router       │   │
│  │  + API    │ │  (Redis)  │ │           │ │                │   │
│  │  Keys)    │ │           │ │           │ │                │   │
│  └───────────┘ └───────────┘ └───────────┘ └────────────────┘   │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                    ┌────────────┼────────────┐
                    ▼            ▼            ▼
┌─────────────────────────────────────────────────────────────────┐
│                   ORCHESTRATOR LAYER                             │
│                   (FastAPI + LangGraph)                           │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐     │
│  │              INTENT ROUTER                               │     │
│  │  "Draft an employment contract" → DRAFT agent           │     │
│  │  "Review this file" → REVIEW agent                      │     │
│  │  "How long is maternity leave?" → CONSULT agent         │     │
│  │  "Create 500 offer letters from Excel" → BATCH agent    │     │
│  │  "What must my company comply with?" → COMPLY agent     │     │
│  └─────────────────────────────────────────────────────────┘     │
│                                                                 │
│  ┌────────────────── AGENT POOL ──────────────────────────┐     │
│  │                                                        │     │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐  │     │
│  │  │  DRAFT   │ │  REVIEW  │ │ CONSULT  │ │  COMPLY  │  │     │
│  │  │  Agent   │ │  Agent   │ │  Agent   │ │  Agent   │  │     │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘  │     │
│  │                                                        │     │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐               │     │
│  │  │  BATCH   │ │ LIBRARY  │ │  MANAGE  │               │     │
│  │  │  Agent   │ │  Agent   │ │  Agent   │               │     │
│  │  └──────────┘ └──────────┘ └──────────┘               │     │
│  └────────────────────────────────────────────────────────┘     │
│                                                                 │
│  ┌────────────────── SHARED SERVICES ────────────────────┐     │
│  │                                                        │     │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐  │     │
│  │  │Citation  │ │Halluc.   │ │ Template │ │ Document │  │     │
│  │  │Verifier  │ │Guard     │ │ Engine   │ │ Builder  │  │     │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘  │     │
│  │                                                        │     │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐               │     │
│  │  │ Context  │ │ Compliance│ │ Export   │               │     │
│  │  │ Manager  │ │ Checker  │ │ Service  │               │     │
│  │  └──────────┘ └──────────┘ └──────────┘               │     │
│  └────────────────────────────────────────────────────────┘     │
└────────────────────────────────┬────────────────────────────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              ▼                  ▼                  ▼
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│   RAG ENGINE     │  │   LLM LAYER      │  │   TOOL LAYER     │
│                  │  │                  │  │                  │
│ Hybrid Search    │  │ Claude Sonnet    │  │ OCR (Surya)      │
│ (pgvector +      │  │ (primary)        │  │ PDF Parser       │
│  full-text)      │  │                  │  │ DOCX Generator   │
│                  │  │ Claude Haiku     │  │ PDF Generator    │
│ Reranker         │  │ (fast tasks)     │  │ Excel Reader     │
│                  │  │                  │  │ Template Render  │
│ Context Builder  │  │ Gemini Flash     │  │ E-Sign (future)  │
│                  │  │ (batch/cheap)    │  │ Web Search       │
└────────┬─────────┘  └────────┬─────────┘  └────────┬─────────┘
         │                     │                     │
         └─────────────────────┼─────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                      SUPABASE LAYER                              │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐   │
│  │                    PostgreSQL                              │   │
│  │                                                           │   │
│  │  ┌─────────────┐  ┌──────────────┐  ┌──────────────────┐  │   │
│  │  │  Tenants    │  │  Law DB      │  │  pgvector        │  │   │
│  │  │  (companies │  │  (636+ docs) │  │  (embeddings)    │  │   │
│  │  │  users,     │  │              │  │                  │  │   │
│  │  │  docs,      │  │  Constitution│  │  law_chunks      │  │   │
│  │  │  contracts) │  │  Acts, Rules │  │  company_chunks  │  │   │
│  │  │  RLS        │  │              │  │  template_chunks │  │   │
│  │  │  isolated   │  │  PUBLIC READ │  │                  │  │   │
│  │  └─────────────┘  └──────────────┘  └──────────────────┘  │   │
│  └───────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────┐     │
│  │  Auth    │  │ Storage  │  │ Realtime │  │  Edge        │     │
│  │ (Users + │  │ (Docs,   │  │ (Chat,   │  │  Functions   │     │
│  │ API Keys)│  │ exports) │  │ notify)  │  │  (webhooks)  │     │
│  └──────────┘  └──────────┘  └──────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. Document Generation Engine (Core Innovation)

```
┌─────────────────────────────────────────────────────────────────┐
│               DOCUMENT GENERATION ENGINE                         │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐   │
│  │                 TEMPLATE SYSTEM                            │   │
│  │                                                           │   │
│  │  Templates are NOT static Word files.                     │   │
│  │  They are INTELLIGENT SCHEMAS:                            │   │
│  │                                                           │   │
│  │  ┌─────────────────────────────────────────────┐          │   │
│  │  │  Template: "employment_contract"            │          │   │
│  │  │                                             │          │   │
│  │  │  Sections:                                  │          │   │
│  │  │  ├── header (company info, date, number)    │          │   │
│  │  │  ├── parties (employer + employee info)     │          │   │
│  │  │  ├── position (job title, department)       │          │   │
│  │  │  ├── term (duration, start date)            │          │   │
│  │  │  ├── salary (base, allowance, bonus)        │          │   │
│  │  │  ├── working_hours (schedule, overtime)     │          │   │
│  │  │  ├── insurance (EPF, ESI, gratuity)         │          │   │
│  │  │  ├── leave (annual, sick, maternity)        │          │   │
│  │  │  ├── obligations (employer + employee)      │          │   │
│  │  │  ├── termination (conditions, notice)       │          │   │
│  │  │  ├── dispute (resolution method)            │          │   │
│  │  │  └── signatures                             │          │   │
│  │  │                                             │          │   │
│  │  │  Required by law: [term, salary, insurance] │          │   │
│  │  │  Legal refs: [Contract Act, Code on Wages]  │          │   │
│  │  │  Compliance rules: [min wage, 48h/week, ...]│          │   │
│  │  └─────────────────────────────────────────────┘          │   │
│  └───────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐   │
│  │                 GENERATION PIPELINE                        │   │
│  │                                                           │   │
│  │  ① Collect Variables                                      │   │
│  │  ┌─────────────────────────────────┐                      │   │
│  │  │ Interactive Q&A or API params:  │                      │   │
│  │  │ - company_name: "Acme Pvt Ltd"  │                      │   │
│  │  │ - employee_name: "Rahul Sharma" │                      │   │
│  │  │ - position: "Production Worker" │                      │   │
│  │  │ - salary: 18000                 │                      │   │
│  │  │ - term_months: 12               │                      │   │
│  │  └─────────────────────────────────┘                      │   │
│  │                    │                                      │   │
│  │                    ▼                                      │   │
│  │  ② Validate & Enrich                                     │   │
│  │  ┌─────────────────────────────────┐                      │   │
│  │  │ - Salary >= minimum wage? ✅     │                      │   │
│  │  │ - Hours <= 48/week? ✅           │                      │   │
│  │  │ - Required fields present? ✅    │                      │   │
│  │  │ - Auto-calculate EPF/ESI rates  │                      │   │
│  │  │ - Auto-add required clauses     │                      │   │
│  │  └─────────────────────────────────┘                      │   │
│  │                    │                                      │   │
│  │                    ▼                                      │   │
│  │  ③ Generate with LLM                                     │   │
│  │  ┌─────────────────────────────────┐                      │   │
│  │  │ Template schema + variables     │                      │   │
│  │  │ + relevant law articles         │                      │   │
│  │  │ + company custom rules          │                      │   │
│  │  │         │                       │                      │   │
│  │  │         ▼                       │                      │   │
│  │  │    Claude Sonnet                │                      │   │
│  │  │         │                       │                      │   │
│  │  │         ▼                       │                      │   │
│  │  │  Complete document (markdown)   │                      │   │
│  │  └─────────────────────────────────┘                      │   │
│  │                    │                                      │   │
│  │                    ▼                                      │   │
│  │  ④ Compliance Check                                      │   │
│  │  ┌─────────────────────────────────┐                      │   │
│  │  │ Verify generated doc against:   │                      │   │
│  │  │ - Relevant law articles         │                      │   │
│  │  │ - Template required sections    │                      │   │
│  │  │ - Company-specific rules        │                      │   │
│  │  │ - Common legal pitfalls         │                      │   │
│  │  └─────────────────────────────────┘                      │   │
│  │                    │                                      │   │
│  │                    ▼                                      │   │
│  │  ⑤ Export                                                │   │
│  │  ┌─────────────────────────────────┐                      │   │
│  │  │ Markdown → DOCX (python-docx)  │                      │   │
│  │  │ Markdown → PDF (weasyprint)    │                      │   │
│  │  │ With: company logo, formatting │                      │   │
│  │  │       page numbers, headers    │                      │   │
│  │  │       signature blocks         │                      │   │
│  │  └─────────────────────────────────┘                      │   │
│  └───────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5. Batch Processing Engine

```
┌─────────────────────────────────────────────────────────────────┐
│                  BATCH PROCESSING ENGINE                         │
│          "500 employment contracts in 10 minutes"               │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐   │
│  │  Input: Excel/CSV + Template                              │   │
│  │                                                           │   │
│  │  Excel columns mapping:                                   │   │
│  │  ┌──────────────────────────────────────────────────┐     │   │
│  │  │ Name      │ DOB       │ Employee ID│ Position    │     │   │
│  │  │ Rahul S.  │ 01/01/90  │ EMP-0001   │ Operator    │     │   │
│  │  │ Priya K.  │ 15/03/95  │ EMP-0002   │ QC          │     │   │
│  │  │ ...       │ ...       │ ...        │ ...         │     │   │
│  │  │ (500 rows)│           │            │             │     │   │
│  │  └──────────────────────────────────────────────────┘     │   │
│  └───────────────────────────────────────────────────────────┘   │
│                           │                                     │
│                           ▼                                     │
│  ┌───────────────────────────────────────────────────────────┐   │
│  │  Processing Pipeline:                                     │   │
│  │                                                           │   │
│  │  Row 1 ──→ Validate ──→ Generate ──→ Check ──→ DOCX  ─┐  │   │
│  │  Row 2 ──→ Validate ──→ Generate ──→ Check ──→ DOCX  ─┤  │   │
│  │  Row 3 ──→ Validate ──→ Generate ──→ Check ──→ DOCX  ─┤  │   │
│  │  ...                                                  ─┤  │   │
│  │  Row N ──→ Validate ──→ Generate ──→ Check ──→ DOCX  ─┤  │   │
│  │                                                        │  │   │
│  │  Parallel processing: 10-20 concurrent (Celery workers) │  │   │
│  │  LLM: Use Gemini Flash for batch (cheaper, fast enough) │  │   │
│  └──────────────────────────────────────────────────────┬──┘   │
│                                                        │       │
│                                                        ▼       │
│  ┌───────────────────────────────────────────────────────────┐   │
│  │  Output:                                                  │   │
│  │  ├── /batch_001/EMP_RahulSharma.docx                     │   │
│  │  ├── /batch_001/EMP_PriyaKumar.docx                      │   │
│  │  ├── /batch_001/...                                       │   │
│  │  ├── /batch_001/SUMMARY.xlsx (tracking sheet)             │   │
│  │  └── /batch_001/ALL.zip (download all)                    │   │
│  │                                                           │   │
│  │  Summary: 500 created, 498 OK, 2 warnings                │   │
│  └───────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 6. Template Library Architecture

```
Template Categories:
│
├── 📁 Contracts
│   ├── employment_contract (Permanent / fixed-term employment contract)
│   ├── probation_agreement (Probation terms)
│   ├── service_agreement (Service agreement)
│   ├── sale_of_goods_agreement (Sale of goods — Sale of Goods Act 1930)
│   ├── lease_agreement (Lease of premises/equipment — Transfer of Property Act 1882)
│   ├── joint_venture_agreement (Business cooperation / joint venture)
│   ├── agency_agreement (Agency / distribution)
│   ├── loan_agreement (Loan agreement)
│   ├── job_work_agreement (Job work / contract manufacturing)
│   └── franchise_agreement (Franchise agreement)
│
├── 📁 Addenda (Appendices)
│   ├── addendum_extension (Contract extension)
│   ├── addendum_amendment (Amendment of terms)
│   ├── addendum_supplement (Additional terms)
│   ├── addendum_settlement (Final settlement / closure of contract)
│   └── addendum_termination (Contract termination)
│
├── 📁 HR Letters & Orders (Decisions)
│   ├── appointment_letter (Hiring / appointment)
│   ├── designation_order (Appointment to a position / promotion)
│   ├── salary_revision_letter (Salary increment)
│   ├── disciplinary_order (Disciplinary action after domestic enquiry)
│   ├── dismissal_order (Dismissal for misconduct)
│   ├── relieving_letter (Separation / relieving)
│   ├── transfer_order (Transfer)
│   └── deputation_order (Deputation / business travel)
│
├── 📁 Standing Orders & Policies (Policies)
│   ├── standing_orders (Standing orders — Industrial Employment (Standing Orders) Act 1946)
│   ├── salary_policy (Salary & bonus policy)
│   ├── finance_policy (Financial policy)
│   ├── recruitment_procedure (Recruitment procedure)
│   ├── training_procedure (Training procedure)
│   ├── posh_policy (Prevention of sexual harassment — POSH Act 2013)
│   └── settlement_agreement (Memorandum of settlement with union — Industrial Relations Code 2020)
│
├── 📁 Letters & Applications (Correspondence)
│   ├── official_letter (Official letter)
│   ├── power_of_attorney (Power of attorney)
│   ├── leave_application (Leave application)
│   ├── complaint_letter (Complaint / grievance)
│   ├── invitation_letter (Invitation letter)
│   └── notice (Notice)
│
├── 📁 Minutes & Records (Minutes)
│   ├── meeting_minutes (Meeting minutes)
│   ├── handover_record (Handover / delivery record)
│   ├── incident_record (Misconduct / incident record)
│   ├── inspection_record (Inspection record)
│   └── board_resolution (Board resolution — Companies Act 2013)
│
└── 📁 Reports (Reports)
    ├── epf_esi_return (EPF / ESI monthly returns)
    ├── tds_return (TDS returns — Income Tax Act 1961)
    ├── labour_return (Annual / half-yearly labour returns)
    └── fire_safety_report (Fire safety compliance report)

Template Schema (JSON):
{
  "id": "employment_contract",
  "name": "Employment Contract",
  "category": "contracts",
  "version": "2.0",
  "legal_basis": ["Indian Contract Act 1872", "Code on Wages 2019", "Industrial Relations Code 2020", "Code on Social Security 2020"],
  "variables": [
    {"key": "company_name", "label": "Company Name", "type": "text", "required": true},
    {"key": "company_address", "label": "Registered Address", "type": "text", "required": true},
    {"key": "company_tax_code", "label": "GSTIN / PAN", "type": "text", "required": true},
    {"key": "representative", "label": "Authorised Signatory", "type": "text", "required": true},
    {"key": "representative_title", "label": "Position", "type": "text", "required": true},
    {"key": "employee_name", "label": "Employee Name", "type": "text", "required": true},
    {"key": "employee_dob", "label": "Date of Birth", "type": "date", "required": true},
    {"key": "employee_pan", "label": "PAN", "type": "text", "required": true},
    {"key": "employee_address", "label": "Employee Address", "type": "text", "required": true},
    {"key": "position", "label": "Position", "type": "text", "required": true},
    {"key": "department", "label": "Department", "type": "text"},
    {"key": "work_location", "label": "Place of Work", "type": "text", "required": true},
    {"key": "contract_type", "label": "Employment Type", "type": "enum", "options": ["permanent", "fixed_term", "temporary"], "required": true},
    {"key": "term_months", "label": "Term (months)", "type": "number", "condition": "contract_type == 'fixed_term'"},
    {"key": "start_date", "label": "Start Date", "type": "date", "required": true},
    {"key": "base_salary", "label": "Base Salary", "type": "currency", "required": true, "min": "minimum_wage"},
    {"key": "allowances", "label": "Allowances", "type": "json"},
    {"key": "working_hours", "label": "Hours/week", "type": "number", "max": 48, "default": 48},
    {"key": "probation_days", "label": "Probation (days)", "type": "number", "max": 180}
  ],
  "sections": [...],
  "compliance_rules": [
    {"rule": "base_salary >= minimum_wage", "message": "Wages must not be below the applicable minimum wage (Code on Wages 2019)"},
    {"rule": "working_hours <= 48", "message": "Working hours must not exceed 48 hours/week (OSH Code 2020)"},
    {"rule": "probation_days <= 180", "message": "Probation beyond 6 months should be justified under the applicable standing orders"},
    {"rule": "no_post_employment_non_compete", "message": "Post-employment non-compete clauses are generally void (Section 27, Indian Contract Act 1872)"}
  ]
}
```

---

## 7. Compliance Engine

```
┌─────────────────────────────────────────────────────────────────┐
│                    COMPLIANCE ENGINE                             │
│         "Is your company legally compliant?"                    │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐   │
│  │  Company Profile:                                         │   │
│  │  - Industry: Manufacturing                                │   │
│  │  - Size: 500 employees                                    │   │
│  │  - Location: Pune, Maharashtra                            │   │
│  │  - Operations: Electronics assembly                       │   │
│  └──────────────────────┬────────────────────────────────────┘   │
│                         │                                       │
│                         ▼                                       │
│  ┌───────────────────────────────────────────────────────────┐   │
│  │  Auto-Generate Compliance Checklist:                      │   │
│  │                                                           │   │
│  │  📋 Labour                                                │   │
│  │  ├── ✅ Appointment letters for all employees             │   │
│  │  ├── ✅ Certified standing orders (IESO Act 1946)         │   │
│  │  ├── ⚠️ Internal Committee under POSH Act 2013            │   │
│  │  ├── ✅ Factory licence / Shops & Establishments reg.     │   │
│  │  └── ❌ Annual returns under labour laws                  │   │
│  │                                                           │   │
│  │  📋 EPF / ESI / Gratuity                                  │   │
│  │  ├── ✅ EPF registration & monthly contributions          │   │
│  │  ├── ⚠️ ESI coverage for all eligible employees           │   │
│  │  └── ✅ Gratuity provision (5+ years of service)          │   │
│  │                                                           │   │
│  │  📋 Occupational Safety (OSH Code 2020)                   │   │
│  │  ├── ✅ Safety training for workers                       │   │
│  │  ├── ❌ Periodic medical examinations                     │   │
│  │  ├── ⚠️ Accident reporting                                │   │
│  │  └── ✅ Hazard risk assessment                            │   │
│  │                                                           │   │
│  │  📋 Fire Safety                                           │   │
│  │  ├── ✅ Fire NOC                                          │   │
│  │  ├── ⚠️ Periodic fire system inspection                   │   │
│  │  └── ✅ Annual fire drills                                │   │
│  │                                                           │   │
│  │  📋 Tax                                                   │   │
│  │  ├── ✅ Monthly GST returns (GSTR-1, GSTR-3B)             │   │
│  │  ├── ✅ Quarterly TDS returns                             │   │
│  │  └── ✅ Income tax return & tax audit                     │   │
│  │                                                           │   │
│  │  📋 Environment                                           │   │
│  │  ├── ⚠️ Consent to Operate (State Pollution Control Board)│   │
│  │  ├── ✅ Environmental impact assessment                   │   │
│  │  └── ❌ Annual environmental statement                    │   │
│  │                                                           │   │
│  │  Score: 72/100 | Issues: 3 critical, 5 warnings           │   │
│  └───────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐   │
│  │  Deadline Calendar:                                       │   │
│  │                                                           │   │
│  │  📅 07/03 — Deposit TDS for February                      │   │
│  │  📅 11/03 — File GSTR-1 for February                      │   │
│  │  📅 15/03 — EPF & ESI contributions for February          │   │
│  │  📅 15/03 — Advance tax (4th instalment)                  │   │
│  │  📅 20/03 — File GSTR-3B for February                     │   │
│  └───────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 8. Contract Lifecycle Management

```
┌─────────────────────────────────────────────────────────────────┐
│              CONTRACT LIFECYCLE                                  │
│                                                                 │
│  ┌─────┐    ┌────────┐    ┌────────┐    ┌────────┐    ┌──────┐  │
│  │Draft│───▶│Review  │───▶│Approve │───▶│Active  │───▶│Expire│  │
│  │     │    │        │    │        │    │        │    │      │  │
│  └─────┘    └────────┘    └────────┘    └───┬────┘    └──────┘  │
│    AI          AI           Human          │                    │
│  generates   checks       approves         │                    │
│                                            │                    │
│                              ┌─────────────┤                    │
│                              │             │                    │
│                              ▼             ▼                    │
│                         ┌────────┐    ┌────────┐               │
│                         │Amend   │    │Renew   │               │
│                         │addendum│    │extend  │               │
│                         └────────┘    └────────┘               │
│                                                                 │
│  Tracking Dashboard:                                            │
│  ├── 245 Active contracts                                       │
│  ├── 12 Expiring in 30 days ⚠️                                  │
│  ├── 3 Pending review                                           │
│  ├── 1 Compliance issue 🔴                                      │
│  └── Last created: 2 hours ago                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 9. Pricing Model (Updated)

### Pricing Philosophy: 
> **90% cheaper than retaining a law firm, but priced above a plain chatbot**
> Because we **CREATE value** (documents), not just answer questions

| Plan | Price/month | Includes | Target |
|---|---|---|---|
| **Starter** | ₹6,999 | 20 docs + 100 Q&A + 5 reviews | SMEs < 20 employees |
| **Business** | ₹16,999 | 100 docs + 500 Q&A + 20 reviews + compliance | SMEs 20-100 employees |
| **Enterprise** | ₹49,999 | Unlimited docs + Q&A + batch + API + SLA | Companies 100+ employees |
| **Custom** | Negotiable | White-label, dedicated, training | Business groups / conglomerates |

### Add-ons:
- Batch processing (500+ docs): ₹1,999/batch
- Custom template: ₹6,999/template
- Compliance audit: ₹9,999/audit
- API integration support: ₹16,999 setup

### Actual Cost Comparison:
| Item | Traditional | Legal AI Platform |
|---|---|---|
| Draft 1 employment contract | ₹2,000-10,000 (lawyer) | ~₹30 (AI) |
| Review 1 contract | ₹5,000-20,000 | ~₹150 |
| Standing orders / HR policy | ₹20,000-60,000 | ~₹700 |
| Hire Legal Staff | ₹40,000-1,00,000/month | ₹16,999/month (Business plan) |
| Consult 1 question | ₹1,000-3,000 | ~₹30 |
| 500 employment contracts batch | ₹10 lakh+ (lawyer) | ₹1,999 |

---

## 10. Development Roadmap (Updated)

### Phase 1: Foundation (Week 1-4)
```
├── Supabase setup + full schema migration
├── FastAPI scaffold + auth + rate limiting
├── Law data pipeline (India Code / Gazette of India → pgvector)
├── RAG engine (hybrid search + reranker)
├── Legal Q&A agent (CONSULT module)
└── Basic API endpoints
```

### Phase 2: Document Engine (Week 5-8)
```
├── Template schema system
├── Document generation pipeline
├── 10 core templates (employment contract, appointment letter, standing orders...)
├── DOCX/PDF export (python-docx, weasyprint)
├── Contract review agent (REVIEW module)
├── DRAFT module API endpoints
└── Pilot customer beta test
```

### Phase 3: Batch + Management (Week 9-12)
```
├── Batch processing engine (Celery workers)
├── Excel import → batch document generation
├── Document management (upload, search, track)
├── Contract lifecycle tracking
├── Compliance engine (basic checklist)
├── Usage tracking + billing
└── Web dashboard (Next.js)
```

### Phase 4: Scale + Launch (Week 13-16)
```
├── Embeddable chat widget
├── Webhook events
├── Complete template library (50+ templates)
├── Advanced compliance (deadline calendar)
├── Mobile-responsive dashboard
├── Landing page + pricing page
├── Public launch
└── First paying customers
```
