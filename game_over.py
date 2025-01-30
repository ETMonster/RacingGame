import pygame
import sys
from button import Button

pygame.init()

def get_font(size):
    return pygame.font.Font("assets/font(1).ttf", size)

def game_over_screen(screen, laps, time, position = 1):
    screen.fill((0, 0, 0))
    BG = pygame.image.load("assets/Background.png")

    while True:
        #blit backgroumd
        screen.blit(BG, (0, 0) )

        #game over text
        game_over_text=get_font(40).render("GAME OVER", True, "#b68f40")
        game_over_rect=game_over_text.get_rect(center=(400, 100))
        screen.blit(game_over_text, game_over_rect)

        #laps and time text
        laps_message="You ran %d laps!" % laps
        time_message="Your time: %.2f seconds!" % time
        postion_message= f'#{position}'


        #blitting
        laps_text=get_font(30).render(laps_message, True, "White")
        time_text=get_font(30).render(time_message, True, "White")
        position_text=get_font(80).render(postion_message, True, (255, 215, 0) if position == 1 else (192, 192, 192) if position == 2 else (206, 137, 70))

        laps_rect=laps_text.get_rect(center=(400, 200))
        time_rect=time_text.get_rect(center=(400, 275))
        position_rect=position_text.get_rect(center=(400, 400))

        screen.blit(laps_text, laps_rect)
        screen.blit(time_text, time_rect)
        screen.blit(position_text, position_rect)
        options=pygame.image.load("assets/Options Rect.png")
        pygame.transform.scale(options,(200,100))
        #buttons
        main_menu_button = Button(
            image=options,
            pos=(400, 550),
            text_input="MAIN MENU",
            font=get_font(40),
            base_color="#d7fcd4",
            hovering_color="White",
        )
        quit_image=pygame.image.load("assets/Quit Rect.png")
        pygame.transform.scale(quit_image, (200, 100))
        quit_button = Button(
            image=quit_image,
            pos=(400, 700),
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


