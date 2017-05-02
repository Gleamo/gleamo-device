import queue as Queue
from .inetwork import INetwork
from .mq_subscriber import MQSubscriber

'''
Message Queue class

This is a robust network class that provides
a connection to an endpoint. Data will be
pushed to the device. The `get_poll_interval`
is set to 1 millisecond since it has no cost
to get commands from the network
'''
class MQ(INetwork):
    def __init__(self, endpoint, username, password):
        self.queue = Queue.Queue()
        self.subscriber = MQSubscriber(endpoint, username, password, self.queue)
        self.subscriber.start()

    def check(self):
        try:
            return self.queue.get(False)
        except Queue.Empty:
            return None

    def get_poll_interval(self):
        return 1
