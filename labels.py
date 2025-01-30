import pygame

def update_timer(screen, start_time, color, position, font):
    #time in seconds which is current time minus start time
    time=(pygame.time.get_ticks()-start_time)/1000
    timer_text="Time: " + str(time) + "s"
    #blit the timer
    timer_surface=font.render(timer_text, True, color)
    screen.blit(timer_surface, position)
    return time

def lap_label(screen, position, color, font):
    pygame.draw.rect(screen, (0, 0, 0), (position[0], position[1], 170, 100))
    pygame.draw.rect(screen, color, (position[0], position[1], 170, 100), 3)

    title_text = "Laps:"
    title_surface = font.render(title_text, True, color)
    screen.blit(title_surface, (position[0] + 10, position[1] + 10))

#for player car, laps argument should be laps attribute
#name should be "player car"
def display_laps(screen, laps, color, position, font, name, total_laps):

    if laps<=total_laps:
        car_text = name + ":" + str(laps)+"/"+str(total_laps)
        car_surface = font.render(car_text, True, color)
        screen.blit(car_surface, (position[0] , position[1] + 25))  #Display the lap count below the title
    else:
        car_text = name +":DONE"
        car_surface = font.render(car_text, True, color)
        screen.blit(car_surface, (position[0] , position[1] + 25))  #Display the lap count below the title