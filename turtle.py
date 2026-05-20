#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import math


class TurtleHouse(Node):

    def __init__(self):
        super().__init__('turtle_house_drawer')

        self.publisher_ = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

        time.sleep(1)

        self.draw_house()

    def move(self, linear_speed, angular_speed, duration):
        msg = Twist()

        msg.linear.x = linear_speed
        msg.angular.z = angular_speed

        end_time = time.time() + duration

        while time.time() < end_time:
            self.publisher_.publish(msg)
            time.sleep(0.1)

        self.stop()

    def stop(self):
        msg = Twist()
        self.publisher_.publish(msg)
        time.sleep(0.5)

    def forward(self, distance, speed=2.0):
        duration = distance / speed
        self.move(speed, 0.0, duration)

    def turn(self, angle_deg, angular_speed=1.5):
        angle_rad = math.radians(angle_deg)
        duration = abs(angle_rad / angular_speed)

        direction = 1.0 if angle_deg > 0 else -1.0

        self.move(0.0, direction * angular_speed, duration)

    def draw_square(self, side):
        for _ in range(4):
            self.forward(side)
            self.turn(90)

    def draw_roof(self, side):
        self.turn(45)
        self.forward(side / 1.4)

        self.turn(90)
        self.forward(side / 1.4)

        self.turn(135)

    def draw_house(self):
        side = 3.0

        # Draw square base
        self.draw_square(side)

        # Move to roof start
        self.turn(90)
        self.forward(side)

        # Draw roof
        self.turn(-90)
        self.draw_roof(side)

        self.get_logger().info("House drawing completed!")


def main(args=None):
    rclpy.init(args=args)

    node = TurtleHouse()

    rclpy.spin_once(node, timeout_sec=1)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
