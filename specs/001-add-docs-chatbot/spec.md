# Feature Specification: Floating Docs Chatbot with RAG

**Feature Branch**: `001-add-docs-chatbot`  
**Created**: 2025-12-06  
**Status**: Draft  
**Input**: User description: "Add a floating AI chatbot inside the existing Docusaurus documentation that answers user questions using book content through a RAG pipeline.

Core Feature:
FastAPI backend  OpenAI Agent SDK orchestrator  Gemini model for response  Qdrant (FastEmbed vectors) for retrieval  Context7MCP for accessing latest documentation context & unified chunking  Chatbot supports direct questions + selected-text contextual answers. Server-side chat persistence is deferred; interactions are stateless apart from page/selection context.

Success Criteria:
Chatbot bubble visible across all pages, opens chat panel.
Answers must be grounded in book context with citations.
Selected-text queries prioritize selected content retrieval.
Qdrant retrieval with FastEmbed + Context7MCP enabled.
10 test prompts with 80% accurate/contextual responses.

Constraints:
Backend via FastAPI.
Gemini is answering LLM (no OpenAI LLM).
Vector DB: Qdrant; server-side chat storage deferred (stateless responses).
No UI theme overhaul or multi-tenant architecture."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Ask Any Docs Question (Priority: P1)

Visitors open the floating bubble and ask general documentation/book questions, receiving grounded answers with citations.

**Why this priority**: Core value; enables self-service answers across the docs.

**Independent Test**: From any docs page, ask “How do I get started?” and receive a cited answer from the book docs within target latency.

**Acceptance Scenarios**:

1. **Given** the bubble is visible on any page, **When** a visitor opens it and asks a general question, **Then** the chatbot returns a concise, cited answer drawn from book content.  
2. **Given** the chatbot cannot find a clear answer, **When** it responds, **Then** it provides a polite fallback and suggests related links or search.

---

### User Story 2 - Selected-Text Context Answers (Priority: P1)

Visitors select text on a page and request an explanation; answers prioritize the selected text and page context.

**Why this priority**: Improves relevance and trust for page-specific questions.

**Independent Test**: Select a configuration snippet, ask “What does this do?”, and see an answer citing the selected section first.

**Acceptance Scenarios**:

1. **Given** text is selected on the page, **When** the visitor triggers a question, **Then** the chatbot scopes retrieval to that selection and cites it in the response.  
2. **Given** the selection is too small or missing, **When** the visitor asks, **Then** the chatbot falls back to page/global context and discloses the fallback.

---

### Edge Cases

- Widget blocked or fails to load; provide fallback link to search/help.  
- Very long or multi-part questions; prompt to shorten or split.  
- Content not in corpus; disclose limitation and suggest alternatives.  
- Backend or retrieval timeout; preserve typed question and offer retry.  
- Selected text missing or empty; handle gracefully with page/global fallback.

### Assumptions

- Book/docs content is available for embedding; Context7MCP provides latest context and chunking guidance.  
- Gemini is the answering LLM; no OpenAI completion models are used.  
- Server-side chat persistence is out of scope; interactions are stateless aside from page context.  
- UI uses existing Docusaurus theme with minimal changes (no overhaul).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: A floating chat bubble is visible on all docs pages and opens a chat panel on click.  
- **FR-002**: Users can send general questions and receive grounded, cited answers from book/docs content.  
- **FR-003**: Selected-text questions prioritize the selected content and page context before broader corpus.  
- **FR-004**: Responses must include citations or references to relevant doc sections when available.  
- **FR-005**: Retrieval must use Qdrant with FastEmbed vectors and Context7MCP guidance for chunking/context refresh.  
- **FR-006**: Graceful fallbacks for unknown answers, missing selection, and backend timeouts, without losing user input.  
- **FR-007**: Latency targets: 10 test prompts achieve at least 80% accurate/contextual responses; typical answer under 3 seconds where feasible.  
- **FR-008**: No UI theme overhaul or multi-tenant behavior; widget adapts to existing Docusaurus styling.

### Key Entities *(include if feature involves data)*

- **Context Chunk**: Embedded doc segments (selection/page/global) with source refs and scores.  
- **User Profile**: Not captured in this phase; no auth or personalization.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Chat bubble visible on 100% of docs pages and opens reliably.  
- **SC-002**: 90% of answers include at least one citation to relevant doc sections.  
- **SC-003**: 80% of selected-text queries return answers that reference the selection/page before global context.  
- **SC-004**: 10 curated test prompts achieve ≥80% accurate/contextual responses.  
