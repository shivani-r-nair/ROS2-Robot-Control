#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class LidarPublisher(Node):
    def __init__(self):
        super().__init__('lidar_publisher')

        self.publisher_ = self.create_publisher(Int32, 'lidar_data', 10)

        self.timer = self.create_timer(1.0, self.timer_callback)
        self.count = 0

        self.get_logger().info('Lidar Publisher Node Started')

    def timer_callback(self):
        msg = Int32()
        msg.data = self.count

        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')

        self.count += 1
        if self.count > 10:
            self.count = 0


def main(args=None):
    rclpy.init(args=args)
    node = LidarPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
