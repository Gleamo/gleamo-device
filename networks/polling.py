import urllib
import json
from .inetwork import INetwork
from commands.utilities import json_to_commands

THREE_SECONDS = 3000

'''
Polling class

This is a simple network class that provides a simple
polling mechanism for requesting commands from an
endpoint.

This is for testing mainly, this should not be used
in production
'''
class Polling(INetwork):
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def check(self):
        urllib.request.urlopen(endpoint + 'commands')
        data = json.loads(url.read().decode())

        return json_to_commands(data);

    def get_poll_interval(self):
        return THREE_SECONDS
