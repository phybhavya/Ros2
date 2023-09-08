#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
# import math,transforms3d
rn=100
class LidarNode(Node):
    def __init__(self):
        super().__init__("Lidar_msgs")
        self.lidar_subscriber = self.create_subscription(LaserScan, 'gazebo_lidar/out',self.robot_lidar_callback, 10)
        self.get_logger().info("Lidar Node subscribed")
        self.publisher = self.create_publisher(Twist, "/cmd_vel", 10)
        self.subscriber = self.create_subscription(Odometry, "/odom", self.control_loop, 10)
    def robot_lidar_callback(self,msg):
        global rn
        vel  = msg.ranges
        rn = min(vel)
        print(rn)

        if rn<10:
            rn=100
  
    def control_loop(self,msg):
        vel = Twist()
        if(rn <10):
            vel.linear.x = 0.0 
        else:
            vel.linear.x = 1.0
            vel.angular.z = 0.0*round(2) 
              
        print('speed : {}'.format(vel))    
        self.publisher.publish(vel)

def main(args=None):
    global rn
    rn=100
    rclpy.init(args=args)
    node = LidarNode() 
    rclpy.spin(node)
    rclpy.shutdown()
     
     
if __name__ == "__main__":
    main()