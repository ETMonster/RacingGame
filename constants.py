import pygame

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

class Object:
    def __init__(self, image, width, height, position, rotation):
        self.image = image
        self.width = width
        self.height = height
        self.position = position
        self.rotation = rotation

    def get_rect(self, new_position = None):
        return pygame.Rect(self.position.x if new_position is None else new_position.x, self.position.y if new_position is None else new_position.y, self.width, self.height)

    def check_collision(self, objects, delta_position):
        for obj_group in objects.to_dictionary():
            for obj in objects.to_dictionary()[obj_group]:
                if self.get_rect(delta_position).colliderect(obj.get_rect()) and not self == obj:
                    return True
                else:
                    continue

        return False

class Camera:
    def __init__(self, position, scale):
        self.position = Vector(position.x - WINDOW_WIDTH // 2, position.y - WINDOW_HEIGHT // 2)
        self.scale = scale

    def update_position(self, focus_object):
        self.position = Vector(focus_object.position.x - WINDOW_WIDTH // 2, focus_object.position.y - WINDOW_HEIGHT // 2)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
PIXEL_TO_SCREEN_FACTOR = 3

MOVEMENT_ZERO_MARGIN = 0.5

FPS = 60

MIN_CAMERA_SCALE = 1
camera = Camera(Vector(x = 0, y = 0), 1)