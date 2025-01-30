import pygame
import math
import car
import race
from car import *
from game_over import game_over_screen
from race import *
from constants import *
from maps import *
from labels import *

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Racing Prototype')
clock = pygame.time.Clock()
font = pygame.font.Font("assets/font(1).ttf", 10)

current_race = None


def update(npc_image1, npc_image2, start_time):
    player_car = None

    delta_time = clock.tick(FPS) / 1000
    current_race.objects.cars[1].update(current_race.map.wall_segments, current_race.map.inner_points,
                                        current_race.map.outer_points)
    current_race.objects.cars[2].update(current_race.map.wall_segments, current_race.map.inner_points,
                                        current_race.map.outer_points)
    if not current_race.is_paused:
        for obj_group in current_race.objects.to_dictionary():
            for obj in current_race.objects.to_dictionary()[obj_group]:
                if obj.is_player == True:
                    obj.update_attributes()

                    obj.debug([''], current_race)

        for car in current_race.objects.to_dictionary()['cars']:

            if car.is_player:
                car.update_rotation(delta_time, current_race)
                car.update_position(delta_time, current_race)

                update_lap_player(car, car.render_image.get_rect(), current_race.map.checkpoints,
                                  current_race.map.finish)
                camera.update_position(car)
                player_car = car

        car_temp = pygame.transform.rotate(npc_image1, -current_race.objects.cars[1].dir)

        current_race.update_screen(screen)

        for x in range(1, 3):
            current_race.map.checker_count(current_race.objects.cars[x])
            if current_race.map.lap_checker(current_race.objects.cars[x], current_race.total_laps):
                current_race.objects.cars[x].speed = 0
                print((pygame.time.get_ticks() - start_time) / 1000)
        if current_race.objects.cars[1].laps <= current_race.total_laps:
            npc_pos_screen = (
                (current_race.objects.cars[1].pos[0] - camera.position.x) - (current_race.map.surface.get_width() // 2),
                (current_race.objects.cars[1].pos[1] - camera.position.y) - (current_race.map.surface.get_height() // 2),
            )
            screen.blit(car_temp, npc_pos_screen)
        if current_race.objects.cars[2].laps <= current_race.total_laps:
            car_temp2 = pygame.transform.rotate(npc_image2, -current_race.objects.cars[2].dir)

            npc_pos_screen = (
                (current_race.objects.cars[2].pos[0] - camera.position.x) - (current_race.map.surface.get_width() // 2),
                (current_race.objects.cars[2].pos[1] - camera.position.y) - (current_race.map.surface.get_height() // 2),
            )
            screen.blit(car_temp2, npc_pos_screen)
        lap_label(screen, (0, 0), (255, 255, 255), font)
        update_timer(screen, start_time, (255, 0, 0), (650, 10), font)
        display_laps(screen, player_car.laps, (255, 255, 255), (10, 50), font, 'Player Car', player_car.total_laps)
        display_laps(screen, current_race.objects.cars[1].laps, (255, 255, 255), (10, 10), font,
                     current_race.objects.cars[1].name, player_car.total_laps)
        display_laps(screen, current_race.objects.cars[2].laps, (255, 255, 255), (10, 30), font,
                     current_race.objects.cars[2].name, player_car.total_laps)

        #REPLACE current_race.objects.cars[1].laps with current_race.objects.cars[0].laps
        if current_race.objects.cars[1].laps > current_race.objects.cars[0].total_laps:
            current_race.objects.cars[1].speed = 0
            current_race.objects.cars[2].speed = 0
            if current_race.map.id == 0:
                current_race.objects.cars[1].pos = [1850, 2650]
                current_race.objects.cars[2].pos = [1850, 2750]
            if current_race.map.id == 1:
                current_race.objects.cars[1].pos = [3270, 150]
                current_race.objects.cars[2].pos = [3270, 250]
            return False
        else:
            return True


def start_race(selected_map, selected_laps, selected_speed, music_on):
    global current_race

    start_time = pygame.time.get_ticks()
    if music_on:
        pygame.mixer.init()
        pygame.mixer.music.load(selected_map.music)
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1)

    # Update current_race with the selected map
    current_race = Race(
        screen=screen,
        track=selected_map,
        total_laps=selected_laps,
        is_paused=False,
        friction=0.1,
        objects=Race_Objects(
            cars=[
                car.Player(
                    image='assets/green_car.png',
                    position=Vector(x=selected_map.player_pos[0], y=selected_map.player_pos[1]),
                    rotation=Rotation(radians=selected_map.player_rotation[0], angle=selected_map.player_rotation[1]),
                    is_player=True,
                    velocity=Vector(x=0, y=0),
                    direction=Vector(x=0, y=0),
                    gas_acceleration=30,
                    brake_acceleration=150,
                    roll_acceleration=0.98,
                    skid_acceleration=0.96,
                    min_turn_radius=30,
                    turn_factor=0.7,
                    max_turn_speed=3,
                    max_speed=450,
                    collision=True,
                ),
                car.Opponent("assets/red_car.png", selected_map.npc_pos, selected_map.npc_dir, 3 + selected_speed, 6,
                             selected_map.red_bias, "Red Car", 0, 0),
                car.Opponent("assets/blue_car.png", [selected_map.npc_pos[0], selected_map.npc_pos[1] + 100],
                             selected_map.npc_dir, 3 + selected_speed, 6, selected_map.blue_bias, "Blue Car", 0, 0),
            ],
            obstacles=[],
        ),
    )

    npc_image1 = pygame.image.load("assets/red_car.png")
    npc_image1 = pygame.transform.scale(npc_image1, (30, 20))

    npc_image2 = pygame.image.load("assets/blue_car.png")
    npc_image2 = pygame.transform.scale(npc_image2, (30, 20))

    # Countdown variables
    countdown_time = pygame.time.get_ticks()
    countdown_font = pygame.font.Font("assets/font(1).ttf", 75)
    countdown_text = "3"
    start_game = False
    running = True
    while running:
        screen.fill((80, 80, 80))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        # Countdown logic
        elapsed_time = pygame.time.get_ticks() - countdown_time
        if elapsed_time < 1000:
            countdown_text = "3"
        elif elapsed_time < 2000:
            countdown_text = "2"
        elif elapsed_time < 3000:
            countdown_text = "1"
        elif elapsed_time >= 3000:
            countdown_text = ""
            start_game = True
        if countdown_text:
            countdown_surface = countdown_font.render(countdown_text, True, (255, 0, 0))
            countdown_rect = countdown_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            screen.blit(countdown_surface, countdown_rect)

        if start_game:
            if update(npc_image1, npc_image2, (start_time + 3000)):
                pass
            else:
                running = False
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    display_time = (pygame.time.get_ticks() - (start_time + 3000)) / 1000
    game_over_screen(game_over_screen(screen, current_race.objects.cars[1].laps, display_time))

    pygame.quit()
