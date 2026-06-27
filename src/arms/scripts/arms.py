#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, Float32MultiArray


class ArmsController(Node):
    def __init__(self):
        super().__init__('arms_controller')

        # Subscribe to wheel commands
        self.subscription = self.create_subscription(
            Float32MultiArray,
            'wheel_cmd',
            self.wheel_callback,
            10
        )

        # Publish arm command
        self.publisher_ = self.create_publisher(
            Float32,
            'arm_cmd',
            10
        )

        self.get_logger().info("Arms Controller Started")

    def wheel_callback(self, msg):
        left = msg.data[0]
        right = msg.data[1]

        arm_msg = Float32()

        # RULE:
        # wheels = 0 → arms MOVE
        # wheels > 0 → arms STOP

        if left == 0.0 and right == 0.0:
            arm_msg.data = 1.0   # MOVE arms
            self.get_logger().info("WHEELS STOPPED → ARMS MOVING")
        else:
            arm_msg.data = 0.0   # STOP arms
            self.get_logger().info("WHEELS MOVING → ARMS STOPPED")

        self.publisher_.publish(arm_msg)


def main(args=None):
    rclpy.init(args=args)

    node = ArmsController()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
