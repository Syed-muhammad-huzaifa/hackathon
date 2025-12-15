<!--
---
Sync Impact Report
---
Version change: 1.0.0 -> 2.0.0
Modified principles:
- I. Physical AI in the Real World -> I. Grounded Answers & Sources
- II. Humanoid Robotics Fundamentals -> II. Mode Discipline (RAG vs Selected Text)
- III. ROS 2 Ecosystem -> III. Book-Only Knowledge Base
- IV. URDF for Humanoids -> IV. Indexing & Metadata Integrity
- V. Digital Twin Simulation -> V. Frontend UX & Chat Surface
- VI. Advanced Sensor Integration -> VI. Non-Negotiable Stack & Deployment
Added sections:
- VII. Security & Secrets Hygiene
- VIII. Quality, Operability & README
- IX. Personalization & Urdu (Bonus Features)
- X. Compliance & Change Management
Removed sections:
- VII. NVIDIA Isaac Sim Integration
- VIII. Autonomous Navigation
- IX. Vision-Language-Action Systems
- X. Voice Command Interface
- XI. Natural-Language Cognitive Planning
- XII. Autonomous Humanoid Capstone
Templates requiring updates:
- ✅ .specify/templates/plan-template.md
- ✅ .specify/templates/spec-template.md (reviewed: no principle references to update)
- ✅ .specify/templates/tasks-template.md (reviewed: sample text only; no principle references)
Follow-up TODOs: None
-->
# Docusaurus Book + RAG Chatbot Constitution

## Core Principles

### I. Grounded Answers & Sources
All responses MUST be grounded strictly in allowed context. If the answer is not found, state that explicitly and ask a clarifying question. Every answer MUST include sources with chapter/heading/anchor and chunk_id(s) (or selected spans).

### II. Mode Discipline (RAG vs Selected Text)
Strict modes are absolute. In RAG mode, respond only with retrieved book chunks from Qdrant. In Selected-Text mode, respond only with the provided selection; if absent, reply “Not in selected text” and request the needed text. No external knowledge is allowed.

### III. Book-Only Knowledge Base
The Docusaurus book markdown is the sole knowledge source. Content updates MUST flow into the retrieval index; no shadow knowledge bases or ad-hoc notes are permitted.

### IV. Indexing & Metadata Integrity
Chunk by headings and store stable metadata: route, heading, anchor, and chunk_id. Provide and maintain a documented command or script to rebuild and upsert embeddings to Qdrant. Retrieval responses MUST surface chunk identifiers.

### V. Frontend UX & Chat Surface
The docs experience is mobile-first, readable, and accessible: Inter for body, JetBrains Mono for code, 16px base, ~1.6 line-height, with light and dark modes. The chat is a floating button and drawer on desktop and a bottom sheet on mobile, with mode toggle, selected-text preview, sources, and clear loading and error states.

### VI. Non-Negotiable Stack & Deployment
Book: Docusaurus deployed to GitHub Pages. Backend: FastAPI. Vector DB: Qdrant Cloud (Free Tier). Database: Neon Serverless Postgres. Auth (if present): better-auth. Stack substitutions require a formal amendment.

### VII. Security & Secrets Hygiene
Secure by default: no secrets in the frontend or static assets; collect only minimal user data. Environment variables and credentials stay server-side. Never commit secrets.

### VIII. Quality, Operability & README
The deployed book MUST remain live on GitHub Pages. The README MUST cover setup, env vars, indexing, deploy, and troubleshooting. UI must be responsive with explicit loading and error states. No committed secrets—CI/CD gates should enforce this.

### IX. Personalization & Urdu (Bonus Features)
If authentication is enabled, collect minimal software and hardware background at signup and store in Neon. Logged-in users may personalize chapters (with a revert path) and translate chapters to Urdu via a toggle that preserves code blocks unchanged.

### X. Compliance & Change Management
All code, specs, tasks, and docs MUST align with this Constitution. Any deviation requires written justification, review, and a migration plan before merging.

## Governance
This Constitution is the single source of truth for all technical decisions within the project. It supersedes all other practices, conventions, or individual preferences. All project artifacts, including code, specifications, and documentation, MUST comply with these principles.

Amendments to this Constitution require a formal proposal, review, and a documented migration plan for existing systems. All pull requests and design reviews must explicitly verify compliance with these principles. Complexity or deviation from a principle must be rigorously justified and approved. Version bumps follow semantic versioning: MAJOR for incompatible principle changes, MINOR for new principles or materially expanded guidance, PATCH for clarifications.

**Version**: 2.0.0 | **Ratified**: 2025-11-29 | **Last Amended**: 2025-12-15
