import pygame
from constants import *
import car

class Race:
    def __init__(self, friction, objects):
        self.friction = friction # <0.001 to 1 (0 = 0% blending each frame, 1 = 100% blending each frame)
        self.objects = objects

    def update_screen(self, screen):
        for obj_group in self.objects.to_dictionary():
            for obj in self.objects.to_dictionary()[obj_group]:
                scaled_image = pygame.transform.scale(obj.image, (obj.width / camera.scale, obj.height / camera.scale)) # Account for camera scale function

                rotated_image = pygame.transform.rotate(scaled_image, obj.rotation.angle) # Get object image and rotate it
                rect = rotated_image.get_rect() # Get rect of rotated image

                rect.center = (obj.position.world_to_screen(x = obj.position.x).x, obj.position.world_to_screen(y = obj.position.y).y) # Set screen position in relation to camera

                obj.render_image = pygame.transform.rotate(scaled_image, obj.rotation.angle)

                #screen.blit(obj.mask.to_surface(), rect.topleft)
                screen.blit(obj.render_image, rect.topleft) # Blit onto screen


class Race_Objects:
    def __init__(self, cars, obstacles):
        self.cars = cars
        self.obstacles = obstacles

    def to_dictionary(self):
        return {
            'obstacles': self.obstacles,
            'cars': self.cars,
        }

class Obstacle(Object):
    def __init__(self, image = None, position = Vector(0, 0), rotation = Rotation(0, 0), collision = False, width = None, height = None):
        super().__init__(image, position, rotation, collision, width, height)

current_race = None