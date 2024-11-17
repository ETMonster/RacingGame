import pygame
import math
from car import *
from race import current_track
from constants import *

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Racing Prototype')

clock = pygame.time.Clock()

def update():
    delta_time = clock.tick(FPS) / 1000

    for car in current_track.objects.to_dictionary()['cars']:
        car.update_rotation(delta_time, current_track)
        car.update_position(delta_time, current_track)

    current_track.update_race(screen)

running = True
while running:
    screen.fill((80, 80, 80))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update()

    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, 2, 2))

    pygame.display.flip()

    pygame.time.Clock().tick(FPS)

pygame.quit()