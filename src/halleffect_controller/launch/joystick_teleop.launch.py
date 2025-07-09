import os

from ament_index_python.packages import get_package_share_directory

import launch
import launch_ros.actions


def generate_launch_description():
    joy_config = launch.substitutions.LaunchConfiguration('joy_config')
    joy_dev = launch.substitutions.LaunchConfiguration('joy_dev')
    publish_stamped_twist = launch.substitutions.LaunchConfiguration('publish_stamped_twist')
    config_filepath = launch.substitutions.LaunchConfiguration('config_filepath')

    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument('joy_vel', default_value='cmd_vel'),
        launch.actions.DeclareLaunchArgument('joy_config', default_value='ps3'),
        launch.actions.DeclareLaunchArgument('joy_dev', default_value='0'),
        launch.actions.DeclareLaunchArgument('publish_stamped_twist', default_value='true'),
        
        
        launch.actions.DeclareLaunchArgument('config_filepath', default_value=[
            launch.substitutions.TextSubstitution(text=os.path.join(
                get_package_share_directory('teleop_twist_joy'), 'config', '')),
            joy_config, launch.substitutions.TextSubstitution(text='.joy_config.yaml')]),



        launch_ros.actions.Node(
            package='joy', 
            executable='joy_node', 
            name='joy_node',
            parameters=['/home/ubuntu/rover_ws/src/halleffect_controller/config/joy_config.yaml'
            ]),


        launch_ros.actions.Node(
            package='teleop_twist_joy', 
            executable='teleop_node',
            name='teleop_twist_joy_node',
            parameters=['/home/ubuntu/rover_ws/src/halleffect_controller/config/teleop_twist_joy_node.yaml', {'publish_stamped_twist': publish_stamped_twist}],
            remappings={('/cmd_vel', launch.substitutions.LaunchConfiguration('joy_vel'))},
        ),


        launch_ros.actions.Node(
            package='halleffect_controller',
            executable='joystick_republisher',
            name='joystick_republisher',
            output='screen',
            parameters=['/home/ubuntu/rover_ws/src/halleffect_controller/config/joystick_republisher.yaml']
        )


    ])