import rclpy
from rclpy.node import Node
from std_msgs.msg import String


# Create a class called SimplePublisher.
# It inherits from Node, because every ROS 2 program is usually written as a node.
class SimplePublisher(Node):

    # Constructor of the class.
    # This function runs automatically when we create an object of SimplePublisher.
    def __init__(self):
        # Initialize the parent Node class.
        # The node name will be "simple_publisher".
        super().__init__('simple_publisher')

        # Create a publisher.
        # Message type: String
        # Topic name: chatter
        # Queue size: 10
        self.pub_ = self.create_publisher(String, 'chatter', 10)

        # Counter variable to count how many messages have been published.
        self.counter_ = 0

        # Timer period in seconds.
        # 1.0 means the timer callback runs every 1 second.
        self.frequency_ = 1.0

        # Print information in the terminal.
        self.get_logger().info('Publishing every %.1f seconds' % self.frequency_)

        # Create a timer.
        # This calls timerCallback() every self.frequency_ seconds.
        self.timer_ = self.create_timer(self.frequency_, self.timerCallback)

    # This function is called repeatedly by the timer.
    def timerCallback(self):
        # Create a String message object.
        msg = String()

        # Store text data inside the message.
        msg.data = 'Hello ROS 2 - counter %d' % self.counter_

        # Publish the message to the "chatter" topic.
        self.pub_.publish(msg)

        # Increase the counter by 1 after every publish.
        self.counter_ += 1


def main():
    # Initialize ROS 2 communication.
    rclpy.init()

    # Create an object of the SimplePublisher node.
    simple_publisher = SimplePublisher()

    # Keep the node alive so the timer can keep running.
    rclpy.spin(simple_publisher)

    # Destroy the node after stopping.
    simple_publisher.destroy_node()

    # Shutdown ROS 2 communication.
    rclpy.shutdown()


# This makes sure main() only runs when this file is executed directly.
if __name__ == '__main__':
    main()