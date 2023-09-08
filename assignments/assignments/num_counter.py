#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String, Int32
#global count_
class COUNTER(Node):
    def __init__(self):
        super().__init__("number_counter")
        self.count_ = 0
        self.subscriber_ = self.create_subscription(Int32, "number",self.callback_robot_news, 100)
        self.publisher_ = self.create_publisher(Int32, "number_counter", 10)
        self.get_logger().info("robot_subscriber and publisher Node Started")
    def callback_robot_news(self, msg):
        self.count_ += msg.data
        number = Int32()
        number.data =self.count_
        self.publisher_.publish(number)
        self.get_logger().info(str(self.count_))
def main(args=None):
    rclpy.init(args=args)
    node = COUNTER()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == "__main__":
    main()