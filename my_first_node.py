
import rclpy
from rclpy.node import Node

class  MyNode(Node):

    def __init__(self):
        super().__init__("py_test")
        self.counter_ = 0
        self.get_logger().info("Hola ROS2")
        self.create_timer(0.5,self.time_callback)

    def time_callback(self):
        self.counter_ -=1
        self.get_logger().info("Hello " + str(self.counter_))

def main(args=None):
    rclpy.init(args=args)
    # node = Node("py_test")
    node = MyNode()
    #  node.get_logger().info("HEllo ROS2") #gives info just list hello world
    rclpy.spin(node) # it will keep the node alive to exit press CTRL+C
    
    rclpy.shutdown()

if __name__ == "__main__":
    main()