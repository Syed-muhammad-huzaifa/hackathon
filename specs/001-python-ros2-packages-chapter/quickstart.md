# Quickstart: Exploring Python ROS 2 Packages

This quickstart guide provides a high-level overview of the practical steps involved in creating, configuring, and launching ROS 2 Python packages, as detailed in "Chapter 2: Python ROS 2 Packages". It assumes you have a ROS 2 environment already set up.

## 1. Create a New ROS 2 Workspace

A ROS 2 workspace is where you store and build your ROS 2 packages.

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
colcon build
```

## 2. Create a Python ROS 2 Package

Use the `ros2 pkg create` command to create a new Python package.

```bash
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_python my_python_pkg
```

This will create a basic package structure with a `package.xml` and `setup.py` file.

## 3. Develop a ROS 2 Python Node

Navigate into your new package's directory (`~/ros2_ws/src/my_python_pkg`).

Create a Python file (e.g., `my_node.py`) inside `my_python_pkg/my_python_pkg/` (the sub-directory with the same name as the package) and add your node's logic.

```python
# my_node.py
import rclpy
from rclpy.node import Node

class MyPublisher(Node):
    def __init__(self):
        super().__init__('my_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    my_publisher = MyPublisher()
    rclpy.spin(my_publisher)
    my_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

## 4. Configure `setup.py`

Edit `~/ros2_ws/src/my_python_pkg/setup.py` to define the entry point for your node.

```python
from setuptools import setup

package_name = 'my_python_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/my_launch_file.launch.py']), # Example for launch file
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='you@example.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'my_node = my_python_pkg.my_node:main', # Define your node executable here
        ],
    },
)
```

## 5. Configure `package.xml`

Edit `~/ros2_ws/src/my_python_pkg/package.xml` to declare dependencies and metadata.

```xml
<?xml version="1.0"?>
<?xml-model href="http://download.ros.org/schema/package_format3.xsd" schematypens="http://www.w3.org/2001/XMLSchema"?>
<package format="3">
  <name>my_python_pkg</name>
  <version>0.0.0</version>
  <description>TODO: Package description</description>
  <maintainer email="you@example.com">Your Name</maintainer>
  <license>TODO: License declaration</license>
  <depend>rclpy</depend>
  <depend>std_msgs</depend> <!-- Add any messages types used -->
  <test_depend>ament_copyright</test_depend>
  <test_depend>ament_flake8</test_depend>
  <test_depend>ament_pep257</test_depend>
  <test_depend>python3-pytest</test_depend>
  <export>
    <build_type>ament_python</build_type>
  </export>
</package>
```

## 6. Build and Source Your Workspace

After making changes, rebuild your workspace and source the setup files.

```bash
cd ~/ros2_ws
colcon build --packages-select my_python_pkg
source install/setup.bash # or setup.zsh, setup.ps1
```

## 7. Run Your Node

You can now run your node using `ros2 run`.

```bash
ros2 run my_python_pkg my_node
```

## 8. Create and Use a Launch File (Optional)

Create a Python launch file (e.g., `my_launch_file.launch.py`) in a `launch` subdirectory within your package (`~/ros2_ws/src/my_python_pkg/launch/`).

```python
# my_launch_file.launch.py
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_python_pkg',
            executable='my_node',
            name='my_publisher_node',
            output='screen'
        ),
        # Add more nodes here if needed
    ])
```

Make sure to update `setup.py` (Step 4) to include the launch file in `data_files`. Rebuild and source your workspace (Step 6).

Then, launch your nodes:

```bash
ros2 launch my_python_pkg my_launch_file.launch.py
```
