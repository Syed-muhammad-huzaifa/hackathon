---
id: 0008
title: agent-integration
stage: tasks
date: 2025-12-06
surface: codex-cli
model: gpt-5
feature: 001-add-docs-chatbot
branch: 001-add-docs-chatbot
user: PMLS
command: Integrate Agents SDK scaffold with Context7 MCP requirement
labels: []
links:
  spec: specs/001-add-docs-chatbot/spec.md
  ticket: ""
  adr: ""
  pr: ""
files:
  - specs/001-add-docs-chatbot/tasks.md
  - backend/agents/pipeline.py
  - backend/agents/prompts.py
  - backend/retrieval/retriever.py
  - backend/app/routers/chat.py
tests:
  - Not run
---

## Prompt

yes do

## Response snapshot

- Implemented Agents SDK-based pipeline scaffold with function_tool fetch_context, system prompt, Gemini model setting, and Runner.run call (async). Selection-first retrieval; citations gathered from tool outputs. Chat routes now await the agent. Model default set to gemini-1.5-pro; Context7 MCP requirement noted in docs.

## Outcome

- Impact: Agent layer now uses Agents SDK pattern with retrieval tool; ready to swap in real Gemini credentials. Tasks updated (T020 completed).  
- Tests: Not run.  
- Files: pipeline, prompts, retriever, chat routes updated.  
- Next prompts: Finish polish/tests (CSP, perf, schemathesis/Playwright), 10-query eval harness, duplicate spec cleanup if desired.
- Reflection: Agents call depends on proper model/provider; ensure Context7 MCP consulted before further changes.

## Evaluation notes (flywheel)

- Failure modes observed: None (agent call still requires API key/model config).
- Graders run and results (PASS/FAIL): Not run.
- Prompt variant (if applicable): n/a
- Next experiment (smallest change to try): Wire real Gemini credentials and run end-to-end tests.
