
import rclpy
from rclpy.node import Node
def main(args=None):
    rclpy.init(args=args)
    node = Node("py_test")
    node.get_logger().info("HEllo ROS2") #gives info just list hello world
    #rclpy.spin(node) # it will keep the node alive to exit press CTRL+C
    rclpy.shutdown()

if __name__ == "__main__":
    main()