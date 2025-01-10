import pygame

def update_timer(screen, start_time, color, position, font):

    #time in seconds which is current time minus start time
    time=(pygame.time.get_ticks()-start_time)/1000
    timer_text="Time: " + str(time) + "s"
    #blit the timer
    timer_surface=font.render(timer_text, True, color)
    screen.blit(timer_surface, position)


def update_laps(screen, laps, color, position, font):

    laps_text="Laps: " + str(laps)
    laps_surface=font.render(laps_text, True, color)
    screen.blit(laps_surface, position)
