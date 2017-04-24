import RPi.GPIO as GPIO
from color import Color

'''
The Hardware class is set up to be used in a with statement
'''
class Hardware:
    def __enter__(
        self,
        red_pin: int = 14,
        green_pin: int = 15,
        blue_pin: int = 18,
        motor_pin: int = 23
    ):
        self.red_pin = red_pin
        self.green_pin = green_pin
        self.blue_pin = blue_pin
        self.motor_pin = motor_pin

        # set board mode to Broadcom
        # TODO I'm not sure why we do this
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(red_pin, GPIO.OUT)
        GPIO.setup(green_pin, GPIO.OUT)
        GPIO.setup(blue_pin, GPIO.OUT)
        GPIO.setup(motor_pin, GPIO.OUT)

        self.red_channel = GPIO.PWM(red_pin, 100)
        self.green_channel = GPIO.PWM(green_pin, 100)
        self.blue_channel = GPIO.PWM(blue_pin, 100)

        self.red_channel.start(0)
        self.green_channel.start(0)
        self.blue_channel.start(0)

    def __exit__(self):
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

    def run_motor(self):
        GPIO.output(motor_pin, 1)

    def stop_motor(self):
        GPIO.output(motor_pin, 0)
