# Data Model: Real-World Constraints

This document outlines the conceptual entities for the textbook section "Real-World Constraints."

## Conceptual Entities

### Environmental Constraint
-   **Description**: An unpredictable or difficult condition in the physical world that a robot must navigate.
-   **Key Characteristics**:
    -   External to the robot.
    -   Often requires adaptive behavior.
    -   Examples: Slippery floors, uneven terrain, poor lighting, dynamic obstacles (e.g., people).

### Hardware Limitation
-   **Description**: A physical or operational limit inherent to the robot's own components.
-   **Key Characteristics**:
    -   Internal to the robot system.
    -   Requires monitoring and resource management.
    -   Examples: Finite battery life, motor overheating, limited processing power, sensor noise or delays.

### Safety Rule
-   **Description**: A programmed behavior or physical design feature intended to prevent the robot from causing harm.
-   **Key Characteristics**:
    -   A top-priority constraint that can override other goals.
    -   Can be software-based (e.g., stopping for obstacles) or hardware-based (e.g., emergency stop buttons).
    -   Examples: Collision avoidance, limiting arm speed near humans, defining no-go zones.
