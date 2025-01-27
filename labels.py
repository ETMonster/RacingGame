import pygame

def update_timer(screen, start_time, color, position, font):

    #time in seconds which is current time minus start time
    time=(pygame.time.get_ticks()-start_time)/1000
    timer_text="Time: " + str(time) + "s"
    #blit the timer
    timer_surface=font.render(timer_text, True, color)
    screen.blit(timer_surface, position)



def lap_label(screen, position, color, font):

    pygame.draw.rect(screen, (0, 0, 0), (position[0], position[1], 170, 100))
    pygame.draw.rect(screen, color, (position[0], position[1], 170, 100), 3)

    title_text = "Laps:"
    title_surface = font.render(title_text, True, color)
    screen.blit(title_surface, (position[0] + 10, position[1] + 10))

def update_laps(screen, laps, color, position, font, name, total_laps):

    if laps<=total_laps:
        car_text = name + ":" + str(laps)+"/"+str(total_laps)
        car_surface = font.render(car_text, True, color)
        screen.blit(car_surface, (position[0] , position[1] + 25))  #Display the lap count below the title\
    else:
        car_text = name +":DONE"
        car_surface = font.render(car_text, True, color)
        screen.blit(car_surface, (position[0] , position[1] + 25))  #Display the lap count below the title\
#requires checkpoint attribute in player car class
#checkpoints is list of rect
#finish line is rect
def update_lap_player(car, car_rect, checkpoints, finish_line):
    last_checkpoint=0
    for x in range(len(checkpoints)):

        collide=pygame.Rect.colliderect(car_rect, checkpoints[x])
        #if they are colliding and the checkpoint hasn't been hit yet
        if collide and (x not in car.checkpoints):
            #check to see if car is passing the checkpoints in order
            if x==last_checkpoint:
                car.checkpoints.append(x)
                last_checkpoint+=1

    #if car is colliding with finish line and has went through all the checkpoints
    if pygame.Rect.colliderect(car_rect, finish_line) and (len(car.checkpoints)==len(checkpoints)):
        car.checkpoints.clear()
        car.laps+=1

    if car.laps>car.total_laps:
        return false
