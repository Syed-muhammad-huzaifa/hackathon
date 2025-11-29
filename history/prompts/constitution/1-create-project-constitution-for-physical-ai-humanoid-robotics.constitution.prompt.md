---
id: 1
title: Create Project Constitution for Physical AI & Humanoid Robotics
stage: constitution
date: 2025-11-29
surface: agent
model: Gemini
feature: none
branch: main
user: PMLS
command: /sp.constitution
labels: [constitution, robotics]

links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
 - .specify/templates/plan-template.md
tests:
 - "none"
---

## Prompt

/sp.constitution Write a full Constitution for a textbook titled “Physical AI & Humanoid Robotics” using Spec-Kit Plus principles. Base the Constitution entirely on the following course outline: Physical AI in the real world, humanoid robotics fundamentals, ROS 2 nodes/topics/services, URDF for humanoids, Gazebo and Unity digital twin simulation, physics simulation and sensors (LiDAR, Depth Cameras, IMUs), NVIDIA Isaac Sim, Isaac ROS VSLAM and Nav2 path planning, Vision-Language-Action systems, Whisper voice commands, natural-language cognitive planning, and the capstone “Autonomous Humanoid” project inc

## Response snapshot

I have drafted a new constitution for the "Physical AI & Humanoid Robotics" textbook, version 1.0.0, based on the course outline you provided. I have also updated the project templates to ensure consistency with the new principles.

## Outcome

- ✅ Impact: Created a new project constitution and updated relevant templates.
- 🧪 Tests: No tests were run.
- 📁 Files: 
  - .specify/memory/constitution.md
  - .specify/templates/plan-template.md
- 🔁 Next prompts: none
- 🧠 Reflection: The `create-phr.sh` script failed silently, which required manual intervention to create the PHR.

## Evaluation notes (flywheel)

- Failure modes observed: The `create-phr.sh` script did not create the necessary directories and failed without any error message.
- Graders run and results (PASS/FAIL): none
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none
