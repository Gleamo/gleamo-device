import unittest
from .clamp import clamp

class TestClamp(unittest.TestCase):
    def test_does_not_change_valid_values(self):
        value = 1
        after = clamp(value, 0, 2)
        self.assertEqual(value, after)

    def test_does_clamp_value_if_too_big(self):
        value = 1
        after = clamp(value, 0, 0.5)
        self.assertEqual(0.5, after)

    def test_does_clamp_value_if_too_small(self):
        value = -1
        after = clamp(value, 0, 0.5)
        self.assertEqual(0, after)
