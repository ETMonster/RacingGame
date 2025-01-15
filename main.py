import pygame
import math
from car import *
from race import *
from constants import *
from maps import *

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Racing Prototype')

clock = pygame.time.Clock()

current_race = Race(
    screen = screen,
    track = maps[0],
    is_paused = False,
    friction = 0.1,
    objects = Race_Objects(
        cars = [
            car.Player(
                image = pygame.image.load('red_car.png').convert_alpha(), # Car image path
                position = Vector(x = 0, y = 0), # Position in world
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
                max_speed = 600, # The maximum velocity
                collision = True, # Collision
            ),
            car.Opponent(
                image=pygame.image.load('red_car.png').convert_alpha(),  # Car image path
                position=Vector(x=0, y=100),  # Position on screen
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
                collision = True,
            )
        ],

        obstacles = [
            Obstacle(
                image=pygame.image.load('obstacle.png').convert_alpha(),
                position=Vector(x = -100, y = 0),
                rotation=Rotation(radians = 0, angle = 0),
                collision=True,
            ),
        ]
    )
)

def update():
    delta_time = clock.tick(FPS) / 1000

    if not current_race.is_paused:
        for obj_group in current_race.objects.to_dictionary():
            for obj in current_race.objects.to_dictionary()[obj_group]:
                obj.update_attributes()

        for car in current_race.objects.to_dictionary()['cars']:
            car.update_rotation(delta_time, current_race)
            car.update_position(delta_time, current_race)

            if car.is_player:
                camera.update_position(car)

    current_race.update_screen(screen)
    debug(['track'], current_race)

running = True
while running:
    screen.fill((80, 80, 80))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update()

    pygame.display.flip()

    pygame.time.Clock().tick(FPS)

pygame.quit()