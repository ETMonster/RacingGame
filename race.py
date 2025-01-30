import pygame
from constants import *
import car
import maps



class Race:
    def __init__(self, screen, track, total_laps, is_paused, friction, objects):
        self.screen = screen
        self.map = track
        self.total_laps = total_laps
        self.is_paused = is_paused
        self.friction = friction # <0.001 to 1 (0 = 0% blending each frame, 1 = 100% blending each frame)
        self.objects = objects

        self.race_time = 0

    def update_screen(self, screen, debug = []):
        if self.map.image is not None:
            map_rect = pygame.Rect(
                (self.map.image.get_width() // 2) + camera.position.x,
                (self.map.image.get_height() // 2) + camera.position.y,
                WINDOW_WIDTH, WINDOW_HEIGHT
            )

            map_subsurface = self.map.image.subsurface(map_rect)
            map_rect.center = world_to_screen(
                x=camera.position.x + (WINDOW_WIDTH // 2),
                y=camera.position.y + (WINDOW_HEIGHT // 2),
                return_tuple=True
            )

            screen.blit(map_subsurface, map_rect.topleft)

        for x in debug:
            if x == 'map':
                map_rect = pygame.Rect(
                    (self.map.width // 2) + camera.position.x, (self.map.height // 2) + camera.position.y,
                    WINDOW_WIDTH, WINDOW_HEIGHT
                )

                map_subsurface = self.map.surface.subsurface(map_rect)

                map_rect.center = world_to_screen(
                    x = camera.position.x + (WINDOW_WIDTH // 2),
                    y = camera.position.y + (WINDOW_HEIGHT // 2),
                    return_tuple=True
                )

                screen.blit(map_subsurface, map_rect.topleft)

        for obj_group in self.objects.to_dictionary():
            for obj in self.objects.to_dictionary()[obj_group]:
                if obj.is_player:
                    scaled_image = pygame.transform.scale(obj.image, (obj.width / camera.scale, obj.height / camera.scale)) # Account for camera scale function

                    rotated_image = pygame.transform.rotate(scaled_image, obj.rotation.angle) # Get object image and rotate it
                    rect = rotated_image.get_rect() # Get rect of rotated image

                    rect.center = world_to_screen(x = obj.position.x, y = obj.position.y, return_tuple = True) # Set screen position in relation to camera

                    obj.render_image = pygame.transform.rotate(scaled_image, -obj.rotation.angle)

                    #screen.blit(obj.mask.to_surface(), rect.topleft)
                    screen.blit(obj.render_image, rect.topleft) # Blit onto screen


class Race_Objects:
    def __init__(self, cars, obstacles):
        self.cars = cars
        self.obstacles = obstacles

    def to_dictionary(self):
        return {
            'cars': self.cars,
            'obstacles': self.obstacles,
        }

current_race = None
