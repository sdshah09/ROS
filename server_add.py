#!/usr/bin/env python3
from multiprocessing import get_logger
from urllib import request, response
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class Add_two_int(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("add_two_ints")
        self.server_ = self.create_service(AddTwoInts,"add_two_ints",self.callback_add_two_int)
        self.get_logger().info("Add two integers")

    def callback_add_two_int(self,request,response):
        response.sum = request.a + request.b
        self.get_logger().info(str(request.a)+ " + "+ str(request.b) + " = " + str(response.sum))
        return response

    
def main(args=None):
    rclpy.init(args=args)
    node = Add_two_int() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
