# Data Model: Floating Docs Chatbot with RAG

## Entities

### Message
- id (uuid)
- role (enum: user/assistant/system)
- content (text)
- citations (json array of doc refs)
- created_at (timestamp)
- token_count (int, optional)

### ContextChunk
- id (uuid)
- message_id (fk Message, optional)
- source_type (enum: selection/current_page/global_docs)
- source_ref (string: doc path/url)
- embedding_vector_id (string, Qdrant point id)
- relevance_score (float)
- created_at (timestamp)

## Relationships
- Message 0..n ContextChunk (citations per answer)

## Validation Rules
- role restricted to user/assistant/system.
- citations reference known doc paths or anchors.
- limit message payload size to prevent overly long inputs.
