from hardware.ihardware import IHardware
from commands.command import Command
from state.state import State
from buzzer.buzzer_pattern import BuzzerPattern
from colors.color import Color

def ease(current_value, next_value, now, start, end):
    return (((next_value - current_value) / (end - start)) * (now - start)) + current_value

'''
Given a `state`, a `command`, and `now`, the Dispatcher knows
how to create the next state and provide it to the `hardware_service`
'''
class Dispatcher:
    def __init__(self, hardware_service: IHardware):
        self.hardware_service = hardware_service

    def determine_color(self, start_color: Color, target_color: Color, start, end, now):
        diff_until_end = end - now
        time_diff = now - start

        if target_color.is_no_change():
            return start_color
        elif diff_until_end <= 0:
            # Weird, we took too long
            return target_color
        elif time_diff == 0:
            # Weird, no time difference yet
            return start_color
        else:
            # convert the current state color to hsl
            current_hsl = start_color.to_hls()
            # convert the current command color to hsl
            target_hsl = target_color.to_hls()
            # perform an interval between the two hsls
            next_h = ease(current_hsl['h'], target_hsl['h'], now, start, end);
            next_s = ease(current_hsl['s'], target_hsl['s'], now, start, end);
            next_l = ease(current_hsl['l'], target_hsl['l'], now, start, end);
            next_hsl = { 'h': next_h, 's': next_s, 'l': next_l }

            return Color.hls_to_rgb(next_hsl)

    def determine_buzzer(self, target_buzzer, start, end, now):
        threshold = start + target_buzzer.duration

        if now <= threshold and now <= end:
            return target_buzzer
        else:
            return BuzzerPattern.NONE

    def dispatch(self, command: Command, now: int):
        start_time = command.start_time
        end_time = command.start_time + command.duration

        next_color = self.determine_color(command.start_color, command.color, start_time, end_time, now)
        next_buzzer = self.determine_buzzer(command.buzzer_pattern, start_time, end_time, now)

        next_state = State(next_color, next_buzzer)

        self.state_to_hardware(next_state)
        return next_state

    def state_to_hardware(self, state: State):
        self.hardware_service.set_color(state.color)

        if (state.buzzer_pattern.strength > 0):
            self.hardware_service.run_motor(state.buzzer_pattern.strength)
        else:
            self.hardware_service.stop_motor()
