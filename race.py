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
                obj_scaled_image = pygame.transform.scale(obj.image, (obj.width / camera.scale, obj.height / camera.scale)) # Account for camera scale function

                obj_rotated_image = pygame.transform.rotate(obj_scaled_image, obj.rotation.angle) # Get object image and rotate it
                obj_rect = obj_rotated_image.get_rect() # Get rect of rotated image

                obj_rect.center = (obj.position.world_to_screen(x = obj.position.x).x, obj.position.world_to_screen(y = obj.position.y).y) # Set screen position in relation to camera

                obj.render_image = pygame.transform.rotate(obj_scaled_image, obj.rotation.angle)

                screen.blit(obj.render_image, obj_rect.topleft) # Blit onto screen


class Race_Objects:
    def __init__(self, cars, obstacles):
        self.cars = cars
        self.obstacles = obstacles

    def to_dictionary(self):
        return {
            'cars': self.cars,
            'obstacles': self.obstacles
        }

class Obstacle(Object):
    def __init__(self, image, position, rotation, width = None, height = None):
        super().__init__(image, position, rotation, width, height)

current_race = None