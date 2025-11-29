# Quickstart: Exploring URDF

This quickstart guide provides a high-level overview of the practical steps involved in creating, visualizing, and simulating URDF models, as detailed in "Chapter 3: URDF". It assumes you have a ROS 2 environment with RViz and Gazebo already set up.

## 1. Understand the Core Concepts

Before diving into code, familiarize yourself with:
- **Links**: Rigid bodies of the robot (e.g., torso, upper arm, wheel).
- **Joints**: Connections between links, defining their relative motion (e.g., revolute for rotation, fixed for rigid connections).

## 2. Create a Basic URDF File

Start by creating a simple `.urdf` file (e.g., `my_robot.urdf`) in a ROS 2 package. A minimal URDF defines at least one link.

```xml
<?xml version="1.0"?>
<robot name="my_simple_robot">

  <link name="base_link">
    <visual>
      <geometry><box size="0.6 0.4 0.2"/></geometry>
      <material name="blue"><color rgba="0 0 0.8 1"/></material>
    </visual>
  </link>

  <link name="caster_link">
    <visual>
      <geometry><sphere radius="0.05"/></geometry>
      <material name="white"><color rgba="1 1 1 1"/></material>
    </visual>
  </link>

  <joint name="base_to_caster" type="fixed">
    <parent link="base_link"/>
    <child link="caster_link"/>
    <origin xyz="-0.2 0 -0.1"/>
  </joint>

</robot>
```
Remember to define materials or reference existing ones if specified in your URDF.

## 3. Visualize Your URDF in RViz

To see your robot model:
- Ensure your URDF is accessible to ROS 2 (e.g., within a package and sourced).
- Use `urdf_tutorial`'s `display.launch.py` or a custom launch file with `robot_state_publisher` and `joint_state_publisher_gui`.

```bash
# Example using urdf_tutorial (if installed)
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$(pwd) # Add current dir to ROS_PACKAGE_PATH if URDF is standalone
ros2 launch urdf_tutorial display.launch.py model:=my_robot.urdf
```
Or, more commonly, launch `robot_state_publisher` and `joint_state_publisher_gui` in your own package's launch file.

## 4. Integrate URDF with Gazebo (for Simulation)

For simulation in Gazebo, a URDF often needs additional tags (e.g., `<gazebo>` tags for physics properties, plugins).

-   **Add Gazebo references**: Extend your URDF with `<gazebo>` elements to define material colors in Gazebo and attach Gazebo plugins.
-   **Launch in Gazebo**: Use a launch file to spawn your robot model in Gazebo.

```xml
<!-- Example Gazebo snippet in URDF -->
<gazebo reference="base_link">
  <material>Gazebo/Blue</material>
</gazebo>
```

Launch command:
```bash
ros2 launch gazebo_ros spawn_entity.launch.py -entity my_robot -topic robot_description
```
(This assumes `robot_description` is published, often by `robot_state_publisher` reading your URDF.)

## 5. XACRO for Modular URDFs (Recommended)

For complex robots, use XACRO (`.urdf.xacro` files) to create modular and reusable URDF components. This allows you to define macros for common parts (e.g., a wheel, a sensor mount) and include them in your main robot description.

```xml
<?xml version="1.0"?>
<robot name="my_modular_robot" xmlns:xacro="http://ros.org/xacro">
  <xacro:include filename="$(find my_package)/urdf/macros.xacro" />
  <xacro:my_macro arg1="value"/>
</robot>
```
Remember to process XACRO files into standard URDF before using them with tools that only accept `.urdf` (e.g., `ros2 run xacro xacro my_robot.urdf.xacro > my_robot.urdf`).
