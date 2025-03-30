#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Talker(Node):
    def __init__(self):
        super().__init__("talker")
        self.pub = self.create_publisher(String, '/chatter', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.counter = 1

    def timer_callback(self):
        msg = String()
        msg.data = f"kem cho?: {self.counter}"
        self.pub.publish(msg)
        self.get_logger().info(msg.data)
        self.counter += 1


def main(args=None):
    rclpy.init(args=args)

    talker_node = Talker()
    rclpy.spin(talker_node)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
