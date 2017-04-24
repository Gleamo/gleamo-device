from .buzzer import BuzzerPattern

'''
A command is the base object for the Gleamo hardware

A command carries the following information:
- When the command was created
- When the command should finish
- What the command should do as a sequence of events
'''
class Command:
    @staticmethod
    def json_to_commands(json):
        # XXX
        return []

    def __init__(
        self,
        duration: long = 0,
        start_offset: long = 0,
        end_offset: long = 0,
        color: Color,
        buzzer_pattern: BuzzerPattern = BuzzerPattern.None
    ):
        # TODO validate duration, start_offset, and end_offset with a max value
        self.duration = duration
        self.start_offset = start_offset
        self.end_offset = end_offset
        self.color = Color
        self.buzzer_pattern = buzzer_pattern

    def set_start_time(self, time: long = 0):
        self.start_time = time

    def is_expired(self, now):
        expected_end_time = self.start_time + self.duration + self.start_offset + self.end_offset

        return expected_end_time < now
