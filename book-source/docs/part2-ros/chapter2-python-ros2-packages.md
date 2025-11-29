# Chapter 2: Python ROS 2 Packages

(This chapter is designed to be 600-800 words, beginner-friendly, technically accurate, and aligned with the course outline.)

## Introduction to ROS 2 Python Packages

ROS 2 (Robot Operating System 2) leverages Python for modular robotic software development. A ROS 2 Python package is a fundamental container for your Python code, configurations, and resources, enabling easy sharing and reuse of robot functionalities. This chapter introduces you to creating, configuring, and utilizing these packages.

## Creating a ROS 2 Python Package

To create a new Python package, navigate to your ROS 2 workspace's `src` directory and use `ros2 pkg create --build-type ament_python <package_name>`. For example, `ros2 pkg create --build-type ament_python my_robot_controller`.

This command generates a directory structure including:
-   `package.xml`: For package metadata and dependencies.
-   `setup.py`: For build and installation instructions.
-   `my_robot_controller/my_robot_controller/`: A Python module directory containing `__init__.py`.

## ROS 2 Nodes in Python Packages

ROS 2 applications consist of **nodes**, which are executables performing specific tasks. In Python, nodes are typically classes inheriting from `rclpy.node.Node`, residing within your package's Python module directory (e.g., `my_robot_controller/my_robot_controller/`). The `__init__.py` file here designates it as a Python package.

A basic ROS 2 Python node structure (`simple_publisher.py`):

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SimplePublisher(Node):
    def __init__(self):
        super().__init__('simple_publisher_node')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        self.timer = self.create_timer(0.5, self.publish_message)
        self.i = 0
    def publish_message(self):
        msg = String(data=f'Hello ROS 2: {self.i}')
        self.publisher_.publish(msg)
        self.i += 1
def main(args=None):
    rclpy.init(args=args); node = SimplePublisher(); rclpy.spin(node)
    node.destroy_node(); rclpy.shutdown()
if __name__ == '__main__': main()
```

## Understanding package.xml

The `package.xml` file is your package's manifest, detailing its metadata and dependencies. It's crucial for ROS 2 to build, install, and run your package correctly.

Key elements:
-   **`<name>`, `<version>`, `<description>`, `<maintainer>`, `<license>`**: Basic package information.
-   **Dependency Tags**: e.g., `<depend>rclpy</depend>` for runtime needs.
-   **`<export>`**: Declares the build system type, e.g., `<build_type>ament_python</build_type>`.

Example `package.xml` snippet:

```xml
<package format="3">
  <name>my_robot_controller</name>
  <version>0.0.0</version>
  <description>A basic ROS 2 Python package.</description>
  <maintainer email="your_email@example.com">Your Name</maintainer>
  <license>Apache-2.0</license>
  <depend>rclpy</depend>
  <depend>std_msgs</depend>
  <export><build_type>ament_python</build_type></export>
</package>
```

## Understanding setup.py

`setup.py` defines how your Python package is built, installed, and how its nodes are exposed to ROS 2, utilizing Python's `setuptools`.

Key elements:
-   **`name`, `version`, `packages`**: Package structure.
-   **`data_files`**: Lists non-Python files (like `package.xml`, launch files) for installation.
-   **`entry_points`**: Crucially defines console scripts for your nodes, making them executable via `ros2 run`.

Example `setup.py` snippet:

```python
from setuptools import setup
import os; from glob import glob; package_name = 'my_robot_controller'
setup(
    name=package_name, version='0.0.0', packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    entry_points={
        'console_scripts': ['simple_publisher_node = my_robot_controller.simple_publisher:main'],
    },
)
```
`entry_points` maps an executable name to a Python function, enabling `ros2 run`.

## Launching Multiple ROS 2 Nodes

In real robotics, multiple nodes work together. **ROS 2 launch files** (Python scripts) manage their simultaneous startup and configuration, providing a centralized approach to:
-   Start multiple nodes.
-   Configure nodes with parameters and remappings.
-   Manage node lifecycle.

Example Python launch file (`my_robot_controller/launch/my_example_launch.launch.py`):

```python
from launch import LaunchDescription; from launch_ros.actions import Node
def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_robot_controller', executable='simple_publisher_node',
            name='publisher_node_instance', output='screen', emulate_tty=True,
        ),
    ])
```
After `setup.py` is updated, and the workspace built/sourced, execute with `ros2 launch my_robot_controller my_example_launch.launch.py`.

## Real-World Integration of ROS 2 Python Packages

ROS 2 Python packages are vital for deploying robots, enabling them to perceive, decide, and act.

**1. Sensor Drivers and Data Processing:** Packages wrap Python APIs for sensors (e.g., cameras, LiDAR) to publish data as ROS 2 topics. For instance, a node might process camera images and publish them for navigation.

**2. Robot Control and Actuation:** Python packages implement higher-level control (e.g., PID controllers) and interface with actuators. Nodes translate command topics (e.g., velocity) into hardware-specific motor controls.

ROS 2 Python packages offer a modular, communicative structure, making them ideal for rapid prototyping and deployment on real robots.