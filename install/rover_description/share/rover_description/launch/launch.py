from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
import os
from ament_index_python.packages import get_package_share_directory
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command, LaunchConfiguration


def generate_launch_description():
    # Include the robot state publisher node
    
    model_arg = DeclareLaunchArgument(
        name='model',
        default_value=os.path.join(get_package_share_directory("rover_description"), "urdf", "rover.urdf"),
        description='Absolute Path to the URDF model of the robot to be used by the robot state publisher'
    )

    # Declare the model path as a parameter

    robot_description = ParameterValue(Command(['xacro ', LaunchConfiguration("model")]), value_type=str)
    
    
    # Create the robot state publisher node

    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description": robot_description}]
    )

    # Create the joint_state_publisher node

    joint_state_publisher_gui = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
    )


    # Create the rviz node 

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=["-d", os.path.join(get_package_share_directory("rover_description"), "rviz", "display.rviz")],
    )

    return LaunchDescription([


    ])