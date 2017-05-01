import unittest
from .dispatcher import Dispatcher
from hardware.mock_hardware import MockHardware
from colors.color import Color
from buzzer.buzzer_pattern import BuzzerPattern
from commands.command import Command
from state.state import State

class TestDispatcher(unittest.TestCase):
    def test_dispatches_to_hardware(self):
        with MockHardware() as hardware_service:
            dispatcher = Dispatcher(hardware_service)

            current_state = State(
              color=Color(100, 100, 100),
              buzzer_pattern=BuzzerPattern.NONE
            )

            command = Command(
              color=Color(110, 110, 110),
              duration=100,
              buzzer_pattern=BuzzerPattern.NONE
            )

            now = 0

            next_state = dispatcher.dispatch(current_state, command, now)

            self.assertEqual(next_state.color.r, 100)
            self.assertEqual(next_state.color.g, 100)
            self.assertEqual(next_state.color.b, 100)
            self.assertEqual(hardware_service.color_last_called_with.r, 100)
            self.assertEqual(hardware_service.color_last_called_with.g, 100)
            self.assertEqual(hardware_service.color_last_called_with.b, 100)
            self.assertEqual(hardware_service.color_called_count, 1)

            now = 10

            next_state = dispatcher.dispatch(next_state, command, now)

            self.assertEqual(next_state.color.r, 101)
            self.assertEqual(next_state.color.g, 101)
            self.assertEqual(next_state.color.b, 101)
            self.assertEqual(hardware_service.color_last_called_with.r, 101)
            self.assertEqual(hardware_service.color_last_called_with.g, 101)
            self.assertEqual(hardware_service.color_last_called_with.b, 101)
            self.assertEqual(hardware_service.color_called_count, 2)

            now = 90

            next_state = dispatcher.dispatch(next_state, command, now)

            self.assertEqual(next_state.color.r, 109)
            self.assertEqual(next_state.color.g, 109)
            self.assertEqual(next_state.color.b, 109)
            self.assertEqual(hardware_service.color_last_called_with.r, 109)
            self.assertEqual(hardware_service.color_last_called_with.g, 109)
            self.assertEqual(hardware_service.color_last_called_with.b, 109)
            self.assertEqual(hardware_service.color_called_count, 3)

            now = 100

            next_state = dispatcher.dispatch(next_state, command, now)

            self.assertEqual(next_state.color.r, 110)
            self.assertEqual(next_state.color.g, 110)
            self.assertEqual(next_state.color.b, 110)
            self.assertEqual(hardware_service.color_last_called_with.r, 110)
            self.assertEqual(hardware_service.color_last_called_with.g, 110)
            self.assertEqual(hardware_service.color_last_called_with.b, 110)
            self.assertEqual(hardware_service.color_called_count, 4)

    def test_dispatches_to_hardware_with_buzzer(self):
        with MockHardware() as hardware_service:
            dispatcher = Dispatcher(hardware_service)

            current_state = State(
              color=Color(100, 100, 100),
              buzzer_pattern=BuzzerPattern.NONE
            )

            command = Command(
              color=Color.no_change(),
              duration=100,
              buzzer_pattern=BuzzerPattern(duration=10, strength=1)
            )

            now = 0

            next_state = dispatcher.dispatch(current_state, command, now)

            self.assertEqual(next_state.color.r, 100)
            self.assertEqual(next_state.color.g, 100)
            self.assertEqual(next_state.color.b, 100)
            self.assertEqual(next_state.buzzer_pattern.strength, 1)
            self.assertEqual(hardware_service.motor_called_count, 1)
            self.assertEqual(hardware_service.motor_state, 1)

            now = 10

            next_state = dispatcher.dispatch(next_state, command, now)

            self.assertEqual(next_state.color.r, 100)
            self.assertEqual(next_state.color.g, 100)
            self.assertEqual(next_state.color.b, 100)
            self.assertEqual(next_state.buzzer_pattern.strength, 1)
            self.assertEqual(hardware_service.motor_called_count, 2)
            self.assertEqual(hardware_service.motor_state, 1)

            now = 90

            next_state = dispatcher.dispatch(next_state, command, now)

            self.assertEqual(next_state.color.r, 100)
            self.assertEqual(next_state.color.g, 100)
            self.assertEqual(next_state.color.b, 100)
            self.assertEqual(next_state.buzzer_pattern.strength, 0)
            self.assertEqual(hardware_service.motor_stop_called_count, 1)
            self.assertEqual(hardware_service.motor_state, 0)
