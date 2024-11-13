class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rotation:
    def __init__(self, radians, angle):
        self.radians = radians
        self.angle = angle


WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
PIXEL_TO_SCREEN_FACTOR = 2

MOVEMENT_ZERO_MARGIN = 0.5

FPS = 60