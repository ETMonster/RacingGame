import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")
LOGO = pygame.image.load("assets/logoimagecorner.png")
LOGO = pygame.transform.scale(LOGO, (135, 135))

PAUSE_ICON = pygame.image.load("assets/PauseIcon.png")
PAUSE_ICON = pygame.transform.scale(PAUSE_ICON, (100, 30))

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def pause_menu():
    paused = True
    while paused:
        PAUSE_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill((0, 0, 0, 150))

        PAUSE_TEXT = get_font(50).render("PAUSED", True, "White")
        PAUSE_RECT = PAUSE_TEXT.get_rect(center=(640, 250))
        SCREEN.blit(PAUSE_TEXT, PAUSE_RECT)

        RESUME_BUTTON = Button(image=None, pos=(640, 350),
                               text_input="RESUME", font=get_font(75), base_color="White", hovering_color="Green")
        EXIT_BUTTON = Button(image=None, pos=(640, 460),
                             text_input="EXIT TO MAIN MENU", font=get_font(75), base_color="White", hovering_color="Green")

        for button in [RESUME_BUTTON, EXIT_BUTTON]:
            button.changeColor(PAUSE_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESUME_BUTTON.checkForInput(PAUSE_MOUSE_POS):
                    paused = False
                if EXIT_BUTTON.checkForInput(PAUSE_MOUSE_POS):
                    main_menu()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False

        pygame.display.update()

def play():
    game_running = True
    paused = False

    while game_running:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        # Draw the pause icon on the play screen if not paused
        if not paused:
            SCREEN.blit(PAUSE_ICON, (100, SCREEN.get_height() - 72))  # Position it properly on the play screen

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()  #Go back to main menu

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  #Press "P" to pause
                    paused = True

        if paused:
            pause_menu()

        pygame.display.update()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")
        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("RYAN'S RADICAL RACING!", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()

        SCREEN.blit(LOGO, (-15, SCREEN.get_height() - 110))

        pygame.display.update()

def main():
    main_menu()

if __name__ == "__main__":
    main()
