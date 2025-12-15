# Implementation Plan: Floating Docs Chatbot with RAG

**Branch**: `001-add-docs-chatbot` | **Date**: 2025-12-06 | **Spec**: specs/001-add-docs-chatbot/spec.md  
**Input**: Feature specification from `specs/001-add-docs-chatbot/spec.md`

## Summary

Deliver a floating chat bubble across the existing Docusaurus docs (in `/book-source`) that answers general and selected-text questions using a RAG pipeline: FastAPI backend, OpenAI Agent SDK orchestrator with Gemini as the LLM (no OpenAI LLM), Qdrant with FastEmbed vectors, Context7 MCP for up-to-date docs context and chunking. Must surface citations, prioritize selected-text context, and achieve ≥80% accuracy on 10 test prompts. Agent implementation MUST consult Context7 MCP for the latest Agents SDK patterns before coding to avoid incorrect/hallucinated usage. Server-side chat persistence (including metadata and session history) is deferred for now.

## Technical Context

**Language/Version**: TypeScript/React (existing Docusaurus in `/book-source`) + Python 3.11 (FastAPI)  
**Primary Dependencies**: FastAPI, OpenAI Agents SDK (Gemini), FastEmbed, Qdrant, Context7 MCP, Docusaurus/React  
**Storage**: Qdrant (vectors); server-side chat persistence deferred (stateless responses; client cache optional)  
**Testing**: Backend: pytest + httpx; Contract: schemathesis; Frontend: Playwright + React Testing Library  
**Target Platform**: Web (Docusaurus) + cloud-hosted FastAPI service  
**Project Type**: Web (frontend + backend)  
**Performance Goals**: Answers typically <3s; ≥80% accuracy on 10 curated prompts; bubble load impact <200ms; p95 retrieval <500ms at target scale  
**Constraints**: Gemini only (no OpenAI LLM), no UI theme overhaul, no multi-tenant architecture, citations required, selected-text prioritized, Context7 MCP used for docs context/chunking and MUST be consulted before implementing Agents SDK calls (no hallucinated agent wiring)  
**Scale/Scope**: Moderate traffic (docs assistant), stateless backend responses; any continuity handled client-side only if needed

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Physical AI in the Real World**: Not applicable (web chatbot); request exemption.  
- **II. Humanoid Robotics Fundamentals**: Not applicable; request exemption.  
- **III. ROS 2 Ecosystem**: Not applicable; request exemption.  
- **IV. URDF for Humanoids**: Not applicable; request exemption.  
- **V. Digital Twin Simulation**: Not applicable; request exemption.  
- **VI. Advanced Sensor Integration**: Not applicable; request exemption.  
- **VII. NVIDIA Isaac Sim Integration**: Not applicable; request exemption.  
- **VIII. Autonomous Navigation**: Not applicable; request exemption.  
- **IX. Vision-Language-Action Systems**: Not applicable; request exemption.  
- **X. Voice Command Interface**: Not applicable; request exemption.  
- **XI. Natural-Language Cognitive Planning**: Not applicable; request exemption.  
- **XII. Autonomous Humanoid Capstone**: Not applicable; request exemption.

## Project Structure

### Documentation (this feature)

```text
specs/001-add-docs-chatbot/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
└── contracts/
```

### Source Code (repository root)

```text
backend/
|-- app/             # FastAPI entrypoints, routers, middleware
|-- agents/          # Agent SDK orchestration (Gemini) and tools
|-- retrieval/       # FastEmbed + Qdrant retriever, chunking
|-- tests/           # pytest + httpx + schemathesis

book-source/ (existing Docusaurus)
|-- src/             # Integrate widget components/services here
|-- static/          # Widget bundle if needed
`-- docusaurus.config.js # Inject/enable floating widget
```

**Structure Decision**: Web split (frontend widget + backend service) with contracts under specs/001-add-docs-chatbot/contracts.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|--------------------------------------|
| Constitution robotics requirements waived | Feature is a docs chatbot, not robotics | Robotics/ROS/URDF add no value here |
