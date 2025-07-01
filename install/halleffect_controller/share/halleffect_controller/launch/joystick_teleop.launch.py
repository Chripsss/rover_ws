import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    use_sim_time_arg = DeclareLaunchArgument(name="use_sim_time", default_value="True",
                                      description="Use simulated time"
    )

    teleop_twist_joy = Node(
    package='teleop_twist_joy',
    executable='teleop_node',
    name='teleop_twist_joy',
    parameters=[os.path.join(
        get_package_share_directory("halleffect_controller"),
        "config", "teleop_twist_joy.yaml"
    ),
                {"use_sim_time": LaunchConfiguration("use_sim_time")}]
)


    joy_node = Node(
        package="joy",
        executable="joy_node",
        name="joystick",
        parameters=[os.path.join(get_package_share_directory("halleffect_controller"), "config", "joy_config.yaml"),
                    {"use_sim_time": LaunchConfiguration("use_sim_time")}]
    )

    return LaunchDescription(
        [
            use_sim_time_arg,
            teleop_twist_joy,
            joy_node
        ]
    )