class Vector:
    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y

    def screen_to_world(self):
        return Vector(self.x - camera.position.x, self.y - camera.position.y)

    def world_to_screen(self, x = None, y = None):
        return Vector(self.x if x is None else x - camera.position.x, self.y if y is None else y - camera.position.y)

class Rotation:
    def __init__(self, radians = None, angle = None):
        self.radians = radians
        self.angle = angle

class Camera:
    def __init__(self, position, scale):
        self.position = Vector(position.x - WINDOW_WIDTH // 2, position.y - WINDOW_HEIGHT // 2)
        self.scale = scale

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
PIXEL_TO_SCREEN_FACTOR = 3

MOVEMENT_ZERO_MARGIN = 0.5

FPS = 60

camera = Camera(Vector(x = 0, y = 0), 1)