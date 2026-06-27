#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, Float32MultiArray


class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller')

        # Subscribe to LiDAR
        self.subscription = self.create_subscription(
            Int32,
            'lidar_data',
            self.lidar_callback,
            10
        )

        # Publish wheel commands
        self.publisher_ = self.create_publisher(
            Float32MultiArray,
            'wheel_cmd',
            10
        )

        self.get_logger().info("Robot Controller Started")

    def lidar_callback(self, msg):
        lidar_value = msg.data

        cmd = Float32MultiArray()

        # RULE:
        # 0–3 => STOP
        # >3  => MOVE
        if lidar_value <= 3:
            cmd.data = [0.0, 0.0]   # STOP
            self.get_logger().info(f"LIDAR {lidar_value} -> STOP")
        else:
            cmd.data = [2.0, 2.0]   # MOVE forward
            self.get_logger().info(f"LIDAR {lidar_value} -> MOVE")

        self.publisher_.publish(cmd)


def main(args=None):
    rclpy.init(args=args)
    node = RobotController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

