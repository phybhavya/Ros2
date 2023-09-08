#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int32,String
class NumberPublisher(Node):
    def __init__(self):
        super().__init__("number_publisher")
        self.number = 2
        self.publisher_ = self.create_publisher(Int32, "number", 10)
        self.timer_ = self.create_timer(2, self.publish_news)
        self.get_logger().info("Number Publisher has started")
    def publish_news(self):
        msg = Int32()
        msg.data = self.number
        self.publisher_.publish(msg)
        print(msg)
def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisher()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == '__main__':
    main()