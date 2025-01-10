import pygame
import math
from timer import update_timer, update_laps

map_choice=1

if map_choice==1:
    from map1 import inner_points, outer_points, obstacle_points, track_width, track_height
if map_choice==2:
    from map2 import inner_points, outer_points, obstacle_points, track_width, track_height
from car import trial_npc



wall_segments = []
for x in range(len(inner_points)):
    wall_segments.append((inner_points[x - 1], inner_points[x]))
for x in range(len(outer_points)):
    wall_segments.append((outer_points[x-1], outer_points[x]))
for x in obstacle_points:
    for y in range(len(x)):
        wall_segments.append((x[y-1],x[y]))



pygame.init()

screen_width, screen_height = 800, 800
screen=pygame.display.set_mode((screen_width, screen_height))

track_surface=pygame.Surface((track_width, track_height))


#drawing track
track_surface.fill((50, 50, 50))
pygame.draw.polygon(track_surface, (255, 255, 255), outer_points)
pygame.draw.polygon(track_surface, (50, 50, 50), inner_points)
#drawing obstacles
for x in range(len(obstacle_points)):
    pygame.draw.polygon(track_surface, (0, 0, 0), obstacle_points[x])

npc_image1 = pygame.image.load("red_car.png")
npc_image1 = pygame.transform.scale(npc_image1, (30, 20))

npc_car1 = trial_npc("red_car.png", [1530, 800], 90, 3, 6, "right", "npc car1", 0,0)
npc_car1.update(wall_segments, inner_points, outer_points)

npc_image2 = pygame.image.load("blue_car.png")
npc_image2 = pygame.transform.scale(npc_image2, (30, 20))

npc_car2 = trial_npc("blue_car.png", [1680, 800], 90, 3, 6, "left", "npc car2",0,0)
npc_car2.update(wall_segments, inner_points, outer_points)
npc_car_list=[npc_car1, npc_car2]



def checker_count(car):
    if (car.pos[0]>=280 and car.pos[0]<=520) and (car.pos[1]>=600 and car.pos[1]<=610):
        car.checker=car.laps
        print(car.checker)

def lap_checker(car):
    if (car.pos[0]>=990 and car.pos[0]<1000) and (car.pos[1]>=240 and car.pos[1]<=500):
        car.laps=car.checker+1
        print(car.laps)
    if car.laps == 2:
        return True
    else:
        return False

start_time=pygame.time.get_ticks()
font=pygame.font.Font(None,24)

#Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for x in npc_car_list:
        checker_count(x)
        if lap_checker(x):
            running = False
            print((pygame.time.get_ticks()-start_time )/1000)

    #camera position to follow the NPC car
    camera_x = npc_car1.pos[0] - screen_width // 2
    camera_y = npc_car1.pos[1] - screen_height // 2

    #ensure camera stays within track limits
    camera_x = max(0, min(camera_x, track_width - screen_width))
    camera_y = max(0, min(camera_y, track_height - screen_height))

    #Update NPC car position
    npc_car1.update(wall_segments, inner_points, outer_points)
    npc_car2.update(wall_segments, inner_points, outer_points)


    #blit the updated screen
    screen.fill((0, 0, 0))
    screen.blit(track_surface, (-camera_x, -camera_y))

    #draw the NPC car
    car_temp = pygame.transform.rotate(npc_image1, -npc_car1.dir)
    screen.blit(car_temp, (npc_car1.pos[0] - camera_x, npc_car1.pos[1] - camera_y))

    car_temp2 = pygame.transform.rotate(npc_image2, -npc_car2.dir)
    screen.blit(car_temp2, (npc_car2.pos[0] - camera_x, npc_car2.pos[1] - camera_y))

    update_timer(screen,start_time, (255,0,0), (650,10), font)
    update_laps(screen, npc_car1.laps,(255,0,0), (10,10), font )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
