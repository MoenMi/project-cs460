import os
import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from webots_ros2_driver.webots_launcher import WebotsLauncher
from webots_ros2_driver.webots_controller import WebotsController


def generate_launch_description():
    # world_file = LaunchConfiguration('world')
    world_file = os.getenv('WORLD_FILE')
    package_dir = get_package_share_directory('project_cs460')
    robot_description_path = os.path.join(package_dir, 'resource', 'my_robot.urdf')

    webots = WebotsLauncher(
        world=os.path.join(package_dir, 'worlds', world_file)
        # world=os.path.join(package_dir, 'worlds', 'bruno-business-library.wbt')
    )

    my_robot_driver = WebotsController(
        robot_name='my_robot',
        parameters=[
            {'robot_description': robot_description_path},
        ]
    )

    return LaunchDescription([
        webots,
        my_robot_driver,
        launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=webots,
                on_exit=[launch.actions.EmitEvent(event=launch.events.Shutdown())],
            )
        ),
        # DeclareLaunchArgument(
        #     'world',
        #     description='World file to load'
        # ),
        # Node(
        #     package='project_cs460',
        #     executable='my_robot_driver',
        #     name='robot',
        #     output='screen',
        #     parameters=[{'world_file': world_file}],
        # ),
    ])