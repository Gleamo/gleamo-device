import RPi.GPIO as GPIO
from .ihardware import IHardware
from color import Color

'''
The Hardware class is set up to be used in a with statement
'''
class Hardware(IHardware):
    def __init__(
        self
        red_pin: int = 14,
        green_pin: int = 15,
        blue_pin: int = 18,
        motor_pin: int = 2
    ):
        self.red_pin = red_pin
        self.green_pin = green_pin
        self.blue_pin = blue_pin
        self.motor_pin = motor_pin


    def __enter__(self):
        # set board mode to Broadcom (versus Board)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.red_pin, GPIO.OUT)
        GPIO.setup(self.green_pin, GPIO.OUT)
        GPIO.setup(self.blue_pin, GPIO.OUT)
        GPIO.setup(self.motor_pin, GPIO.OUT)

        self.red_channel = GPIO.PWM(self.red_pin, 100)
        self.green_channel = GPIO.PWM(self.green_pin, 100)
        self.blue_channel = GPIO.PWM(self.blue_pin, 100)
        self.motor_channel = GPIO.PWM(self.motor_pin, 0)

        self.red_channel.start(0)
        self.green_channel.start(0)
        self.blue_channel.start(0)
        self.motor_channel.start(0)
        return self;

    def __exit__(self, exec_type, exec_val, exec_tb):
        GPIO.cleanup()

    def set_color(self, color: Color):
        # Convert from 0-255 to 0-100
        rgb = [
            color.r / 255.0 * 100,
            color.g / 255.0 * 100,
            color.b / 255.0 * 100
        ]
        self.red_channel.ChangeDutyCycle(rgb[0])
        self.green_channel.ChangeDutyCycle(rgb[1])
        self.blue_channel.ChangeDutyCycle(rgb[2])

    def run_motor(self, strength: float = 1):
        self.motor_channel.ChangeDutyCycle(strength)

    def stop_motor(self):
        self.motor_channel.ChangeDutyCycle(0)
