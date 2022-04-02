import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

def main(args=None):
    rclpy.init(args=args)
    node = Node("add_two_ints_client")

    client = node.create_client(AddTwoInts,"add_two_ints")
    while not client.wait_for_service(1.0): #todo: will wait for service for 1 second
        node.get_logger().warn("Waiting for Server...")
    
    request = AddTwoInts.Request()
    request.a = 3
    request.b = 4
    future = client.call_async(request) #? future object will save the value for future use
    rclpy.spin_until_future_complete(node,future)

    try:
        response = future.result()
        node.get_logger.info(str(request.a)+ " + "+ str(request.b) + " = " + str(response.sum))
    
    except Exception as e:
        node.get_logger().error("Service call failed %r")
    rclpy.shutdown()

    if __name__ == "__main__":
        main()