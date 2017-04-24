import unittest
from .buzzer.BuzzerPattern import NONE

class TestBuzzer(unittest.TestCase):
    def test_none_pattern_exists(self):
        self.assertTrue(NONE != null)
