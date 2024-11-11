import pygame
import math
from car import *
#from race import *

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Racing Prototype')

clock = pygame.time.Clock()

def update():
    delta_time = clock.tick(FPS) / 1000

    player.update_rotation(delta_time)
    player.update_position(delta_time)

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update()

    rotated_image = pygame.transform.rotate(player.image, player.rotation.angle)

    player_rect = rotated_image.get_rect()
    player_rect.center = (player.position.x + player.width // 2, player.position.y + player.height // 2)

    screen.blit(rotated_image, player_rect.topleft)

    pygame.display.flip()

    pygame.time.Clock().tick(FPS)

pygame.quit()