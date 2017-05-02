'''
INetwork Interface

Any network code should extend this interface. The scheduler
will expect any networks to behave the same
'''
class INetwork:
    def __init__(self, endpoint, username, password):
        self.endpoint = endpoint

    def check(self):
        raise NotImplementedError

    def get_poll_interval(self):
        raise NotImplementedError
