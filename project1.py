'''Cretae two nodes and one turtesim node and change all their names and display it using rqt'''
import rclpy
from rclpy.node import Node

class  MyNode(Node):

    def __init__(self):
        super().__init__("custom_py")
        self.counter_ = 0
        self.get_logger().info("Hola ROS2!")
        self.create_timer(0.5,self.time_callback)

    def time_callback(self):
        self.counter_ -=2
        self.get_logger().info("Hello " + str(self.counter_))

class MyNodee(Node):
    def __init__(self):
        super().__init__("this_is_a_really_long_name_for_a_cpp_node_but_it_works")
        self.get_logger().info("Hello Node2")

def main(args=None):
    rclpy.init(args=args)
    # node = Node("py_test")
    node = MyNode()
    node1 = MyNodee()
    #  node.get_logger().info("HEllo ROS2") #gives info just list hello world
    rclpy.spin(node) # it will keep the node alive to exit press CTRL+C
    
    rclpy.shutdown()

if __name__ == "__main__":
    main()