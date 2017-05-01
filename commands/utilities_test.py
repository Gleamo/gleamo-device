import unittest
import json
from .utilities import json_command_to_command, json_to_commands

class TestCommandsUtilities(unittest.TestCase):
    def test_converts_command(self):
        data = json.loads(
'''
{
    "duration": 1000,
    "start_offset": 0,
    "end_offset": 0,
    "color": {
        "r": 100,
        "g": 120,
        "b": 250
    },
    "buzzer_pattern": "none"
}
'''
        )

        command = json_command_to_command(data)

        self.assertEqual(command.duration, 1000)
        self.assertEqual(command.start_offset, 0)
        self.assertEqual(command.end_offset, 0)
        self.assertEqual(command.color.r, 100)
        self.assertEqual(command.color.g, 120)
        self.assertEqual(command.color.b, 250)

    def test_converts_json_to_commands(self):
        data = json.loads(
'''
{
    "commands": [
        {
            "duration": 1000,
            "start_offset": 0,
            "end_offset": 0,
            "color": {
                "r": 100,
                "g": 120,
                "b": 250
            },
            "buzzer_pattern": "none"
        }
    ]
}
'''
        )

        commands = json_to_commands(data)

        self.assertEqual(len(commands), 1)
        self.assertEqual(commands[0].duration, 1000)
        self.assertEqual(commands[0].start_offset, 0)
        self.assertEqual(commands[0].end_offset, 0)
        self.assertEqual(commands[0].color.r, 100)
        self.assertEqual(commands[0].color.g, 120)
        self.assertEqual(commands[0].color.b, 250)

    def test_converts_custom_buzzer(self):
        data = json.loads(
'''
{
    "commands": [
        {
            "duration": 100,
            "start_offset": 0,
            "end_offset": 0,
            "color": {
                "r": 100,
                "g": 100,
                "b": 100
            },
            "buzzer_pattern": {
                "duration": 100,
                "strength": 0.1
            }
        }
    ]
}
'''
        )

        commands = json_to_commands(data)

        self.assertEqual(len(commands), 1)
        self.assertAlmostEqual(commands[0].buzzer_pattern.strength, 0.1)
        self.assertEqual(commands[0].buzzer_pattern.duration, 100)
