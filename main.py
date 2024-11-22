import pygame
import math
from car import *
from race import current_race
from constants import *

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Racing Prototype')

clock = pygame.time.Clock()

def update():
    delta_time = clock.tick(FPS) / 1000

    for car in current_race.objects.to_dictionary()['cars']:
        car.update_rotation(delta_time, current_race)
        car.update_position(delta_time, current_race)

        if car.is_player:
            #camera.scale = math.sqrt(car.velocity.x ** 2 + car.velocity.y ** 2) / 500
            #camera.scale = max(camera.scale, MIN_CAMERA_SCALE)

            camera.update_position(car)

    current_race.update_screen(screen)

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