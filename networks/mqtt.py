from .inetwork import INetwork

'''
MQTT class

This is a robust network class that provides
a connection to an endpoint. Data will be
pushed to the device. The `get_poll_interval`
is set to 1 millisecond since it has no cost
to get commands from the network
'''
class MQTT(INetwork):
    def __init__(self, endpoint):
        self.endpoint = endpoint
        # TODO create a connection

    def check(self):
        # TODO return any commands in the queue

    def get_poll_interval(self):
        return 1
