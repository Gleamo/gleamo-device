from .utilities import clamp

'''
The BuzzerPattern Class

Contains information on different buzzer types

@param int duration – how long in milliseconds to make the buzzer buzz
@param float strength – how hard to spin the buzzer: ∃[0, 1]
'''
class BuzzerPattern:
    def __init__(
        self,
        duration: int = 0,
        strength: float = 1
    ):
        self.duration = clamp(duration, 0, 1000)
        self.strength = strength

BuzzerPattern.NONE = BuzzerPattern(0)
BuzzerPattern.SHORT = BuzzerPattern(1)
BuzzerPattern.LONG = BuzzerPattern(2)
