import unittest
from .buzzer_pattern import BuzzerPattern

class TestBuzzerPattern(unittest.TestCase):
    def test_none_pattern_exists(self):
        self.assertTrue(BuzzerPattern.NONE != None)

    def test_short_pattern_exists(self):
        self.assertTrue(BuzzerPattern.SHORT != None)

    def test_long_pattern_exists(self):
        self.assertTrue(BuzzerPattern.LONG != None)

    def test_valid_buzzer_pattern(self):
        buzzer = BuzzerPattern(
            duration=999999,
            strength=100
        )

        self.assertEqual(buzzer.duration, 1000)
        self.assertEqual(buzzer.strength, 1)
