import unittest
import json
from .commands import Command

class TestCommand(unittest.TestCase):
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
            "buzer_pattern": "none"
        }
    ]
}
'''
        )
        pass

    def test_determines_that_a_command_has_expired(self):
        pass

    def test_determined_that_a_command_has_not_expired(self):
        pass


    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')
    #
    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)
