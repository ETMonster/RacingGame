import pygame
import math
from car import trial_npc


pygame.init()

WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

center = [WIDTH // 2, HEIGHT // 2]
x1, y1 = 150, 50  #dimensions for inner ellipse
x2, y2 = 250, 120  #dimensions for outer ellipse
total_points = 720

#function to calculate ellipse points
def ellipse_points(center, x, y, total_points):
    coordinates = []
    for i in range(180):
        rad = 2 * (math.pi / 180) * i
        a = center[0] + x * math.cos(rad)
        b = center[1] + y * math.sin(rad)
        coordinates.append((a, b))
    return coordinates

#generate track points
inner_points = ellipse_points(center, x1, y1, total_points)
outer_points = ellipse_points(center, x2, y2, total_points)
print(inner_points)
print(outer_points)
#create wall segments
wall_segments=[]
for x in range(len(inner_points)):
    wall_segments.append((inner_points[x - 1], inner_points[x]))
    wall_segments.append((outer_points[x-1], outer_points[x]))
print(wall_segments)

#image for car
npc_image=pygame.image.load("red_car.png")
npc_image=pygame.transform.scale(npc_image, (20,10))

#declaring npc
npc_car=trial_npc("red_car.png",[center[0], center[1] - y2 + 35], 0, 0.07, 0.5 )
npc_car.update(wall_segments, inner_points, outer_points)

screen.fill((0,0,0))

#loop for game
game_active = True
while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False


    npc_car.update(wall_segments, inner_points, outer_points)
    screen.fill((0, 0, 0))

    pygame.draw.polygon(screen, (255, 255, 255), outer_points) #drawing outer ellipse
    pygame.draw.polygon(screen, (0, 0, 0), inner_points) #drawing inner ellipse using background colour

    #blitting the car on the screen
    car_temp = pygame.transform.rotate(npc_image, -npc_car.dir)
    screen.blit(car_temp,npc_car.pos)

    pygame.display.update()

pygame.quit()

