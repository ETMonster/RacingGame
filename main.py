import pygame
import math
from map1 import inner_points, outer_points
from car import trial_npc

print(outer_points)
print(inner_points)


wall_segments = []
for x in range(len(inner_points)):
    wall_segments.append((inner_points[x - 1], inner_points[x]))
for x in range(len(outer_points)):
    wall_segments.append((outer_points[x-1], outer_points[x]))


pygame.init()

#Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Track dimensions
TRACK_WIDTH, TRACK_HEIGHT = 8000, 8000
track_surface = pygame.Surface((TRACK_WIDTH, TRACK_HEIGHT))


track_surface.fill((50, 50, 50))
pygame.draw.polygon(track_surface, (255, 255, 255), outer_points)
pygame.draw.polygon(track_surface, (50, 50, 50), inner_points)

npc_image = pygame.image.load("red_car.png")
npc_image = pygame.transform.scale(npc_image, (30, 20))

#Declaring NPC car
npc_car = trial_npc("red_car.png", [1000, 400], 0, 3, 5)
npc_car.update(wall_segments, inner_points, outer_points)


#Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Camera position to follow the NPC car
    camera_x = npc_car.pos[0] - SCREEN_WIDTH // 2
    camera_y = npc_car.pos[1] - SCREEN_HEIGHT // 2

    #Ensure camera stays within track limits
    camera_x = max(0, min(camera_x, TRACK_WIDTH - SCREEN_WIDTH))
    camera_y = max(0, min(camera_y, TRACK_HEIGHT - SCREEN_HEIGHT))

    #Update NPC car position
    npc_car.update(wall_segments, inner_points, outer_points)

    #Blit the updated screen
    screen.fill((0, 0, 0))
    screen.blit(track_surface, (-camera_x, -camera_y))

    #Draw the NPC car
    car_temp = pygame.transform.rotate(npc_image, -npc_car.dir)
    screen.blit(car_temp, (npc_car.pos[0] - camera_x, npc_car.pos[1] - camera_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
