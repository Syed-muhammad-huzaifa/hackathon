# Data Model: Python ROS 2 Packages Chapter (Conceptual Entities)

This section describes the key conceptual entities that will be explained and structured within the "Python ROS 2 Packages" textbook chapter. These are not data models for software implementation but rather the core information units that the chapter will convey to the reader.

## Conceptual Entities

### ROS 2 Python Package

- **Description**: The fundamental unit of software organization in ROS 2 for Python-based components. It encapsulates nodes, configuration, and dependencies.
- **Attributes**:
    - `name`: Unique identifier for the package.
    - `version`: Software version of the package.
    - `description`: Human-readable summary of the package's purpose.
    - `maintainer`: Contact information for package maintainer(s).
    - `license`: Software license under which the package is distributed.
    - `dependencies`: Other ROS 2 packages or system libraries that this package relies on.
    - `nodes`: Python executables that perform specific tasks within the ROS 2 graph.
- **Relationships**:
    - Contains `Node`s.
    - Depends on other `ROS 2 Python Package`s.
    - Defined by `package.xml` and `setup.py`.

### Node

- **Description**: An executable process within a ROS 2 system that performs a specific, often modular, computation (e.g., sensor driver, data processing, control algorithm).
- **Attributes**:
    - `name`: Unique name within the ROS 2 graph (can be remapped).
    - `type`: The Python class or function that implements the node's logic.
    - `publisher`: Publishes data to topics.
    - `subscriber`: Subscribes to data from topics.
    - `service_server`: Offers services.
    - `service_client`: Requests services.
    - `action_server`: Offers action goals.
    - `action_client`: Requests action goals.
- **Relationships**:
    - Belongs to a `ROS 2 Python Package`.
    - Communicates with other `Node`s via ROS 2 communication primitives.

### package.xml (Package Manifest)

- **Description**: An XML file providing metadata about a ROS 2 package, essential for build systems (like `ament_cmake`, `ament_python`) and package management.
- **Key Elements**:
    - `<name>`, `<version>`, `<description>`, `<maintainer>`, `<license>`
    - `<depend>`, `<build_depend>`, `<exec_depend>`, etc. (for specifying dependencies)
    - `<export>` (for exporting build/run information)
- **Relationships**:
    - Defines metadata and dependencies for a `ROS 2 Python Package`.

### setup.py (Python Setup Script)

- **Description**: A Python script used by `ament_python` to configure how a Python-based ROS 2 package is built and installed. It uses `setuptools`.
- **Key Elements**:
    - `setup()` function call.
    - `package_dir`, `packages`.
    - `entry_points` (crucial for defining ROS 2 executables/nodes).
- **Relationships**:
    - Configures the build and installation process for a `ROS 2 Python Package`.
    - Declares `Node`s as entry points.

### Launch File

- **Description**: An XML or Python file (using `ros2 launch`) used to start and configure multiple ROS 2 nodes, potentially with arguments and remapping rules, in a coordinated manner.
- **Attributes**:
    - `nodes`: List of nodes to be launched.
    - `parameters`: Configuration values passed to nodes.
    - `remappings`: Rules for changing topic, service, or action names.
    - `arguments`: Command-line arguments for launch file.
- **Relationships**:
    - Orchestrates the execution of multiple `Node`s.
    - Part of a `ROS 2 Python Package` or a separate launch package.

## Relationships Overview

- A `ROS 2 Python Package` is described by `package.xml` and configured for building/installation by `setup.py`.
- A `ROS 2 Python Package` contains one or more `Node`s.
- `Node`s communicate with each other and are orchestrated by `Launch File`s.
- `Launch File`s can be part of a `ROS 2 Python Package` or a dedicated launch package.
