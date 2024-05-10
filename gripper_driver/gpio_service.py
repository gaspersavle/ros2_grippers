from std_srvs.srv import SetBool
import rclpy
from rclpy.node import Node
import RPi.GPIO as GPIO

GPIO_PIN_L_a = 14
GPIO_PIN_L_b = 15
GPIO_PIN_R_a = 2
GPIO_PIN_R_b = 3

SERVICE_NAME_LEFT="gripper_left"
SERVICE_NAME_RIGHT="gripper_right"

class GPIOControlNode(Node):
    def __init__(self):
        super().__init__('gpio_control_node')
        self.service_left= self.create_service(SetBool, SERVICE_NAME_LEFT, self.gpio_control_callback_L)
        self.service_right = self.create_service(SetBool, SERVICE_NAME_RIGHT, self.gpio_control_callback_R)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIO_PIN_L_a, GPIO.OUT)
        GPIO.setup(GPIO_PIN_L_b, GPIO.OUT)
        GPIO.setup(GPIO_PIN_R_a, GPIO.OUT)
        GPIO.setup(GPIO_PIN_R_b, GPIO.OUT)

    def gpio_control_callback_L(self, request, response):
        if request.data:
            GPIO.output(GPIO_PIN_L_a, GPIO.LOW)
            GPIO.output(GPIO_PIN_L_b, GPIO.HIGH)
            response.success = True
            response.message = f"L gripper OPENED"
        else:
            GPIO.output(GPIO_PIN_L_a, GPIO.HIGH)
            GPIO.output(GPIO_PIN_L_b, GPIO.LOW)
            response.success = True
            response.message = f"L gripper CLOSED"
        return response

    def gpio_control_callback_R(self, request, response):
        if request.data:
            GPIO.output(GPIO_PIN_R_a, GPIO.LOW)
            GPIO.output(GPIO_PIN_R_b, GPIO.HIGH)
            response.success = True
            response.message = f"R gripper OPENED"
        else:
            GPIO.output(GPIO_PIN_R_a, GPIO.HIGH)
            GPIO.output(GPIO_PIN_R_b, GPIO.LOW)
            response.success = True
            response.message = f"R gripper CLOSED"
        return response
def main(args=None):
    rclpy.init()
    gpio_control_node = GPIOControlNode()
    rclpy.spin(gpio_control_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
