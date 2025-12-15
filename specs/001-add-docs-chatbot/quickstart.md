# Quickstart: Floating Docs Chatbot with RAG

## Prerequisites
- Node 18+ for Docusaurus widget build.
- Python 3.11+ with uv/pip for FastAPI backend.
- Qdrant Cloud URL/API key.
- (Optional) any Qdrant/FastEmbed keys as needed.
- Gemini credentials (Agents SDK) and Context7 MCP access.

## Setup
1) Backend (FastAPI)  
   - `pip install -r backend/requirements.txt`  
   - Set env: `QDRANT_URL`, `QDRANT_API_KEY`, `NEON_DATABASE_URL`, `GEMINI_API_KEY`, optionally `CHAT_ALLOW_ORIGINS`, `RATE_LIMIT_PER_MINUTE`, `AGENTS_MODEL` (default `gemini-2.5-flash`).  
   - Run: `uvicorn backend.app.main:app --reload`  
   - Ingestion: `python -m backend.ingestion.ingest_docs` (loads book-source/docs, upserts to Qdrant)  
   - Health: `GET /healthz`

2) Frontend (Docusaurus widget)  
   - `cd book-source && npm install`  
   - Dev: `npm run start` (bubble mounts on all pages; connects to `DOCS_CHAT_API_ORIGIN`)  
   - Build: `npm run build`

3) Contracts & tests  
   - Contracts: `specs/001-add-docs-chatbot/contracts/openapi.yaml`  
   - Contract smoke: `schemathesis run specs/001-add-docs-chatbot/contracts/openapi.yaml --base-url http://localhost:8000`  
   - E2E: `cd book-source && npx playwright test`
   - Eval (manual opt-in): `RUN_EVAL=1 pytest backend/tests/eval/test_eval_queries.py`  

## Notes
- Selected-text flow: send to `/chat/selection` with `selected_text` and `page_url`; backend prioritizes selection/page before global.  
- General questions: `/chat/query`.  
- Accuracy goal: 10 curated prompts ≥80% contextual answers with citations.  
- No UI theme overhaul; keep widget minimal and consistent with Docusaurus.
