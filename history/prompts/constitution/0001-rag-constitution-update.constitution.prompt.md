---
id: 0001
title: rag-constitution-update
stage: constitution
date: 2025-12-15
surface: cli
model: gpt-5-codex
feature: none
branch: 001-add-docs-chatbot
user: desktop-8bl3mig\pmyls
command: .specify/scripts/bash/create-phr.sh --title "rag-constitution-update" --stage constitution --json
labels: []
links:
  spec: n/a
  ticket: n/a
  adr: n/a
  pr: n/a
files:
  - path: .specify/memory/constitution.md
    summary: Replaced humanoid robotics constitution with RAG Docusaurus governance, updated principles, and version bumped to 2.0.0 with new dates.
  - path: .specify/templates/plan-template.md
    summary: Updated Constitution Check to match new RAG/Docusaurus principles and stack requirements.
tests:
  - status: not run
    detail: Not run (not requested)
---

## Prompt

update constitution

You **MUST** consider the user input before proceeding (if not empty).

## Outline

You are updating the project constitution at `.specify/memory/constitution.md`. This file is a TEMPLATE containing placeholder tokens in square brackets (e.g. `[PROJECT_NAME]`, `[PRINCIPLE_1_NAME]`). Your job is to (a) collect/derive concrete values, (b) fill the template precisely, and (c) propagate any amendments across dependent artifacts.

Follow this execution flow:

1. Load the existing constitution template at `.specify/memory/constitution.md`.
   - Identify every placeholder token of the form `[ALL_CAPS_IDENTIFIER]`.
   **IMPORTANT**: The user might require less or more principles than the ones used in the template. If a number is specified, respect that - follow the general template. You will update the doc accordingly.

2. Collect/derive values for placeholders:
   - If user input (conversation) supplies a value, use it.
   - Otherwise infer from existing repo context (README, docs, prior constitution versions if embedded).
   - For governance dates: `RATIFICATION_DATE` is the original adoption date (if unknown ask or mark TODO), `LAST_AMENDED_DATE` is today if changes are made, otherwise keep previous.
   - `CONSTITUTION_VERSION` must increment according to semantic versioning rules:
     - MAJOR: Backward incompatible governance/principle removals or redefinitions.
     - MINOR: New principle/section added or materially expanded guidance.
     - PATCH: Clarifications, wording, typo fixes, non-semantic refinements.
   - If version bump type ambiguous, propose reasoning before finalizing.

3. Draft the updated constitution content:
   - Replace every placeholder with concrete text (no bracketed tokens left except intentionally retained template slots that the project has chosen not to define yet—explicitly justify any left).
   - Preserve heading hierarchy and comments can be removed once replaced unless they still add clarifying guidance.
   - Ensure each Principle section: succinct name line, paragraph (or bullet list) capturing non‑negotiable rules, explicit rationale if not obvious.
   - Ensure Governance section lists amendment procedure, versioning policy, and compliance review expectations.

4. Consistency propagation checklist (convert prior checklist into active validations):
   - Read `.specify/templates/plan-template.md` and ensure any "Constitution Check" or rules align with updated principles.
   - Read `.specify/templates/spec-template.md` for scope/requirements alignment—update if constitution adds/removes mandatory sections or constraints.
   - Read `.specify/templates/tasks-template.md` and ensure task categorization reflects new or removed principle-driven task types (e.g., observability, versioning, testing discipline).
   - Read each command file in `.specify/templates/commands/*.md` (including this one) to verify no outdated references (agent-specific names like CLAUDE only) remain when generic guidance is required.
   - Read any runtime guidance docs (e.g., `README.md`, `docs/quickstart.md`, or agent-specific guidance files if present). Update references to principles changed.

5. Produce a Sync Impact Report (prepend as an HTML comment at top of the constitution file after update):
   - Version change: old → new
   - List of modified principles (old title → new title if renamed)
   - Added sections
   - Removed sections
   - Templates requiring updates (✅ updated / ⚠ pending) with file paths
   - Follow-up TODOs if any placeholders intentionally deferred.

6. Validation before final output:
   - No remaining unexplained bracket tokens.
   - Version line matches report.
   - Dates ISO format YYYY-MM-DD.
   - Principles are declarative, testable, and free of vague language ("should" → replace with MUST/SHOULD rationale where appropriate).

7. Write the completed constitution back to `.specify/memory/constitution.md` (overwrite).

8. Output a final summary to the user with:
   - New version and bump rationale.
   - Any files flagged for manual follow-up.
   - Suggested commit message (e.g., `docs: amend constitution to vX.Y.Z (principle additions + governance update)`).

Formatting & Style Requirements:

- Use Markdown headings exactly as in the template (do not demote/promote levels).
- Wrap long rationale lines to keep readability (<100 chars ideally) but do not hard enforce with awkward breaks.
- Keep a single blank line between sections.
- Avoid trailing whitespace.

If the user supplies partial updates (e.g., only one principle revision), still perform validation and version decision steps.

If critical info missing (e.g., ratification date truly unknown), insert `TODO(<FIELD_NAME>): explanation` and include in the Sync Impact Report under deferred items.

Do not create a new template; always operate on the existing `.specify/memory/constitution.md` file.

---

As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

1) Determine Stage
   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

2) Generate Title and Determine Routing:
   - Generate Title: 3–7 words (slug for filename)
   - Route is automatically determined by stage:
     - `constitution` → `history/prompts/constitution/`
     - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
     - `general` → `history/prompts/general/`

3) Create and Fill PHR (Shell first; fallback agent‑native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.

Project: Docusaurus Book + Embedded RAG Chatbot (FastAPI + Qdrant + Neon + Auth/Personalize/Urdu)
## Global Principles
- No hallucinations: if not in allowed context, say not found and ask a clarifying question.
- Strict modes are absolute (RAG vs Selected Text).
- Every answer must include sources.
- Mobile-first, readable, and accessible UI.
- Secure by default: no secrets in frontend, minimal user data.

## Non-Negotiable Stack
- Book: Docusaurus  GitHub Pages
- Backend: FastAPI
- Vector DB: Qdrant Cloud (Free Tier)
- DB: Neon Serverless Postgres
- Auth (bonus): better-auth

## Must-Pass Quality Rules
- Deployed book is live on GitHub Pages.
- README includes: setup, env vars, indexing, deploy, troubleshooting.
- Responsive UI + clear loading/error states.
- No committed secrets.

## RAG + Selected-Text Rules
- Always show Sources with chapter/heading/anchor + chunk_id(s) (or selected spans).
- RAG mode: answer using ONLY retrieved book chunks (from Qdrant).
- Selected-Text mode: answer using ONLY user-selected text; NO retrieval; if missing say Not in selected text.

## Indexing Rules
- Book markdown is the only knowledge source.
- Chunk by headings; store stable metadata: route, heading, anchor, chunk_id.
- Provide one documented command/script to rebuild and upsert embeddings to Qdrant.

## Bonus Features (if implemented)
- better-auth signup/signin; collect software + hardware background at signup (minimal fields) and store in Neon.
- Logged-in users can:
  - Personalize chapter via button (revert to original).
  - Translate chapter to Urdu via button (toggle back; keep code blocks unchanged).

## UI Rules
- Clean docs-first theme, light + dark mode.
- Fonts: Inter (body), JetBrains Mono (code); 16px base, ~1.6 line-height.
- Chat: floating button  drawer (desktop) / bottom sheet (mobile) with mode toggle + selected-text preview + sources.

## Response snapshot

Updated the constitution to v2.0.0 with RAG/Docusaurus principles (grounded answers, mode discipline, book-only knowledge, indexing metadata, UX/chat, stack, security, quality, personalization) and aligned the plan template Constitution Check; dates refreshed to 2025-12-15.

## Outcome

- ƒo. Impact: Constitution and plan template now reflect RAG/Docusaurus governance and stack.
- dY¦ Tests: Not run (not requested).
- dY"? Files: Constitution updated; plan template gate updated to new principles.
- dY"? Next prompts: None.
- dYÿ Reflection: Need to keep spec/tasks templates in mind on next edit though no principle references today.

## Evaluation notes (flywheel)

- Failure modes observed: None.
- Graders run and results (PASS/FAIL): Not run.
- Prompt variant (if applicable): n/a
- Next experiment (smallest change to try): n/a
