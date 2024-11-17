import pygame
from constants import *
import car

class Race:
    def __init__(self, friction, objects):
        self.friction = friction # <0.001 to 1 (0 = 0% blending each frame, 1 = 100% blending each frame)
        self.objects = objects

    def update_race(self, screen):
        for object_group in self.objects.to_dictionary():
            for obj in self.objects.to_dictionary()[object_group]:
                obj_rotated_image = pygame.transform.rotate(obj.image, obj.rotation.angle) # Get object image and rotate it
                obj_rect = obj_rotated_image.get_rect() # Get rect of rotated image

                obj_rect.center = (obj.position.world_to_screen(x = obj.position.x).x, obj.position.world_to_screen(y = obj.position.y).y) # Set screen position in relation to camera

                screen.blit(pygame.transform.rotate(obj.image, obj.rotation.angle), obj_rect.topleft) # Blit onto screen


class Race_Objects:
    def __init__(self, cars, obstacles):
        self.cars = cars
        self.obstacles = obstacles

    def to_dictionary(self):
        return {
            'cars': self.cars,
            'obstacles': self.obstacles
        }

class Obstacle:
    def __init__(self, image, position, rotation, width, height, color = None, rect = None):
        self.image = image
        self.position = position
        self.rotation = rotation
        self.width = width
        self.height = height
        self.color = color
        self.rect = rect

        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def get_rect(self):
        self.rect = pygame.Rect(self.position.x, self.position.y, self.width, self.height)

    def create_obstacle(self):
        pass

    def destroy_obstacle(self):
        pass

current_track = Race(
    0.05,
    Race_Objects(
        cars = [
            car.Player(
                image = pygame.image.load('red_car.png'), # Car image path
                width = pygame.image.load('red_car.png').get_width() * PIXEL_TO_SCREEN_FACTOR, # Car width so it retains its aspect with rescale
                height = pygame.image.load('red_car.png').get_height() * PIXEL_TO_SCREEN_FACTOR, # Car height so it retains its aspect with rescale
                position = Vector(x = 0, y = 0), # Position in world
                velocity = Vector(x = 0, y = 0), # Forward velocity (positive if moving forward from the car's point of view, negative if moving backwards from car's point of view)
                direction = Vector(x = 0, y = 0), # The direction that the car is currently moving in (-1 to 1) and multiplies by velocity to get new position
                rotation = Rotation(radians = 0, angle = 0), # The current rotation of the car in radians and angles
                gas_acceleration = 80, # Acceleration when pressing gas button
                brake_acceleration = 250, # Acceleration when pressing brake button
                roll_acceleration = 0.98, # Acceleration when acceleration buttons pressed
                skid_acceleration = 0.96, # Acceleration when burning out (Target direction + Travel direction > 90)
                min_turn_radius = 30,
                turn_factor = 0.5, # The rate at which cars turn
                max_turn_speed = 3, # The maximum turn speed
                max_speed = 600 # The maximum velocity
            )
        ],

        obstacles = [
            Obstacle(pygame.image.load('car.png'), Vector(x = 0, y = 0), Rotation(angle = 0), 50, 50, (255, 0, 0))
        ]
    )
)