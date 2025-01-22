import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
import time

class ArduinoUARTNode(Node):
    def __init__(self):
        super().__init__('arduino_uart_node')

        # Configure UART parameters
        self.serial_port = '/dev/ttyUSB0'  # Change this according to your system
        self.baud_rate = 115200
        self.serial = None

        # Create a subscriber
        self.subscription = self.create_subscription(
            String,
            'arduino_commands',
            self.command_callback,
            10
        )

        # Initialize UART connection
        try:
            self.serial = serial.Serial(
                port=self.serial_port,
                baudrate=self.baud_rate,
                timeout=1.0
            )
            self.get_logger().info(f'Connected to Arduino on {self.serial_port}')
        except serial.SerialException as e:
            self.get_logger().error(f'Failed to connect to Arduino: {str(e)}')
            return

    def command_callback(self, msg):
        """Callback function to handle incoming messages."""
        if self.serial and self.serial.is_open:
            try:
                # Add newline character for Arduino parsing
                command = msg.data + '\n'
                self.serial.write(command.encode())
                self.get_logger().info(f'Sent command to Arduino: {msg.data}')
            except serial.SerialException as e:
                self.get_logger().error(f'Failed to send command: {str(e)}')
        else:
            self.get_logger().warning('Serial port is not open')

    def __del__(self):
        """Cleanup when the node is destroyed."""
        if self.serial and self.serial.is_open:
            self.serial.close()

def main(args=None):
    rclpy.init(args=args)
    node = ArduinoUARTNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
