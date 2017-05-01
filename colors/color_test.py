import unittest
from .color import Color

class TestColorMethods(unittest.TestCase):

    def test_creates_a_no_change_color(self):
        color = Color.no_change()
        self.assertTrue(color.is_no_change())

    def test_converts_rgb_to_hls(self):
        color = Color(200, 18, 19)
        hls = color.to_hls()

        # Large delta because Python sucks :/
        self.assertAlmostEqual(hls['h'], 1, delta=0.01)
        self.assertAlmostEqual(hls['l'], 0.43, delta=0.01)
        self.assertAlmostEqual(hls['s'], 0.83, delta=0.01)

    def test_converts_hls_to_color(self):
        hls = {
            'h': 120/360,
            'l': .5,
            's': 1
        }
        color = Color.hls_to_rgb(hls)

        self.assertEqual(color.r, 0)
        self.assertEqual(color.g, 255)
        self.assertEqual(color.b, 0)

    def test_converts_bad_hls_values(self):
        hls = {
            'h': 100,
            'l': 12,
            's': 1.1
        }
        color = Color.hls_to_rgb(hls)

        self.assertEqual(color.r, 255)
        self.assertEqual(color.g, 255)
        self.assertEqual(color.b, 255)

    def test_creates_colors(self):
        color = Color(100, 100, 100)
        color2  = Color(1000, 1000, 1000)

        self.assertEqual(color.r, 100)
        self.assertEqual(color.g, 100)
        self.assertEqual(color.b, 100)

        self.assertEqual(color2.r, 255)
        self.assertEqual(color2.g, 255)
        self.assertEqual(color2.b, 255)
