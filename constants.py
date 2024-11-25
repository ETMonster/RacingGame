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
    def __init__(self, image = None, position = Vector(0, 0), rotation = Rotation(0, 0), collision = False, width = None, height = None):
        self.image = image
        self.position = position
        self.rotation = rotation
        self.collision = collision

        if width is None:
            self.width = image.convert_alpha().get_width() * PIXEL_TO_SCREEN_FACTOR
        else:
            self.width = image.convert_alpha().get_width() * width * PIXEL_TO_SCREEN_FACTOR
        if height is None:
            self.height = image.convert_alpha().get_height() * PIXEL_TO_SCREEN_FACTOR
        else:
            self.height = image.convert_alpha().get_height() * height * PIXEL_TO_SCREEN_FACTOR

        self.render_image = image
        self.mask = pygame.mask.from_surface(self.render_image)

    def check_collision(self, objects, delta_position = None):
        for obj_group in objects.to_dictionary():
            for obj in objects.to_dictionary()[obj_group]:
                if obj == self or not obj.collision or not self.collision: # Makes sure to not check for collision on self or obj that doesn't collide
                    continue

                obj.mask = pygame.mask.from_surface(obj.render_image)

                if delta_position is not None:
                    offset = (delta_position.x - obj.position.x, delta_position.y - obj.position.y)
                else:
                    offset = (self.position.x - obj.position.x, self.position.y - obj.position.y)

                if self.mask.overlap(obj.mask, offset): # Compares object masks with offsets for pixel perfect collision
                    return True

        return False

class Camera:
    def __init__(self, position, scale):
        self.position = Vector(position.x - WINDOW_WIDTH // 2, position.y - WINDOW_HEIGHT // 2)
        self.scale = scale

    def update_position(self, focus_object):
        self.position = Vector(focus_object.position.x - WINDOW_WIDTH // 2, focus_object.position.y - WINDOW_HEIGHT // 2)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
PIXEL_TO_SCREEN_FACTOR = 2.5

MOVEMENT_ZERO_MARGIN = 0.5

FPS = 60

MIN_CAMERA_SCALE = 1
camera = Camera(Vector(x = 0, y = 0), 1)