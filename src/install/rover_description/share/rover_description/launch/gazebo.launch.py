from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, SetEnvironmentVariable, IncludeLaunchDescription
import os
from pathlib import Path
from ament_index_python.packages import get_package_share_directory
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command, LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    
    use_sim_time_arg = DeclareLaunchArgument(
        "use_sim_time",
        default_value="True",
    )
    rover_description_dir = get_package_share_directory("rover_description")
    ros_distro = os.environ.get("ROS_DISTRO")
    is_ignition = "True" if ros_distro == "humble" else "False"

    model_arg = DeclareLaunchArgument(name="model", default_value=os.path.join(
                                        rover_description_dir, "urdf", "rover.urdf.xacro"
                                        ),
                                        description='Absolute Path to the URDF model of the robot to be used by the robot state publisher'
    )


    use_sim_time = LaunchConfiguration("use_sim_time")
    
    # Declare the model path as a parameter

    robot_description = ParameterValue(Command([
        "xacro ", 
        LaunchConfiguration("model"),
        " is_ignition:=", 
        is_ignition
        ]), 
        value_type=str)


    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description": robot_description,
                     "use_sim_time": use_sim_time}]
    )

    gazebo_resource_path = SetEnvironmentVariable(
        name='GZ_SIM_RESOURCE_PATH',
        value=[
            str(Path(rover_description_dir).parent.resolve())
            ]
    )


    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('ros_gz_sim'), 'launch'),"/gz_sim.launch.py"]),
        launch_arguments=[
            ("gz_args", [" -v 4", " -r", " empty.sdf"])
            ]
    )

    gz_spawn_entity = Node(
        package='ros_gz_sim',
        executable="create",
        arguments=[
            "-topic", 
            "robot_description",
            "-name", 
            "rover"],
        output='screen'
    )


    bridge_params = os.path.join(get_package_share_directory("halleffect_controller"), "config", "gz_bridge.yaml")

    ros_gz_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        name='ros_gz_bridge',
        parameters=[{'config_file': bridge_params}],
    )


    return LaunchDescription([
        use_sim_time_arg,
        model_arg,
        robot_state_publisher,
        gazebo_resource_path,
        gazebo,
        gz_spawn_entity,
        ros_gz_bridge

    ])
