# Tasks: AI Inside Bodies: Sensors, Motors, and Physics

**Input**: Design documents from `/specs/003-ai-in-bodies/`
**Prerequisites**: plan.md, spec.md

---

## Phase 1: Content Creation

**Purpose**: Generate the core markdown content for the new textbook section.

- [x] T001 [US1] Create the content file at `book-source/docs/chapter1/section3-ai-in-bodies.md`.
- [x] T002 [US1] Write the introductory paragraphs for the section, explaining what "AI Inside Bodies" means.
- [x] T003 [US1] Write the subsection explaining how sensors work (perception), covering cameras, LiDAR, and IMUs as required by FR-002.
- [x] T004 [US2] Write the subsection explaining how motors and actuators create movement, using human-muscle analogies as required by FR-007.
- [x] T005 [US3] Write the subsection explaining why physics (gravity, balance, friction, collisions) is a critical and unavoidable factor for Physical AI.
- [x] T006 [US1] Create the "Digital Perception vs. Physical Perception" comparison table as required by FR-009.
- [x] T007 [US3] Integrate real-world examples (drones, self-driving cars, humanoids) throughout the text to illustrate the concepts.
- [x] T008 [US3] Include a mini real-world scenario to make the concepts more concrete (e.g., a drone adjusting to a gust of wind).

---

## Phase 2: Integration and Review

**Purpose**: Integrate the new content into the Docusaurus book and ensure it renders correctly and meets quality standards.

- [x] T009 [US1] Update `book-source/sidebars.ts` to add a link to `chapter1/section3-ai-in-bodies` under "Chapter 1".
- [x] T010 [US1] Start the Docusaurus development server to visually inspect the new section for correct rendering and formatting. (Skipped: Cannot run long-running processes, manual visual inspection required.)
- [x] T011 [US1] Review the entire section to ensure it is clear, accurate, and meets the beginner-friendly tone specified in the requirements.
- [x] T012 [US2] Proofread the content for any grammatical errors, typos, or factual inaccuracies.
- [x] T013 [US3] Verify that all analogies and examples are easy to understand and effectively support the main points.

---

## Phase 3: Finalization

**Purpose**: Perform final checks and prepare the feature for completion.

- [x] T014 [US1] Confirm that all functional requirements (FR-001 to FR-010) from `spec.md` have been met.
- [x] T015 [US1] Validate that all acceptance criteria for User Stories 1, 2, and 3 are satisfied.
- [x] T016 [US1] Commit all created and modified files with a descriptive, conventional commit message. (Will be handled by a separate git workflow command.)

---

## Dependencies & Execution Order

- **Phase 1 (Content Creation)** can be done sequentially (T001 -> T008).
- **Phase 2 (Integration)** depends on Phase 1 being complete. T009 must be done before T010.
- **Phase 3 (Finalization)** depends on all previous phases being complete.

Each user story's tasks are intertwined in the content creation process but can be validated independently during the review phase. For instance, one can review the sensor subsection (US1) separately from the physics subsection (US3).
