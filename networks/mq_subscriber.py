import pika
import threading, queue as Queue
import json
from commands.utilities import json_to_commands

class MQSubscriber(threading.Thread):
    def __init__(self, endpoint, username, password, queue):
        super(MQSubscriber, self).__init__()
        self.endpoint = endpoint
        self.username = username
        self.password = password
        self.queue = queue
        self.stoprequest = threading.Event()

    def callback(self, channel, method, properties, body):
        data = json.loads(body)
        commands = json_to_commands(data);
        self.queue.put(commands, True)

    def run(self):
        while not self.stoprequest.isSet():
            try:
                credentials = pika.PlainCredentials(self.username, self.password)
                connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.endpoint, credentials=credentials))
                channel = connection.channel()
                channel.queue_declare(queue='commands')
                channel.basic_consume(
                    self.callback,
                    queue='commands',
                    no_ack=True
                )
                channel.start_consuming()
            except Queue.Empty:
                continue
            # XXX add exception handling to connection

    def join(self, timeout=None):
        self.stoprequest.set()
        super(MQSubscriber, self).join(timeout)
