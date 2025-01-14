import pygame
from constants import *
import car

class Race:
    def __init__(self, screen, is_paused, friction, objects, map):
        self.screen = screen
        self.is_paused = is_paused
        self.friction = friction # <0.001 to 1 (0 = 0% blending each frame, 1 = 100% blending each frame)
        self.objects = objects
        self.map = map

    def update_screen(self, screen):
        for obj_group in self.objects.to_dictionary():
            for obj in self.objects.to_dictionary()[obj_group]:
                scaled_image = pygame.transform.scale(obj.image, (obj.width / camera.scale, obj.height / camera.scale)) # Account for camera scale function

                rotated_image = pygame.transform.rotate(scaled_image, obj.rotation.angle) # Get object image and rotate it
                rect = rotated_image.get_rect() # Get rect of rotated image

                rect.center = (world_to_screen(self = obj, x = obj.position.x).x, world_to_screen(self = obj, y = obj.position.y).y) # Set screen position in relation to camera

                obj.render_image = pygame.transform.rotate(scaled_image, -obj.rotation.angle)

                #screen.blit(obj.mask.to_surface(), rect.topleft)
                screen.blit(obj.render_image, rect.topleft) # Blit onto screen

class Map:
    def __init__(self, image, outer_points, inner_points):
        self.image = image
        self.outer_points = outer_points
        self.inner_points = inner_points

    def ellipse_points(self, center, x, y, direction, sort, rotated = False):
        # Not correct yet

        coordinates = []
        for i in range(180):
            rad = 2 * (math.pi / 180) * i
            a = center[0] + x * math.cos(rad)
            b = center[1] + y * math.sin(rad)

            if direction == 1 and a <= center[0]:  # if direction=1 then only draw left half
                coordinates.append((a, b))
            elif direction == -1 and a >= center[0]:  # if direction=-1 then only draw right half
                coordinates.append((a, b))

        if rotated =
        coordinates.sort(key=lambda coordinates: coordinates[1 if rotated else 0], reverse = sort)  # sort by decreasing y value
        return coordinates

class Race_Objects:
    def __init__(self, cars, obstacles):
        self.cars = cars
        self.obstacles = obstacles

    def to_dictionary(self):
        return {
            'cars': self.cars,
            'obstacles': self.obstacles,
        }

class Obstacle(Object):
    def __init__(self, image = None, position = Vector(0, 0), rotation = Rotation(0, 0), collision = False, width = None, height = None):
        super().__init__(image, position, rotation, collision, width, height)

current_race = None