from launch import LaunchDescription
from launch_ros.actions import Node
def generate_launch_description():
    return LaunchDescription([
    Node(
    package='assignment_pkg',
    namespace = 'ns1',
    executable='publisher',
    name = 'publisher',
    argument = ['--ros-args', '--log-level', 'fatal']),
    Node(
    package='assignment_pkg',
    namespace = 'ns1',
    executable='subscriber',
    name = 'subscriber',
    argument = ['--ros-args', '--log-level', 'fatal']),
    ])