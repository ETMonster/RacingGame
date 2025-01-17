import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Pause Menu")

# Load assets
PAUSE_ICON = pygame.image.load("assets/PauseIcon.png")
PAUSE_ICON = pygame.transform.scale(PAUSE_ICON, (100, 30))
BG = pygame.image.load("assets/Background.png")
LOGO = pygame.image.load("assets/logoimagecorner.png")
LOGO = pygame.transform.scale(LOGO, (135, 135))

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
                    paused = False  # Resume the game (have not got to work yet)
                if EXIT_BUTTON.checkForInput(PAUSE_MOUSE_POS):
                    pygame.quit()
                    sys.exit()  # close the program

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False

        SCREEN.blit(LOGO, (-15, SCREEN.get_height() - 110))

        pygame.display.update()

def main():
    pause_activated = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause_activated = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # Check if the user clicked on the pause icon to trigger pause
                if PAUSE_ICON.get_rect(topleft=(10, SCREEN.get_height() - 60)).collidepoint(mouse_pos):
                    pause_activated = True

        if pause_activated:
            pause_menu()

        # Other game content would go here (for now we just display a background)
        SCREEN.blit(BG, (0, 0))

        SCREEN.blit(PAUSE_ICON, (100, SCREEN.get_height() - 72))  # Draw the resized pause icon

        pygame.display.update()

if __name__ == "__main__":
    main()
