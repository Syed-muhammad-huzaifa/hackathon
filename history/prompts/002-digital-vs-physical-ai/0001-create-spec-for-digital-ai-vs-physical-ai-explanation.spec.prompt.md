---
id: 0001
title: Create spec for Digital AI vs Physical AI explanation
stage: spec
date: 2025-11-29
surface: agent
model: gemini-1.5-flash-latest
feature: 002-digital-vs-physical-ai
branch: 002-digital-vs-physical-ai
user: PMLS
command: /sp.specify "Write a structured, beginner-friendly textbook explanation for Section 2: “Digital AI vs Physical AI” in Chapter 1: Introduction to Physical AI, including clear headings, subheadings, short paragraphs, bullet points, and real-world examples. Explain digital AI (software like chatbots, apps, recommendation systems) and Physical AI (robots with bodies, sensors, motors). Compare them using bullet points, explain how digital AI works in virtual space while Physical AI must deal with gravity, movement, obstacles, and real-world safety. Add simple analogies, comparisons, and small examples like ChatGPT vs a warehouse robot or a self-driving car. The content should be accurate, easy to follow, and aligned with the course outline."
labels: ["specification", "digital-ai", "physical-ai", "robotics"]
links:
  spec: specs/002-digital-vs-physical-ai/spec.md
  ticket: null
  adr: null
  pr: null
files:
- specs/002-digital-vs-physical-ai/spec.md
- specs/002-digital-vs-physical-ai/checklists/requirements.md
tests:
- Spec quality checklist validation
---

## Prompt

Write a structured, beginner-friendly textbook explanation for Section 2: “Digital AI vs Physical AI” in Chapter 1: Introduction to Physical AI, including clear headings, subheadings, short paragraphs, bullet points, and real-world examples. Explain digital AI (software like chatbots, apps, recommendation systems) and Physical AI (robots with bodies, sensors, motors). Compare them using bullet points, explain how digital AI works in virtual space while Physical AI must deal with gravity, movement, obstacles, and real-world safety. Add simple analogies, comparisons, and small examples like ChatGPT vs a warehouse robot or a self-driving car. The content should be accurate, easy to follow, and aligned with the course outline.

## Response snapshot

The feature specification for "Digital AI vs Physical AI" has been successfully created.
- A new branch '002-digital-vs-physical-ai' was created.
- The specification document 'specs/002-digital-vs-physical-ai/spec.md' was generated.
- A quality checklist 'specs/002-digital-vs-physical-ai/checklists/requirements.md' was created and validated. All checks passed.
The feature is now ready for the planning phase.

## Outcome

- ✅ Impact: The spec for the feature was successfully created and validated, enabling further development.
- 🧪 Tests: Spec quality checklist validated; all items passed.
- 📁 Files: Created `spec.md` and `requirements.md` for feature `002-digital-vs-physical-ai`.
- 🔁 Next prompts: The user can now proceed with `/sp.plan` or `/sp.clarify` if there were any clarification points.
- 🧠 Reflection: The numbering scheme for feature branches was adjusted to '002' to avoid conflicts with existing '001' prefixed features, which was a concern identified in previous turns.

## Evaluation notes (flywheel)

- Failure modes observed: N/A
- Graders run and results (PASS/FAIL): All spec quality checklist items passed.
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A