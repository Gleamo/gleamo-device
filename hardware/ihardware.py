'''
The IHardware Class
'''
class IHardware:
    def __enter__(self):
        return self

    def __exit__(self, exec_type, exec_val, exec_tb):
        pass

    def set_color(self, color):
        pass

    def run_motor(self, strength):
        pass

    def stop_motor(self):
        pass
