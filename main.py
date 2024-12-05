import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1024, 720))
pygame.display.set_caption("Menu")


BG = pygame.image.load("assets/bgenio.png")
OPTIONS_BG = pygame.image.load("assets/infogenio.png")  # Añade la imagen de fondo para opciones
BG_C = pygame.image.load("assets/play.png")

def get_font(size):  # Devuelve Press-Start-2P en el tamaño deseado
    return pygame.font.Font("assets/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG_C, (0, 0)) 

        PLAY_BACK = Button(image=None, pos=(512, 670), 
                            text_input="X", font=get_font(75), base_color="Red", hovering_color="black")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(OPTIONS_BG, (0, 0))  # Blitar la imagen de fondo de opciones

        OPTIONS_TEXT = get_font(45).render("", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(512, 600))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(512, 600), 
                            text_input="X", font=get_font(75), base_color="Red", hovering_color="Black")

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

        MENU_TEXT = get_font(100).render("", True, "Black")
        MENU_RECT = MENU_TEXT.get_rect(center=(512, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(512, 250), 
                            text_input="INICIAR", font=get_font(60), base_color="#F5C100", hovering_color="#FE368E")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(512, 400), 
                            text_input="INFO", font=get_font(60), base_color="#F5C100", hovering_color="#FE368E")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(512, 550), 
                            text_input="SALIR", font=get_font(60), base_color="#F5C100", hovering_color="#FE368E")

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
                    sys.exit()

        pygame.display.update()

main_menu()