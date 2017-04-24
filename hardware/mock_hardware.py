from hardware import Hardware

class MockHardware(Hardware):
    def __with__(self):
        self.color_called_count = 0
        self.color_last_called_with = null
        self.motor_called_count = 0
        self.motor_stop_called_count = 0
        self.motor_state = 0;

    def __exit__(self):
        pass

    def set_color(self, color):
        self.color_called_count++
        self.color_last_called_with = color

    def run_motor(self):
        self.motor_called_count++
        self.motor_state = 1

    def stop_motor(self):
        self.motor_stop_called_count++
        self.motor_state = 0
