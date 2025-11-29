---
title: 'Chapter 1: ROS Architecture'
---

# Chapter 1: The ROS 2 Architecture

Welcome to Part II of our journey into Physical AI. We're now moving from the "what" and "why" of robotics to the "how." The single most important tool for building modern robots is the Robot Operating System (ROS), specifically ROS 2. Think of it as the central nervous system for a robot. It’s the framework that allows all the different parts—sensors, motors, and decision-making algorithms—to communicate and work together as a single, coherent system.

This chapter introduces the fundamental concepts of the ROS 2 architecture.

## The Computational Graph: A Robot's Digital Nervous System

The core of any ROS 2 system is the **computational graph**. This isn't a physical object, but a network of all the software processes running on the robot. It’s a map that shows how information flows through the robot's "brain."

Imagine a self-driving car. It has separate software processes for reading the camera, detecting obstacles, planning a path, and controlling the wheels. The computational graph is what connects all of these processes, allowing them to share information and coordinate their actions seamlessly. This is the essence of a **distributed system**: instead of one giant, monolithic program, a robot's intelligence is built from many small, independent programs that work together. This makes the system more resilient (if one part crashes, the others can keep running) and easier to develop and debug.

### Nodes: The Brain Cells of ROS

Each of these independent programs in the computational graph is called a **Node**. A node is a single, executable process responsible for one specific task. For example, in our self-driving car:

*   One node for the main camera (`/camera_driver`).
*   One node for the LiDAR sensor (`/lidar_driver`).
*   One node that reads sensor data and detects obstacles (`/obstacle_detector`).
*   One node that plans the car's path (`/path_planner`).
*   One node that sends commands to the wheels (`/motor_controller`).

```
Simple ROS Graph:

[ /camera_driver ] ---- (sends image data) ----> [ /image_processor ]
      (Node 1)                                       (Node 2)
```

## Communication Methods: How Nodes Talk

Nodes would be useless if they couldn't communicate. ROS 2 provides three primary communication methods, each suited for a different type of interaction.

### Topics
**Topics** are one-way communication channels for continuous data streams. A node **publishes** messages to a topic, and any number of other nodes can **subscribe** to that topic to receive the messages.

*   **Analogy**: A radio station. The announcer (publisher) broadcasts a signal, and anyone with a radio tuned to the right frequency (subscribers) can listen. The announcer doesn't know or care who is listening.
*   **Use Case**: A camera node continuously publishing a stream of images, or a wheel sensor node publishing the robot's current speed.

### Services
**Services** are for two-way, request/reply interactions. A client node sends a single request to a service node, which does some work and returns a single response.

*   **Analogy**: A vending machine. You make a request (press a button), and you get one response (a snack). The transaction is synchronous; you wait for the response.
*   **Use Case**: A node requesting a calculation, such as "calculate the distance to the wall in front of me."

### Actions
**Actions** are for long-running tasks that provide continuous feedback. A client node sends a goal to an action server, which begins executing the task. The server provides regular feedback on its progress and can be cancelled by the client.

*   **Analogy**: Ordering a pizza for delivery. You get an initial confirmation (goal accepted), you can track its progress ("the pizza is in the oven"), and you can cancel the order before it arrives.
*   **Use Case**: Telling a robot arm to move to a specific position, or instructing a mobile robot to "navigate to the kitchen."

### Comparison Table

| Method | Type | Analogy | Use Case |
|---|---|---|---|
| **Topic** | One-to-Many, Continuous | Radio Station | Streaming sensor data |
| **Service** | One-to-One, Request/Reply | Vending Machine | Triggering a quick, blocking task |
| **Action** | One-to-One, Long-Running | Pizza Delivery | Executing a long-running goal with feedback |

Understanding these three communication methods is the key to building any ROS 2 system. By combining nodes that perform specific tasks with the right communication channels, you can create complex and robust robotic behaviors.
