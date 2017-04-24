import urllib
import json
import Command from command

TEN_SECONDS = 10000

# The goal here is to do polling for now,
# but to switch to eventsource in the future
# aka, long polling
class Polling:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def set_scheduler(self, scheduler):
        self.scheduler = scheduler

    def check(self):
        urllib.request.urlopen(endpoint + 'commands')
        data = json.loads(url.read().decode())

        return Command.json_to_commands(data);

    def get_poll_interval(self):
        # TODO make this computed based on the last time
        # we received data (sort of a backoff algorithm
        # like... reno?)
        return TEN_SECONDS
