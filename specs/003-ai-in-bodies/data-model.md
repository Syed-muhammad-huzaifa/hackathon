# Data Model: AI Inside Bodies

This document outlines the conceptual entities for the textbook section "AI Inside Bodies," not a software data model.

## Conceptual Entities

### Sensor
-   **Description**: A device that enables a Physical AI to perceive its environment by converting a physical property (e.g., light, distance, acceleration) into a digital signal.
-   **Key Characteristics**:
    -   Provides input data to the AI's decision-making logic.
    -   Types: Camera (vision), LiDAR (depth/distance), IMU (orientation/acceleration).
-   **Relationship**: The "eyes and ears" of the Physical AI.

### Actuator (Motor)
-   **Description**: A component, typically a motor, that converts electrical energy into physical motion, allowing a robot to act upon its environment.
-   **Key Characteristics**:
    -   Executes the AI's decisions.
    -   Examples: Electric motors in joints, wheels, and grippers.
-   **Relationship**: The "muscles" of the Physical AI.

### Physics Engine (Conceptual)
-   **Description**: The set of physical laws (gravity, friction, momentum, etc.) that govern all interactions between the robot and the real world.
-   **Key Characteristics**:
    -   It is not a piece of software, but the real-world constraints the software must respect.
    -   It is constant and unforgiving.
-   **Relationship**: The "rules of the game" that Physical AI must play by.
