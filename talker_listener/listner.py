#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ListnerNode(Node):
    def __init__(self):
        super().__init__("listner")
        self.sub = self.create_subscription(
            String,
            '/chatter',
            self.listner_callback,
            10)

    def listner_callback(self, msg):
        self.get_logger().info(f'{msg.data} majama!')

def main(args=None):
    rclpy.init(args=args)
    listner_node = ListnerNode()
    rclpy.spin(listner_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

