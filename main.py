import pygame
import math
from labels import update_timer, update_laps, lap_label, update_lap_player

pygame.init()

map_choice = 2
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

TRACK_WIDTH, TRACK_HEIGHT = 8000, 8000
track_surface = pygame.Surface((TRACK_WIDTH, TRACK_HEIGHT))

if map_choice == 1:
    from map1 import inner_points, outer_points, obstacle_points, npc_car2, npc_car1, checker_count, lap_checker, checkpoints, finish_line
    maptesting = pygame.image.load("map1test.png")
elif map_choice == 2:
    from map2 import inner_points, outer_points, obstacle_points, npc_car2, npc_car1, checker_count, lap_checker, checkpoints, finish_line
    maptesting = pygame.image.load("!Finalmap2.png")
elif map_choice == 3:
    from map3 import inner_points, outer_points, obstacle_points, npc_car2, npc_car1, checker_count, lap_checker, checkpoints, finish_line
    maptesting = pygame.image.load("map3test.png")

total_laps = 1

wall_segments = []
for x in range(len(inner_points)):
    wall_segments.append((inner_points[x - 1], inner_points[x]))
for x in range(len(outer_points)):
    wall_segments.append((outer_points[x - 1], outer_points[x]))
for x in obstacle_points:
    for y in range(len(x)):
        wall_segments.append((x[y - 1], x[y]))

track_surface.fill((50, 50, 50))
pygame.draw.polygon(track_surface, (255, 255, 255), outer_points)
pygame.draw.polygon(track_surface, (50, 50, 50), inner_points)

for x in range(len(obstacle_points)):
    pygame.draw.polygon(track_surface, (0, 0, 0), obstacle_points[x])

npc_image1 = pygame.image.load("red_car.png")
npc_image1 = pygame.transform.scale(npc_image1, (30, 20))
npc_car1.update(wall_segments, inner_points, outer_points)

npc_image2 = pygame.image.load("blue_car.png")
npc_image2 = pygame.transform.scale(npc_image2, (30, 20))

npc_car2.update(wall_segments, inner_points, outer_points)
npc_car_list = [npc_car1, npc_car2]

for x in checkpoints:
    pygame.draw.rect(track_surface, (0, 255, 0), x, 0)

if map_choice == 1:
    pygame.draw.polygon(track_surface, (100, 100, 100), [(280, 2250), (520, 2250), (520, 2240), (280, 2240)])
elif map_choice == 2:
    pygame.draw.polygon(track_surface, (100, 100, 100), [(2250, 110), (2260, 110), (2260, 350), (2250, 350)])
elif map_choice == 3:
    pygame.draw.polygon(track_surface, (100, 100, 100), [(1290, 3000), (1300, 3000), (1300, 3240), (1290, 3240)])

start_time = pygame.time.get_ticks()
font = pygame.font.Font("font(1).ttf", 10)

pygame.draw.rect(track_surface, (0, 255, 0), finish_line, 0)

countdown_font = pygame.font.Font("font(1).ttf", 100)
countdown_text = ""
countdown_time = pygame.time.get_ticks()
go_message_time = None
go_message_shown = False
start_game = False

camera_x = npc_car1.pos[0] - SCREEN_WIDTH // 2
camera_y = npc_car1.pos[1] - SCREEN_HEIGHT // 2

camera_lerp_speed = 0.1

running = True
clock = pygame.time.Clock()

def render_map(screen, maptesting, map_choice, camera_x, camera_y):
    if map_choice == 1:
        screen.blit(maptesting, (-camera_x, -camera_y))
    elif map_choice == 2:
        screen.blit(maptesting, (-camera_x -1000, -camera_y - 975))
    elif map_choice == 3:
        screen.blit(maptesting, (-camera_x, -camera_y))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if start_game:
        for x in npc_car_list:
            checker_count(x)
            if lap_checker(x, total_laps):
                x.speed = 0
                print((pygame.time.get_ticks() - start_time) / 1000)

        target_camera_x = npc_car1.pos[0] - SCREEN_WIDTH // 2
        target_camera_y = npc_car1.pos[1] - SCREEN_HEIGHT // 2

        camera_x += (target_camera_x - camera_x) * camera_lerp_speed
        camera_y += (target_camera_y - camera_y) * camera_lerp_speed

        camera_x = max(0, min(camera_x, TRACK_WIDTH - SCREEN_WIDTH))
        camera_y = max(0, min(camera_y, TRACK_HEIGHT - SCREEN_HEIGHT))

        npc_car1.update(wall_segments, inner_points, outer_points)
        npc_car2.update(wall_segments, inner_points, outer_points)

    screen.fill((0, 0, 0))
    screen.blit(track_surface, (-camera_x, -camera_y))

    render_map(screen, maptesting, map_choice, camera_x, camera_y)

    car_temp = pygame.transform.rotate(npc_image1, -npc_car1.dir)
    screen.blit(car_temp, (npc_car1.pos[0] - camera_x, npc_car1.pos[1] - camera_y))

    car_temp2 = pygame.transform.rotate(npc_image2, -npc_car2.dir)
    screen.blit(car_temp2, (npc_car2.pos[0] - camera_x, npc_car2.pos[1] - camera_y))

    lap_label(screen, (0, 0), (255, 255, 255), font)
    update_timer(screen, start_time, (255, 0, 0), (650, 10), font)
    for x in range(len(npc_car_list)):
        update_laps(screen, npc_car_list[x].laps, (255, 0, 0), (10, 10 + (20 * x)), font, npc_car_list[x].name, total_laps)

    if not go_message_shown:
        if pygame.time.get_ticks() - countdown_time < 1000:
            countdown_text = "3"
        elif pygame.time.get_ticks() - countdown_time < 2000:
            countdown_text = "2"
        elif pygame.time.get_ticks() - countdown_time < 3000:
            countdown_text = "1"
        elif pygame.time.get_ticks() - countdown_time >= 3000:
            countdown_text = ""
            go_message_time = pygame.time.get_ticks() + 1000
            go_message_shown = True
            start_game = True

    if countdown_text:
        countdown_surface = countdown_font.render(countdown_text, True, (255, 0, 0))
        countdown_rect = countdown_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(countdown_surface, countdown_rect)

    if go_message_shown and go_message_time is not None and pygame.time.get_ticks() < go_message_time:
        go_surface = countdown_font.render("GO!", True, (0, 255, 0))
        go_rect = go_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(go_surface, go_rect)

    if go_message_time is not None and pygame.time.get_ticks() > go_message_time:
        countdown_text = ""
        go_message_time = None
    pygame.display.update()
    clock.tick(60)
