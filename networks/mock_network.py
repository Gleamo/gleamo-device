import json
from .inetwork import INetwork
from commands.utilities import json_to_commands

THIRTY_SECONDS = 30000

'''
MockNetwork Class

This class pretends to actually poll for network requests,
but really all it does is return a 30 second set of commands
that can be polled for every 30 seconds
'''
class MockNetwork(INetwork):
    def __init__(self, endpoint, username, password):
        self.json = '''
{
    "commands": [
        {
            "duration": 10000,
            "start_offset": 0,
            "end_offset": 0,
            "color": {
                "r": 255,
                "g": 0,
                "b": 0
            },
            "buzzer_pattern": "short"
        },
        {
            "duration": 10000,
            "start_offset": 0,
            "end_offset": 0,
            "color": {
                "r": 0,
                "g": 255,
                "b": 0
            },
            "buzzer_pattern": "none"
        },
        {
            "duration": 10000,
            "start_offset": 0,
            "end_offset": 0,
            "color": {
                "r": 0,
                "g": 0,
                "b": 255
            },
            "buzzer_pattern": "none"
        }
    ]
}
'''
    def check(self):
        data = json.loads(self.json)
        return json_to_commands(data)

    def get_poll_interval(self):
        return THIRTY_SECONDS
