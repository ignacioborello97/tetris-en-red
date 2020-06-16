import pygame
from buttons import button, text_objects
from GUI_client_about import about
from GUI_client_instructions import instructions
from GUI_client_lobby import lobby

def main_menu_screen(s_width,s_height):

    red = (200,0,0)
    bright_red = (255,0,0)
    green = (0,200,0)
    bright_green = (0,255,0)
    blue = (0,0,200)
    bright_blue = (0,0,255)
    yellow = (200,200,0)
    bright_yellow = (255,255,0)
    black = (0,0,0)
    silver = (128,128,128)

    screen = pygame.display.set_mode((s_width,s_height))
    pygame.display.set_caption('Menu principal - Tetris en Red')
    screen.fill(silver)

    pygame.font.init()

    welcomeText = pygame.font.SysFont('comicsansms',int(s_width/13))
    textSurf, textRect = text_objects('¡Bienvenido Nombre!',welcomeText)
    textRect.center = (s_width/2,s_height/10)
    screen.blit(textSurf,textRect)

    titleText = pygame.font.SysFont('comicsansms',int(s_width/10))
    textSurf, textRect = text_objects('Tetris en Red',titleText)
    textRect.center = (s_width/2,s_height/4)
    screen.blit(textSurf,textRect)

    create_game = button(screen,'Crear partida',s_width/4,s_height/2.26,s_width/2,s_height/12,bright_red,red,6)
    search_game = button(screen,'Buscar partida',s_width/4,s_height/1.84,s_width/2,s_height/12,bright_green,green,6)
    instructions = button(screen,'Instrucciones',s_width/4,s_height/1.55,s_width/2,s_height/12,bright_blue,blue,6)
    about = button(screen,'Configuracion',s_width/12,s_height/1.14,s_width/4,s_height/12,bright_yellow,yellow,6)
    configuration = button(screen,'Acerca de',s_width*(11/16),s_height/1.14,s_width/4,s_height/12,bright_yellow,yellow,6)

def main_menu():
    while True:

        main_menu_screen(800,700)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()

        pygame.display.update()