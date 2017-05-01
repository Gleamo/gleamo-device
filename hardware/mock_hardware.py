from .ihardware import IHardware

class MockHardware(IHardware):
    def __init__(
        self,
        red_pin: int = 14,
        green_pin: int = 15,
        blue_pin: int = 18,
        motor_pin: int = 2,
        debug: bool = False
    ):
        self.red_pin = red_pin
        self.green_pin = green_pin
        self.blue_pin = blue_pin
        self.motor_pin = motor_pin
        self.debug = debug

    def __enter__(self):
        self.color_called_count = 0
        self.color_last_called_with = None
        self.motor_called_count = 0
        self.motor_stop_called_count = 0
        self.motor_state = 0;

        return self

    def __exit__(self, exec_type, exec_val, exec_tb):
        pass

    def set_color(self, color):
        if self.debug:
            print('Color(', color.r, ', ', color.g, ', ', color.b, ')')
        self.color_called_count += 1
        self.color_last_called_with = color

    def run_motor(self, strength = 1):
        self.motor_called_count += 1
        self.motor_state = strength

    def stop_motor(self):
        self.motor_stop_called_count += 1
        self.motor_state = 0
