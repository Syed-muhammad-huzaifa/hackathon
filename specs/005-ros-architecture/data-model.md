# Data Model: ROS Architecture

This document outlines the conceptual entities for the "ROS Architecture" chapter.

## Conceptual Entities

### Node
-   **Description**: An independent program responsible for a single, well-defined task (e.g., controlling a wheel motor, reading a laser scanner).
-   **Key Characteristics**: The fundamental building block of a ROS system. All nodes together form the computational graph.

### Computational Graph
-   **Description**: The peer-to-peer network of all running ROS 2 nodes. It visualizes the entire robotic system and how data flows between its components.

### Topic (Communication Method)
-   **Description**: A one-way communication channel for continuous data streams. Nodes publish messages to a topic, and any number of nodes can subscribe to receive those messages.
-   **Analogy**: A radio station. The announcer (publisher) broadcasts, and anyone with a radio (subscriber) can listen.
-   **Use Case**: Streaming sensor data, robot state information.

### Service (Communication Method)
-   **Description**: A two-way, request/reply communication method. A client node sends a request, and a service node processes it and returns a single response.
-   **Analogy**: A vending machine. You make a request (press a button), and you get a single response (a snack).
-   **Use Case**: Triggering a specific action, requesting a calculation (e.g., "calculate the distance to this wall").

### Action (Communication Method)
-   **Description**: A two-way communication method for long-running tasks that provides continuous feedback. It can be cancelled.
-   **Analogy**: Ordering a pizza for delivery. You get an initial confirmation, you can track its progress, and you can cancel the order before it arrives.
-   **Use Case**: Navigation goals (e.g., "go to the kitchen"), complex manipulations.
