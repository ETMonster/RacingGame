import pygame
import sys
from button import Button

pygame.init()


def get_font(size):
    return pygame.font.Font("font(1).ttf", size)


def game_over_screen(screen, laps, time):
    screen.fill((0, 0, 0))
    BG = pygame.image.load("Background.png")

    while True:
        #blit backgroumd
        screen.blit(BG, (0, 0) )

        #game over text
        game_over_text=get_font(40).render("GAME OVER", True, "#b68f40")
        game_over_rect=game_over_text.get_rect(center=(400, 100))
        screen.blit(game_over_text, game_over_rect)

        #laps and time text
        laps_message="You ran %d laps!" % (laps-1)
        time_message="Your time: %.2f seconds!" % time

        #blitting
        laps_text=get_font(30).render(laps_message, True, "White")
        time_text=get_font(30).render(time_message, True, "White")

        laps_rect=laps_text.get_rect(center=(400, 200))
        time_rect=time_text.get_rect(center=(400, 275))

        screen.blit(laps_text, laps_rect)
        screen.blit(time_text, time_rect)
        options=pygame.image.load("Options Rect.png")
        pygame.transform.scale(options,(200,100))
        #buttons
        main_menu_button = Button(
            image=options,
            pos=(400, 450),
            text_input="MAIN MENU",
            font=get_font(40),
            base_color="#d7fcd4",
            hovering_color="White",
        )
        quit_image=pygame.image.load("Quit Rect.png")
        pygame.transform.scale(quit_image, (200, 100))
        quit_button = Button(
            image=quit_image,
            pos=(400, 600),
            text_input="QUIT",
            font=get_font(40),
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
                    from menu import main_menu
                    main_menu()

                if quit_button.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


