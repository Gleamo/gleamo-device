from buzzer.buzzer_pattern import BuzzerPattern
from colors.color import Color
from utilities.clamp import clamp

'''
A command is the base object for the Gleamo hardware

A command carries the following information:
- When the command was created
- When the command should finish
- What the command should do as a sequence of events
'''
class Command:
    def __init__(
        self,
        duration: int = 0,
        start_offset: int = 0,
        end_offset: int = 0,
        color: Color = Color.no_change(),
        buzzer_pattern: BuzzerPattern = BuzzerPattern.NONE
    ):
        self.duration = clamp(duration, 0, 10000)
        self.start_offset = clamp(start_offset, 0, 10000)
        self.end_offset = clamp(end_offset, 0, 10000)
        self.color = color
        self.buzzer_pattern = buzzer_pattern

        self.start_time = 0
        self.start_color = None

    def set_start_values(self, time: int = 0, color: Color = None):
        self.start_time = max(time, 0)
        self.start_color = color

    def is_expired(self, now):
        expected_end_time = self.start_time + self.duration + self.start_offset + self.end_offset

        return expected_end_time < now
