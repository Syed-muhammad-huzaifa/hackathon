# Tasks: Floating Docs Chatbot with RAG

**Input**: Design documents from `/specs/001-add-docs-chatbot/`  
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/, quickstart.md

**Tests**: Included where high-value (contracts, integration, 10 evaluation queries).

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure (backend + existing `/book-source` frontend)

- [X] T001 Create backend skeleton per plan (backend/app, agents, retrieval, tests, ingestion, docs)
- [X] T002 [P] Add backend dependencies in backend/requirements.txt (FastAPI, httpx, pydantic, FastEmbed, qdrant-client, OpenAI Agents SDK, pytest)
- [X] T003 [P] Add lint/format configs (ruff/black/mypy) in backend/pyproject.toml
- [X] T004 [P] Add env template with Qdrant/Gemini vars in backend/.env.example and backend/README.md
- [X] T005 [P] Add AGENTS doc entry for stack (FastAPI, Agents SDK+Gemini, Qdrant, FastEmbed, Context7) in AGENTS.md
- [X] T006 [P] Scaffold widget entry in existing Docusaurus (`book-source/src/chat/index.tsx`) and add placeholder bundle hook in `book-source/docusaurus.config.ts`
- [X] T007 [P] Add ESLint/Prettier config for widget code in `book-source/.eslintrc.js`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

- [ ] T008 Removed: DB schema/migrations deferred (stateless backend)
- [ ] T009 Removed: DB connection/session management deferred
- [ ] T010 Removed: Auth dependency omitted for this phase
- [X] T011 [P] Implement Qdrant + FastEmbed helper and collection bootstrap in backend/retrieval/qdrant_client.py
- [X] T012 [P] Create ingestion pipeline to chunk book markdown (Context7-guided chunking) and upsert vectors in backend/ingestion/ingest_docs.py
- [X] T013 [P] Define Agents SDK pipeline skeleton (Gemini) and document required Context7 MCP lookup before implementation in backend/agents/pipeline.py and backend/docs/context7-usage.md
- [X] T014 [P] Scaffold chat routers (/chat/query, /chat/selection) in backend/app/routers/chat.py
- [X] T015 [P] Add middleware for logging/error and CORS in backend/app/middleware.py
- [X] T016 [P] Create frontend API client for chat endpoints in `book-source/src/chat/apiClient.ts`
- [X] T017 [P] Build widget shell components (bubble + modal) in `book-source/src/chat/ChatBubble.tsx` and `book-source/src/chat/ChatModal.tsx`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Ask Any Docs Question (Priority: P1) MVP

**Goal**: General docs/book Q&A via floating widget with grounded answers and citations.

**Independent Test**: From any docs page, ask “How do I get started?”; receive a cited answer from book content within target latency and a graceful fallback when unknown.

### Implementation for User Story 1

- [X] T018 [US1] Implement /chat/query endpoint returning citations in backend/app/routers/chat.py
- [X] T019 [P] [US1] Implement retrieval flow (page/global) in backend/retrieval/retriever.py
- [X] T020 [P] [US1] Implement Agents SDK call to Gemini with citation/fallback shaping after Context7 MCP doc check in backend/agents/pipeline.py
- [X] T021 [P] [US1] Return agent response without server-side persistence (stateless)
- [X] T022 [P] [US1] Build chat panel UI for general questions with loading/error/citations in `book-source/src/chat/components/ChatPanel.tsx`
- [ ] T023 Removed: No browser-session cache needed (stateless)
- [X] T024 [US1] Add integration/contract test for /chat/query success/fallback in backend/tests/integration/test_chat_query.py

**Checkpoint**: User Story 1 independently functional and testable

---

## Phase 4: User Story 2 - Selected-Text Context Answers (Priority: P1)

**Goal**: Selected-text and page-aware answers that prioritize the selection/page before global context.

**Independent Test**: Select a snippet, ask “What does this do?”, and see an answer citing the selection/page first; fallback disclosed if selection insufficient.

### Implementation for User Story 2

- [X] T025 [P] [US2] Capture selected text events and payload in `book-source/src/chat/services/selection.ts`
- [X] T026 [US2] Implement /chat/selection handler honoring selection + page_url in backend/app/routers/chat.py
- [X] T027 [P] [US2] Update retriever to selection-first with fallback to page/global in backend/retrieval/retriever.py
- [X] T028 [P] [US2] Adjust agent prompt to enforce selection-first grounding and disclosure in backend/agents/prompts.py
- [X] T029 [P] [US2] Show selection/context badge in responses in `book-source/src/chat/components/ContextBadge.tsx`
- [X] T030 [US2] Add integration test for /chat/selection success/fallback in backend/tests/integration/test_chat_selection.py

**Checkpoint**: User Story 2 independently functional and testable

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T036 [P] Harden CSP/origin allowances for widget bundle in `book-source/docusaurus.config.ts`
- [X] T037 [P] Performance tuning for <3s responses: batching embeddings, timeouts, streaming flags in backend/agents/pipeline.py
- [X] T038 Security/observability: sanitize inputs, rate limit chat endpoints, redact logs in backend/app/middleware.py
- [X] T039 [P] Contract validation against openapi.yaml (schemathesis) in backend/tests/contract/test_openapi.py
- [X] T040 [P] Update quickstart.md with setup/test deltas in specs/001-add-docs-chatbot/quickstart.md
- [X] T041 [P] Run 10-eval-query harness and log accuracy/citation results in backend/tests/eval/test_eval_queries.py
- [X] T042 [P] Verify Context7 MCP doc pulls match final Agents SDK usage and record in backend/docs/context7-usage.md

---

## Dependencies & Execution Order

- Phase 1 → Phase 2 → User Stories (Phases 3–4) → Phase 6.
- US1 and US2 are both P1; US2 depends on retriever/agent updates from US1 (T019–T020).

### Parallel Opportunities

- Setup: T002–T007 in parallel after T001.
- Foundational: T010–T017 largely parallel; T013 gated by Context7 doc check.
- US1: T019–T023 in parallel after T018; T024 after implementation.
- US2: T025, T027–T029 parallel; T026 after router skeleton; T030 after implementation.
- Polish: Most marked [P] can run independently.

### Implementation Strategy

- MVP: Phases 1–3 to deliver general Q&A with citations (US1).
- Incremental: Add selection-aware flow (US2), then polish/tests/perf.

### Format Validation

All tasks use checklist format `- [ ] T### [P?] [Story?] Description with file path`.
