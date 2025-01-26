import pygame
import sys
from button import Button
from main import main_menu, get_font

pygame.init()





screen = pygame.display.set_mode((1280, 720))
laps = 2
time = 123

#arguments needed
#player laps
#player time
#screen to blit on

def game_over_screen(screen, laps, time):

    BG = pygame.image.load("Background.png")

    while True:
        #blit backgroumd
        screen.blit(BG, (0, 0) )

        #game over text
        game_over_text=get_font(50).render("GAME OVER", True, "#b68f40")
        game_over_rect=game_over_text.get_rect(center=(640, 100))
        screen.blit(game_over_text, game_over_rect)

        #laps and time text
        laps_message="You ran %d laps!" % laps
        time_message="Your time: %.2f seconds!" % time

        #blitting
        laps_text=get_font(40).render(laps_message, True, "White")
        time_text=get_font(40).render(time_message, True, "White")

        laps_rect=laps_text.get_rect(center=(640, 200))
        time_rect=time_text.get_rect(center=(640, 275))

        screen.blit(laps_text, laps_rect)
        screen.blit(time_text, time_rect)

        #buttons
        main_menu_button = Button(
            image=pygame.image.load("Options Rect.png"),
            pos=(640, 400),
            text_input="MAIN MENU",
            font=get_font(50),
            base_color="#d7fcd4",
            hovering_color="White",
        )
        quit_button = Button(
            image=pygame.image.load("Quit Rect.png"),
            pos=(640, 550),
            text_input="QUIT",
            font=get_font(50),
            base_color="#d7fcd4",
            hovering_color="White",
        )

        mouse_pos=pygame.mouse.get_pos()


        for button in [main_menu_button, quit_button]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if main_menu_button.checkForInput(mouse_pos):
                   main_menu()

                if quit_button.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


game_over_screen(screen, laps, time)
