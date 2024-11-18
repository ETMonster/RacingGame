import pygame
import math
from car import *
from race import current_track
#from race import *

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Racing Prototype')

clock = pygame.time.Clock()

def update():
    delta_time = clock.tick(FPS) / 1000

    player.update_rotation(delta_time, current_track)
    player.update_position(delta_time, current_track)
    trial_npc.update_rotation(delta_time, current_track)
    trial_npc.update_position(delta_time, current_track)


running = True
while running:
    screen.fill((116, 118, 120))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update()

    rotated_image = pygame.transform.rotate(player.image, player.rotation.angle)
    rotated_image2 = pygame.transform.rotate(trial_npc.image, trial_npc.rotation.angle)

    player_rect = rotated_image.get_rect()
    player_rect.center = (player.position.x + player.width // 2, player.position.y + player.height // 2)
    trial_npc_rect = rotated_image2.get_rect()
    trial_npc_rect.center = (trial_npc.position.x + trial_npc.width // 2,trial_npc.position.y + trial_npc.height // 2)

    screen.blit(rotated_image, player_rect.topleft)
    screen.blit(rotated_image2, trial_npc_rect.topright)


    pygame.display.flip()

    pygame.time.Clock().tick(FPS)

pygame.quit()