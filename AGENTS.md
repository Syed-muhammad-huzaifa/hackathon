# hackathon Development Guidelines

Auto-generated from all feature plans. Last updated: 2025-12-06

## Active Technologies

- TypeScript/React (book-source Docusaurus) + Python 3.11 (FastAPI); FastAPI, OpenAI Agents SDK (Gemini), FastEmbed, Qdrant, Neon Postgres, Context7 MCP (for SDK docs), Docusaurus/React (001-add-docs-chatbot)

## Project Structure

```text
src/
tests/
```

## Commands

cd backend && pytest && ruff check .  
cd book-source && npm test (or npx playwright test) && npm run lint

## Code Style

TypeScript/React (Docusaurus) + Python 3.11 (FastAPI): Follow standard conventions

## Recent Changes

- 001-add-docs-chatbot: Added FastAPI + Agents SDK (Gemini) + FastEmbed/Qdrant + Neon + Context7 MCP + book-source Docusaurus widget

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
