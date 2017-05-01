import colorsys
from utilities.clamp import clamp

'''
The Color Class

Use to convert numerics to RGB, or HSL
'''
class Color:
    @staticmethod
    def no_change():
        return Color(r=-1, g=-1, b=-1)

    '''
    Convert an HLS object (that has h, l, and s keys) to an RGB Color
    object. Hue, lightness, and saturation are decimals representing
    percentages. ∃[0, 1]
    '''
    @staticmethod
    def hls_to_rgb(hls):
        rgb = colorsys.hls_to_rgb(
            clamp(hls['h'], 0, 1),
            clamp(hls['l'], 0, 1),
            clamp(hls['s'], 0, 1)
        )

        return Color(
            int(rgb[0] * 255),
            int(rgb[1] * 255),
            int(rgb[2] * 255)
        )

    def __init__(self, r: int = 0, g: int = 0, b: int = 0):
        self.r = clamp(r, -1, 255)
        self.g = clamp(g, -1, 255)
        self.b = clamp(b, -1, 255)

    def is_no_change(self):
        return (
            self.r == -1 or
            self.g == -1 or
            self.b == -1
        )

    def to_hls(self):
        hlsTuple = colorsys.rgb_to_hls(self.r / 255, self.g / 255, self.b / 255)

        hls = {}

        hls['h'] = hlsTuple[0]
        hls['l'] = hlsTuple[1]
        hls['s'] = hlsTuple[2]

        return hls
