# Research Notes: Floating Docs Chatbot with RAG

## Decisions

- **Decision**: Use Gemini via OpenAI Agents SDK (no OpenAI LLM) for answers.  
  **Rationale**: Requirement to avoid OpenAI LLM; Gemini supported in Agents SDK and works with tool orchestration.  
  **Alternatives considered**: OpenAI GPT (rejected per constraint); local models (latency/ops overhead).

- **Decision**: Retrieval with FastEmbed + Qdrant, using Context7 MCP for latest docs context and chunking guidance.  
  **Rationale**: Meets constraint; Context7 MCP reduces stale context and improves chunking consistency; Qdrant Cloud fits read-heavy workloads.  
  **Alternatives considered**: Pinecone (extra cost), self-host Qdrant (ops overhead), plain keyword search (lower relevance).

- **Decision**: Defer server-side chat persistence; treat interactions as stateless aside from page/selection context.  
  **Rationale**: Scope reduction per updated requirement; avoids auth/db complexity.  
  **Alternatives considered**: Client-side session storage for continuity (not required), Neon persistence for logs/metadata (deferred), Qdrant payload storage (not needed for chat history).

- **Decision**: Frontend as Docusaurus widget; minimal styling, no theme overhaul.  
  **Rationale**: Constraint to avoid theme changes; keeps integration contained.  
  **Alternatives considered**: Full-page chat surface (violates constraint).

- **Decision**: Accuracy gate: 10 curated prompts with ≥80% contextual/grounded responses.  
  **Rationale**: Explicit success criterion; aligns evaluation with book grounding.  
  **Alternatives considered**: Higher target (risk with time), lower target (insufficient quality bar).
