import pygame
import math
from itertools import combinations
from screeninfo import get_monitors

class Vector:
    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y

class Rotation:
    def __init__(self, radians = None, angle = None):
        self.radians = radians
        self.angle = angle

class Object:
    def __init__(self, image = None, position = Vector(0, 0), rotation = Rotation(0, 0), collision = False, width = None, height = None):
        self.image = pygame.image.load(image)
        self.position = position
        self.rotation = rotation
        self.collision = collision

        if width is None:
            self.width = self.image.convert_alpha().get_width() * PIXEL_TO_SCREEN_FACTOR
        else:
            self.width = width * PIXEL_TO_SCREEN_FACTOR
        if height is None:
            self.height = self.image.convert_alpha().get_height() * PIXEL_TO_SCREEN_FACTOR
        else:
            self.height = height * PIXEL_TO_SCREEN_FACTOR

        self.render_image = self.image
        self.mask = pygame.mask.from_surface(self.render_image)

    def check_collision(self, race, delta_position = None):
        offset = (-(delta_position.x + (race.map.width // 2)), -(delta_position.y + (race.map.height // 2)))

        if not self.mask.overlap(race.map.outer_polygons_mask, offset) or self.mask.overlap(race.map.inner_polygons_mask, offset):
            return True

class Obstacle(Object):
    def __init__(self, image = None, position = Vector(0, 0), rotation = Rotation(0, 0), collision = False, width = None, height = None):
        super().__init__(image, position, rotation, collision, width, height)

class Camera:
    def __init__(self, position, scale):
        self.position = Vector(position.x - WINDOW_WIDTH // 2, position.y - WINDOW_HEIGHT // 2)
        self.scale = scale

    def update_position(self, focus_object):
        self.position = Vector(focus_object.position.x - WINDOW_WIDTH // 2, focus_object.position.y - WINDOW_HEIGHT // 2)

def world_to_screen(self = None, x = None, y = None, return_tuple = False):
    if self is None:
        return (
            Vector(x if x is None else x - camera.position.x, y if y is None else y - camera.position.y)
            if not return_tuple else
            (x if x is None else x - camera.position.x, y if y is None else y - camera.position.y)
        )

    return (
        Vector(self.position.x if x is None else x - camera.position.x, self.position.y if y is None else y - camera.position.y)
        if not return_tuple else
        (self.position.x if x is None else x - camera.position.x, self.position.y if y is None else y - camera.position.y)
    )

def ellipse_points_x(center, x, y, direction, sort): #direction =-1 draw upper half direction=0 draw lower half
    coordinates = []
    for i in range(180):
        rad = direction*(math.pi /180) * i
        a = center[0] + x * math.cos(rad)
        b = center[1] + y * math.sin(rad)
        coordinates.append((a, b))
    if sort==0:
        coordinates.sort(key=lambda coordinates: coordinates[0]) #sort by increasing first index value to ensure proper segments
    if sort==1:
        coordinates.sort(key=lambda coordinates: coordinates[0], reverse=True) #sort by decreasing order
    return coordinates

def ellipse_points_y(center, x, y, direction, sort):
    coordinates = []
    for i in range(180):
        rad = 2*(math.pi / 180) * i
        a = center[0] + x * math.cos(rad)
        b = center[1] + y * math.sin(rad)

        if direction==1 and a <= center[0]: #if direction=1 then only draw left half
            coordinates.append((a, b))
        elif direction==-1 and a >= center[0]: #if direction=-1 then only draw right half
            coordinates.append((a, b))

    if sort==0:
        coordinates.sort(key=lambda coordinates: coordinates[1]) #sort by increasing y value
    if sort==1:
        coordinates.sort(key=lambda coordinates: coordinates[1], reverse=True) #sort by decreasing y value
    return coordinates

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
PIXEL_TO_SCREEN_FACTOR = 1

MOVEMENT_ZERO_MARGIN = 0.5

FPS = 60

MIN_CAMERA_SCALE = 1
camera = Camera(
    position = Vector(x = 0, y = 0),
    scale = 0.8
)
