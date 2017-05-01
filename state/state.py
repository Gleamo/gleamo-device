from colors.color import Color
from buzzer.buzzer_pattern import BuzzerPattern

class State:
    def __init__(self, color: Color, buzzer_pattern: BuzzerPattern):
        self.color = color
        self.buzzer_pattern = buzzer_pattern
