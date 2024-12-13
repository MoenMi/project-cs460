# import os
# import launch
# from launch import LaunchDescription
# from launch.actions import DeclareLaunchArgument
# from launch.substitutions import LaunchConfiguration
# from launch_ros.actions import Node
# from ament_index_python.packages import get_package_share_directory
# from webots_ros2_driver.webots_launcher import WebotsLauncher
# from webots_ros2_driver.webots_controller import WebotsController
# from webots_ros2_driver.wait_for_controller_connection import WaitForControllerConnection


# def generate_launch_description():
#     # world_file = LaunchConfiguration('world')
#     world_file = os.getenv('WORLD_FILE')
#     package_dir = get_package_share_directory('project_cs460')
#     robot_description_path = os.path.join(package_dir, 'resource', 'my_robot.urdf')

#     webots = WebotsLauncher(
#         world=os.path.join(package_dir, 'worlds', world_file)
#         # world=os.path.join(package_dir, 'worlds', 'bruno-business-library.wbt')
#     )

#     robot_state_publisher = Node(
#         package='robot_state_publisher',
#         executable='robot_state_publisher',
#         output='screen',
#         parameters=[{
#             'robot_description': '<robot name=""><link name=""/></robot>'
#         }],
#     )

#     footprint_publisher = Node(
#         package='tf2_ros',
#         executable='static_transform_publisher',
#         output='screen',
#         arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'base_footprint'],
#     )

#     # ROS control spawners
#     controller_manager_timeout = ['--controller-manager-timeout', '50']
#     controller_manager_prefix = 'python.exe' if os.name == 'nt' else ''
#     diffdrive_controller_spawner = Node(
#         package='controller_manager',
#         executable='spawner',
#         output='screen',
#         prefix=controller_manager_prefix,
#         arguments=['diffdrive_controller'] + controller_manager_timeout,
#     )
#     joint_state_broadcaster_spawner = Node(
#         package='controller_manager',
#         executable='spawner',
#         output='screen',
#         prefix=controller_manager_prefix,
#         arguments=['joint_state_broadcaster'] + controller_manager_timeout,
#     )
#     ros_control_spawners = [diffdrive_controller_spawner, joint_state_broadcaster_spawner]

#     robot_description_path = os.path.join(package_dir, 'resource', 'my_robot.urdf')
#     ros2_control_params = os.path.join(package_dir, 'resource', 'ros2control.yml')
#     mappings = [('/diffdrive_controller/cmd_vel_unstamped', '/cmd_vel'), ('/diffdrive_controller/odom', '/odom')]
#     use_sim_time = LaunchConfiguration('use_sim_time', default=True)

#     my_robot_driver = WebotsController(
#         robot_name='TurtleBot3Burger',
#         parameters=[
#             {'robot_description': robot_description_path,
#              'use_sim_time': use_sim_time,
#              'set_robot_state_publisher': True},
#             ros2_control_params
#         ],
#         remappings=mappings,
#         respawn=True
#     )

#     # Wait for the simulation to be ready to start controllers
#     waiting_nodes = WaitForControllerConnection(
#         target_driver=my_robot_driver,
#         nodes_to_start= ros_control_spawners
#     )

#     return LaunchDescription([
#         webots,
#         my_robot_driver,
#         waiting_nodes,
#         robot_state_publisher,
#         footprint_publisher,
#         DeclareLaunchArgument(
#             'mode',
#             default_value='realtime',
#             description='Webots startup mode'
#         ),
#         launch.actions.RegisterEventHandler(
#             event_handler=launch.event_handlers.OnProcessExit(
#                 target_action=webots,
#                 on_exit=[launch.actions.EmitEvent(event=launch.events.Shutdown())],
#             )
#         ),
#         # DeclareLaunchArgument(
#         #     'world',
#         #     description='World file to load'
#         # ),
#         # Node(
#         #     package='project_cs460',
#         #     executable='my_robot_driver',
#         #     name='robot',
#         #     output='screen',
#         #     parameters=[{'world_file': world_file}],
#         # ),
#     ])



import os
import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from webots_ros2_driver.webots_launcher import WebotsLauncher
from webots_ros2_driver.webots_controller import WebotsController
from webots_ros2_driver.wait_for_controller_connection import WaitForControllerConnection


def generate_launch_description():
    world_file = os.getenv('WORLD_FILE', 'default_world.wbt')
    package_dir = get_package_share_directory('project_cs460')
    robot_description_path = os.path.join(package_dir, 'resource', 'my_robot.urdf')

    webots = WebotsLauncher(
        world=os.path.join(package_dir, 'worlds', world_file)
    )

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': open(robot_description_path).read()}],
    )

    footprint_publisher = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        output='screen',
        arguments=['0', '0', '0', '0', '0', '0', '1', 'base_link', 'base_footprint'],
    )

    controller_manager_timeout = ['--controller-manager-timeout', '50']
    diffdrive_controller_spawner = Node(
        package='controller_manager',
        executable='spawner',
        output='screen',
        arguments=['diffdrive_controller'] + controller_manager_timeout,
    )
    joint_state_broadcaster_spawner = Node(
        package='controller_manager',
        executable='spawner',
        output='screen',
        arguments=['joint_state_broadcaster'] + controller_manager_timeout,
    )

    ros2_control_params = os.path.join(package_dir, 'resource', 'ros2control.yml')
    my_robot_driver = WebotsController(
        robot_name='TurtleBot3Burger',
        parameters=[
            {'robot_description': robot_description_path,
            #  'robot_description': open(robot_description_path).read(),
             'use_sim_time': True,
             'set_robot_state_publisher': True},
            ros2_control_params
        ],
        remappings=[
            ('/diffdrive_controller/cmd_vel_unstamped', '/cmd_vel'),
            ('/diffdrive_controller/odom', '/odom')
        ],
        respawn=True
    )

    waiting_nodes = WaitForControllerConnection(
        target_driver=my_robot_driver,
        nodes_to_start=[diffdrive_controller_spawner, joint_state_broadcaster_spawner]
    )

    return LaunchDescription([
        webots,
        robot_state_publisher,
        footprint_publisher,
        my_robot_driver,
        waiting_nodes,
        DeclareLaunchArgument(
            'mode',
            default_value='realtime',
            description='Webots startup mode'
        ),
        launch.actions.RegisterEventHandler(
            event_handler=launch.event_handlers.OnProcessExit(
                target_action=webots,
                on_exit=[launch.actions.EmitEvent(event=launch.events.Shutdown())],
            )
        ),
    ])
