from multiprocessing import get_logger
from rospkg import get_log_dir
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64


class NumberPub(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("number_publisher") # MODIFY NAME
        
        self.publisher_ = self.create_publisher(Int64,"number",10)
        self.number_ = 2
        self.timer_ = self.create_timer(0.5,self.nump)
        self.get_logger().info("Number publisher has been started..")

    def nump(self):
        msg = Int64()
        msg.data = self.number_
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = NumberPub() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
