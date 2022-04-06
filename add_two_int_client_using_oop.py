import rclpy
from rclpy.node import Node
from functools import partial
from example_interfaces.srv import AddTwoInts

class Addtwointsclient(Node):
    def __init__(self):
        super().__init__("add_two_inst_client")
        self.call_server(6,7)
        self.call_server(3,4)
        
    def call_server(self,a,b):
        client = self.create_client(AddTwoInts,"add_two_ints")
        while not client.wait_for_service(1.0): #todo: will wait for service for 1 second
            self.get_logger().warn("Waiting for Server...")

        request = AddTwoInts.Request()
        request.a = a
        request.b = b

        future = client.call_async(request)
        future.add_done_callback(partial(self.call_server,a=a,b=b))
    
    def callback_add(self,future,a,b):
        try:
            response = future.result()
            self.get_logger.info(str(a)+ " + "+ str(b) + " = " + str(response.sum))
        
        except Exception as e:
            self.get_logger().error("Service call failed %r")

def main(args=None):
    rclpy.init(args=args)
    node = Addtwointsclient() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
