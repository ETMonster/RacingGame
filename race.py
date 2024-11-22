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
                obj_image = pygame.transform.scale(obj.image, (obj.width / camera.scale, obj.height / camera.scale))

                obj_rotated_image = pygame.transform.rotate(obj_image, obj.rotation.angle) # Get object image and rotate it
                obj_rect = obj_rotated_image.get_rect() # Get rect of rotated image

                obj_rect.center = (obj.position.world_to_screen(x = obj.position.x).x, obj.position.world_to_screen(y = obj.position.y).y) # Set screen position in relation to camera

                screen.blit(pygame.transform.rotate(obj_image, obj.rotation.angle), obj_rect.topleft) # Blit onto screen


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
    def __init__(self, image, width, height, position, rotation, color = None):
        super().__init__(image, width, height, position, rotation)
        self.color = color

current_race = Race(
    friction = 0.1,
    objects = Race_Objects(
        cars = [
            car.Player(
                image = pygame.image.load('red_car.png'), # Car image path
                width = pygame.image.load('red_car.png').get_width() * PIXEL_TO_SCREEN_FACTOR, # Car width so it retains its aspect with rescale
                height = pygame.image.load('red_car.png').get_height() * PIXEL_TO_SCREEN_FACTOR, # Car height so it retains its aspect with rescale
                position = Vector(x = 0, y = 300), # Position in world
                rotation = Rotation(radians=0, angle=0),  # The current rotation of the car in radians and angles
                is_player = True,
                velocity = Vector(x = 0, y = 0), # Forward velocity (positive if moving forward from the car's point of view, negative if moving backwards from car's point of view)
                direction = Vector(x = 0, y = 0), # The direction that the car is currently moving in (-1 to 1) and multiplies by velocity to get new position
                gas_acceleration = 80, # Acceleration when pressing gas button
                brake_acceleration = 250, # Acceleration when pressing brake button
                roll_acceleration = 0.98, # Acceleration when acceleration buttons pressed
                skid_acceleration = 0.96, # Acceleration when burning out (Target direction + Travel direction > 90)
                min_turn_radius = 30,
                turn_factor = 0.5, # The rate at which cars turn
                max_turn_speed = 3, # The maximum turn speed
                max_speed = 600 # The maximum velocity
            ),
            car.Opponent(
                image=pygame.image.load('red_car.png'),  # Car image path
                width=pygame.image.load('red_car.png').get_width() * PIXEL_TO_SCREEN_FACTOR, # Car width so it retains its aspect with rescale
                height=pygame.image.load('red_car.png').get_height() * PIXEL_TO_SCREEN_FACTOR, # Car height so it retains its aspect with rescale
                position=Vector(x=0, y=0),  # Position on screen
                rotation=Rotation(radians=0, angle=0),  # The current rotation of the car in radians and angles
                is_player = False,
                velocity = Vector(x=0, y=0), # Forward velocity (positive if moving forward from the car's point of view, negative if moving backwards from car's point of view)
                direction= Vector(x=0, y=0), # The direction that the car is currently moving in (-1 to 1) and multiplies by velocity to get new position
                gas_acceleration=50,  # Acceleration when pressing gas button
                brake_acceleration=250,  # Acceleration when pressing brake button
                roll_acceleration=0.98,  # Acceleration when acceleration buttons pressed
                skid_acceleration=0.96,  # Acceleration when burning out (Target direction + Travel direction > 90)
                min_turn_radius=30,
                turn_factor=0.5,  # The rate at which cars turn
                max_turn_speed=3,  # The maximum turn speed
                max_speed=50,  # The maximum velocity
                difficulty=1
            )
        ],

        obstacles = [
            Obstacle(pygame.image.load('car.png'), 50, 50, Vector(x = -100, y = 0), Rotation(angle = 0), (255, 0, 0))
        ]
    )
)