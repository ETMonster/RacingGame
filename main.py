import pygame
import math

map_choice=3

if map_choice==1:
    from map1 import inner_points, outer_points, obstacle_points
if map_choice==2:
    from map2 import inner_points, outer_points, obstacle_points
if map_choice==3:
    from map3 import inner_points, outer_points, obstacle_points
print(outer_points)
print(inner_points)

wall_segments = []
for x in range(len(inner_points)):
    wall_segments.append((inner_points[x - 1], inner_points[x]))
for x in range(len(outer_points)):
    wall_segments.append((outer_points[x-1], outer_points[x]))
for x in obstacle_points:
    for y in range(len(x)):
        wall_segments.append((x[y-1],x[y]))


pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

TRACK_WIDTH, TRACK_HEIGHT = 8000, 8000
track_surface = pygame.Surface((TRACK_WIDTH, TRACK_HEIGHT))

#drawing track
track_surface.fill((50, 50, 50))
pygame.draw.polygon(track_surface, (255, 255, 255), outer_points)
pygame.draw.polygon(track_surface, (50, 50, 50), inner_points)
#drawing obstacles
for x in range(len(obstacle_points)):
    pygame.draw.polygon(track_surface, (0, 0, 0), obstacle_points[x])

# Ball properties
ball_color = (0, 0, 255)
ball_radius = 15
ball_pos = [200, 500]  # Starting position
ball_speed = 5

#Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ball movement with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ball_pos[1] -= ball_speed
    if keys[pygame.K_DOWN]:
        ball_pos[1] += ball_speed
    if keys[pygame.K_LEFT]:
        ball_pos[0] -= ball_speed
    if keys[pygame.K_RIGHT]:
        ball_pos[0] += ball_speed

    # Ensure ball stays within track limits
    ball_pos[0] = max(ball_radius, min(ball_pos[0], TRACK_WIDTH - ball_radius))
    ball_pos[1] = max(ball_radius, min(ball_pos[1], TRACK_HEIGHT - ball_radius))

    #camera position to follow the ball
    camera_x = ball_pos[0] - SCREEN_WIDTH // 2
    camera_y = ball_pos[1] - SCREEN_HEIGHT // 2

    #ensure camera stays within track limits
    camera_x = max(0, min(camera_x, TRACK_WIDTH - SCREEN_WIDTH))
    camera_y = max(0, min(camera_y, TRACK_HEIGHT - SCREEN_HEIGHT))

    #blit the updated screen
    screen.fill((0, 0, 0))
    screen.blit(track_surface, (-camera_x, -camera_y))

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (ball_pos[0] - camera_x, ball_pos[1] - camera_y), ball_radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
