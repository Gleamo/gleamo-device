import unittest
import json
from .command import Command

class TestCommand(unittest.TestCase):
    def test_creates_with_clamped_values(self):
        command = Command(
            duration=9999999,
            start_offset=999999,
            end_offset=999999
        )

        self.assertEqual(command.duration, 10000)
        self.assertEqual(command.start_offset, 10000)
        self.assertEqual(command.end_offset, 10000)

    def test_determines_that_a_command_has_expired(self):
        command = Command(
            duration=100
        )

        command.set_start_time(0)

        self.assertFalse(command.is_expired(0))
        self.assertFalse(command.is_expired(99))
        self.assertFalse(command.is_expired(100))
        self.assertTrue(command.is_expired(101))
        self.assertTrue(command.is_expired(100000))
