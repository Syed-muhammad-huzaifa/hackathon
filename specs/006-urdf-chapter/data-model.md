# Data Model: URDF Chapter (Conceptual Entities)

This section describes the key conceptual entities that will be explained and structured within the "URDF" textbook chapter. These are not data models for software implementation but rather the core information units that the chapter will convey to the reader.

## Conceptual Entities

### URDF (Unified Robot Description Format)

-   **Description**: An XML format for describing all aspects of a robot, including its kinematic and dynamic structure, visual appearance, and collision properties. It serves as a universal language for robot models in ROS.
-   **Attributes**:
    -   `links`: Represent the rigid bodies of the robot.
    -   `joints`: Represent the connections between links, defining their relative motion.
    -   `sensors`: (Conceptual representation) How sensors are attached and their properties.
    -   `actuators`: (Conceptual representation) How actuators are attached and their properties.
-   **Relationships**:
    -   Composed of `Link`s and `Joint`s.
    -   Used by `RViz` for visualization and `Gazebo` for simulation.
    -   Essential for `Humanoid Robot`s and `Mobile Robot`s.

### Link

-   **Description**: A rigid body part of the robot. Links have physical properties (mass, inertia), visual properties (geometry, color/texture), and collision properties.
-   **Attributes**:
    -   `name`: Unique identifier for the link.
    -   `visual`: Describes the visual representation of the link.
    -   `collision`: Describes the collision geometry of the link.
    -   `inertial`: Describes the mass and inertia properties of the link.
-   **Relationships**:
    -   Connected to other `Link`s by `Joint`s.
    -   Forms the kinematic chain of the robot.

### Joint

-   **Description**: A connection between two links that defines their relative motion and limits. Joints can be of various types (e.g., revolute, prismatic, fixed).
-   **Attributes**:
    -   `name`: Unique identifier for the joint.
    -   `type`: The type of motion allowed (e.g., `revolute`, `continuous`, `prismatic`, `fixed`).
    -   `parent`: The name of the parent `Link`.
    -   `child`: The name of the child `Link`.
    -   `origin`: The transform from the parent link's frame to the joint's frame.
    -   `axis`: The axis of rotation or translation for revolute/prismatic joints.
    -   `limit`: Defines the upper, lower, velocity, and effort limits for the joint.
-   **Relationships**:
    -   Connects a `parent Link` to a `child Link`.
    -   Defines the robot's degrees of freedom.

### Sensor (Conceptual Representation)

-   **Description**: How sensors (e.g., cameras, LiDAR, IMU) are typically attached to a robot and their properties are conceptually represented in URDF, often via an additional link and joint.
-   **Attributes**:
    -   `name`: (of the associated link/joint)
    -   `type`: (e.g., camera, lidar - implicitly derived from external plugins/definitions)
-   **Relationships**:
    -   Attached to a `Link`.
    -   Properties are often defined in Gazebo/RViz plugins associated with the URDF.

### Actuator (Conceptual Representation)

-   **Description**: How actuators (e.g., motors, grippers) are typically attached to a robot and their properties are conceptually represented in URDF, often linked to joints.
-   **Attributes**:
    -   `name`: (of the associated joint/link)
    -   `type`: (e.g., motor, servo - implicitly derived from external plugins/definitions)
-   **Relationships**:
    -   Associated with a `Joint` (e.g., providing torque for a revolute joint).
    -   Properties are often defined in Gazebo/RViz plugins associated with the URDF.

### RViz

-   **Description**: A 3D visualizer for ROS. It uses URDF models to display the robot's kinematic state and sensor data in a dynamic environment.
-   **Relationships**:
    -   Consumes `URDF` models for visualization.

### Gazebo

-   **Description**: A powerful 3D robot simulator. It uses URDF models (often converted to SDF) to simulate the robot's physics, sensor data, and interactions with the environment.
-   **Relationships**:
    -   Utilizes `URDF` models for physics simulation.

### Humanoid Robot

-   **Description**: A robot designed to resemble the human body, typically with a torso, head, two arms, and two legs.
-   **Importance of URDF**: Crucial for defining complex kinematics, balance, and whole-body control.

### Mobile Robot

-   **Description**: A robot capable of moving in its environment, often on wheels or tracks.
-   **Importance of URDF**: Essential for defining its base structure, wheel kinematics, and sensor placement for navigation.