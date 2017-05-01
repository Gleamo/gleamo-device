import unittest
from .mock_network import MockNetwork

FAKE_ENDPOINT = 'test.com'

class TestMockNetwork(unittest.TestCase):
    def test_converts_data_to_commands(self):
        network = MockNetwork(FAKE_ENDPOINT)

        commands = network.check()

        self.assertEqual(len(commands), 3)
