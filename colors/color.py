import colorsys

'''
The Color Class

Use to convert numerics to RGB, or HSL
'''
class Color:
    @staticmethod
    def no_change():
        return Color(r=-1, g=-1, b=-1)

    @staticmethod
    def hls_to_rgb(hls):
        # TODO clamp hls values
        rgb = colorsys.hls_to_rgb(hls['h'], hls['l'], hls['s'])

        return Color(
            int(rgb[0] * 255),
            int(rgb[1] * 255),
            int(rgb[2] * 255)
        )

    def __init__(self, r: int = 0, g: int = 0, b: int = 0):
        # TODO clamp hls values
        self.r = r
        self.g = g
        self.b = b

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
