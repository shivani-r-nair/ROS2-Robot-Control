from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='lidar',
            executable='lidar.py',
            output='screen'
        ),
        Node(
            package='wheels',
            executable='wheels.py',
            output='screen'
        ),
        Node(
            package='arms',
            executable='arms.py',
            output='screen'
        ),
    ])
