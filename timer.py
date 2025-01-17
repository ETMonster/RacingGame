import pygame

def update_timer(screen, start_time, color, position, font):

    #time in seconds which is current time minus start time
    time=(pygame.time.get_ticks()-start_time)/1000
    timer_text="Time: " + str(time) + "s"
    #blit the timer
    timer_surface=font.render(timer_text, True, color)
    screen.blit(timer_surface, position)


def update_laps(screen, laps, color, position, font):

    if laps!=3:
        laps_text="Lap: " + str(laps) +"/2"
        laps_surface=font.render(laps_text, True, color)
        screen.blit(laps_surface, position)
