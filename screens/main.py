import pygame
import sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("Background.png")
LOGO = pygame.image.load("logoimagecorner.png")
LOGO = pygame.transform.scale(LOGO, (135, 135))

PAUSE_ICON = pygame.image.load("PauseIcon.png")
PAUSE_ICON = pygame.transform.scale(PAUSE_ICON, (100, 30))


def get_font(size):
    return pygame.font.Font("font(1).ttf", size)


def map_selection_screen():
    BG=pygame.image.load("Background.png")

    #replace with map screenshots
    map1_img=pygame.image.load("logoimagecorner.png")
    map2_img=pygame.image.load("logoimagecorner.png")
    map3_img=pygame.image.load("logoimagecorner.png")

    map1_img = pygame.transform.scale(map1_img, (300, 200))
    map2_img = pygame.transform.scale(map2_img, (300, 200))
    map3_img = pygame.transform.scale(map3_img, (300, 200))

    #map buttons
    map1_button = Button(image=map1_img, pos=(440, 200), text_input="", font=get_font(50), base_color="White", hovering_color="Green")
    map2_button = Button(image=map2_img, pos=(840, 200), text_input="", font=get_font(50), base_color="White", hovering_color="Green")
    map3_button = Button(image=map3_img, pos=(640, 450), text_input="", font=get_font(50), base_color="White", hovering_color="Green")

    back_button = Button(
        image=pygame.image.load("Quit Rect.png"),
        pos=(640, 650),
        text_input="BACK",
        font=get_font(40),
        base_color="#d7fcd4",
        hovering_color="White",
    )

    while True:
        SCREEN.blit(BG, (0, 0))

        title_text = get_font(30).render("SELECT YOUR MAP", True, "#b68f40")
        title_rect = title_text.get_rect(center=(640, 50))
        SCREEN.blit(title_text, title_rect)

        mouse_pos = pygame.mouse.get_pos()

        for button in [map1_button, map2_button, map3_button]:
            button.changeColor(mouse_pos)
            pygame.draw.rect(SCREEN, "White", button.rect.inflate(10, 10), 3)
            button.update(SCREEN)

        back_button.changeColor(mouse_pos)
        back_button.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if map1_button.checkForInput(mouse_pos):
                    print("Map 1 Selected")
                     #incoporate map 1 game here
                if map2_button.checkForInput(mouse_pos):
                    print("Map 2 Selected")
                     #incoporate map 2 game here
                if map3_button.checkForInput(mouse_pos):
                    print("Map 3 Selected")
                     #incoporate map 3 game here
                if back_button.checkForInput(mouse_pos):
                    main_menu()

        pygame.display.update()

#test arguments
laps = 2
speed = 3
music_on = True
#also initialized in main just added here for clarity

def options(laps, speed, music_on):
   #arguments are player_car laps attribute. Set attribute to 2 in code mannually
   #total_laps variable in npc branch main file should also be set to 2
   #speed argument is player speed
   #music should be default on



    # Buttons
    laps_plus_button = Button(image=None, pos=(375, 325), text_input="+", font=get_font(75), base_color="White", hovering_color="Green")
    laps_minus_button = Button(image=None, pos=(275, 325), text_input="-", font=get_font(75), base_color="White", hovering_color="Green")
    speed_plus_button = Button(image=None, pos=(1000, 325), text_input="+", font=get_font(75), base_color="White", hovering_color="Green")
    speed_minus_button = Button(image=None, pos=(900, 325), text_input="-", font=get_font(75), base_color="White", hovering_color="Green")

    music_yes_button = Button(image=None, pos=(575, 450), text_input="YES", font=get_font(50), base_color="Black", hovering_color="LightGreen")
    music_no_button = Button(image=None, pos=(720, 450), text_input="NO", font=get_font(50), base_color="Black", hovering_color="LightCoral")

    back_button = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 650), text_input="BACK", font=get_font(40), base_color="#d7fcd4", hovering_color="White")

    while True:
        SCREEN.blit(BG, (0, 0))

        OPTIONS_TEXT = get_font(50).render("OPTIONS", True, "#b68f40")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 100))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        #Laps display with white background and black text
        laps_text = get_font(40).render("Laps:" + str(laps), True, "Black")
        laps_rect = pygame.Rect(200, 200, 250, 50)  # Define the rect position and size
        pygame.draw.rect(SCREEN, "White", laps_rect)  # Draw white background for the rect
        laps_text_rect = laps_text.get_rect(center=laps_rect.center)  # Center the text
        SCREEN.blit(laps_text, laps_text_rect)

        #Speed display with white background and black text
        speed_text = get_font(40).render("Speed:" + str(speed), True, "Black")
        speed_rect = pygame.Rect(800, 200, 300, 50)  # Define the rect position and size
        pygame.draw.rect(SCREEN, "White", speed_rect)  # Draw white background for the rect
        speed_text_rect = speed_text.get_rect(center=speed_rect.center)  # Center the text
        SCREEN.blit(speed_text, speed_text_rect)

        #Music label with white background and black text
        music_label_text = get_font(40).render("Music?", True, "Black")
        music_label_rect = pygame.Rect(520, 350, 250, 50)
        pygame.draw.rect(SCREEN, "White", music_label_rect)  # Draw white background for the rect
        music_label_text_rect = music_label_text.get_rect(center=music_label_rect.center)  # Center the text
        SCREEN.blit(music_label_text, music_label_text_rect)


        #music toggle
        if music_on:
            music_yes_button.base_color = "Green"
            music_no_button.base_color = "White"
        else:
            music_yes_button.base_color = "White"
            music_no_button.base_color = "Red"

        #music button interaction
        mouse_pos = pygame.mouse.get_pos()

        #checking the buttons for interaction and change their colors on click
        for button in [laps_plus_button, laps_minus_button, speed_plus_button, speed_minus_button]:
            pygame.draw.rect(SCREEN, "White", button.rect.inflate(10, 10), 3)  # Draw a white border around the button
            button.update(SCREEN)

        #Highlighting the Music buttons
        music_yes_button.changeColor(mouse_pos)
        music_no_button.changeColor(mouse_pos)
        pygame.draw.rect(SCREEN, "White", music_yes_button.rect.inflate(10, 10), 3)  # White border for Music Yes
        pygame.draw.rect(SCREEN, "White", music_no_button.rect.inflate(10, 10), 3)  # White border for Music No
        music_yes_button.update(SCREEN)
        music_no_button.update(SCREEN)


        #Highlighting the back button
        back_button.changeColor(mouse_pos)
        pygame.draw.rect(SCREEN, "White", back_button.rect.inflate(10, 10), 3)  # White border around Back button
        back_button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if laps_plus_button.checkForInput(mouse_pos) and laps < 5:
                    laps += 1
                if laps_minus_button.checkForInput(mouse_pos) and laps > 1:
                    laps -= 1
                if speed_plus_button.checkForInput(mouse_pos) and speed < 5:
                    speed += 1
                if speed_minus_button.checkForInput(mouse_pos) and speed > 1:
                    speed -= 1
                if music_yes_button.checkForInput(mouse_pos):
                    music_on = True
                if music_no_button.checkForInput(mouse_pos):
                    music_on = False
                if back_button.checkForInput(mouse_pos):
                    print(laps, speed, music_on)
                    main_menu()
                    #player car laps attribute should be set to laps
                    #total_laps (variable in npc's main module) should be set to laps as it is a variable used to decide the # of laps the npc car's drive and important for some of the labels
                    #return the state of music

                    return laps, speed, music_on

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("RYAN'S RADICAL RACING!", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Options Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(640, 550),
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
                    map_selection_screen()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    #arguments should be player_car laps
                    #player speed
                    #music_on variable
                    options(laps = 2, speed = 3, music_on = True)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()

        SCREEN.blit(LOGO, (-15, SCREEN.get_height() - 110))

        pygame.display.update()


def main():
    main_menu()


if __name__ == "__main__":
    main()
