import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped

class Republisher(Node):
    def __init__(self):
        super().__init__('twist_stamped_republisher')
        self.sub = self.create_subscription(
            TwistStamped,
            '/cmd_vel/geometryTwistStamped',
            self.listener_callback,
            10
        )
        self.pub = self.create_publisher(
            TwistStamped,
            '/halleffect_controller/cmd_vel/geometryTwistStamped',
            10
        )

    def listener_callback(self, msg):
        self.pub.publish(msg)
        self.get_logger().info('Republished TwistStamped message')

def main(args=None):
    rclpy.init(args=args)
    node = Republisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()