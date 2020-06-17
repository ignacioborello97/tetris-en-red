import pygame
from buttons import text_objects, button

def instructions_screen(s_width,s_height):

    black = (0,0,0)
    silver = (128,128,128)

    screen = pygame.display.set_mode((s_width,s_height))
    pygame.display.set_caption('Instrucciones - Tetris en Red')
    screen.fill(silver)

    pygame.font.init()

    subtitleText = pygame.font.SysFont('comicsansms',int(s_width/20))
    textSurf, textRect = text_objects('Crear una partida',subtitleText)
    textRect.center = (s_width/2,s_height/15)
    screen.blit(textSurf,textRect)

    text = pygame.font.SysFont('comicsansms',int(s_width/33))
    textSurf, textRect = text_objects('Al pulsar el boton se creara una partida y obtendras el codigo',text)
    textRect.center = (s_width/2,s_height/6)
    screen.blit(textSurf,textRect)
    textSurf, textRect = text_objects('de la misma. Pasaselo a tus amigos para que jueguen contigo.',text)
    textRect.center = (s_width/2,s_height/4.3)
    screen.blit(textSurf,textRect)

    textSurf, textRect = text_objects('Unirse a una partida',subtitleText)
    textRect.center = (s_width/2,s_height/2.73)
    screen.blit(textSurf,textRect)

    textSurf, textRect = text_objects('Ingresa el codigo de la partida a la que',text)
    textRect.center = (s_width/2,s_height/2.14)
    screen.blit(textSurf,textRect)
    textSurf, textRect = text_objects('quieres unirte e ingresalo para poder jugar.',text)
    textRect.center = (s_width/2,s_height/1.88)
    screen.blit(textSurf,textRect)

    textSurf, textRect = text_objects('Jugando',subtitleText)
    textRect.center = (s_width/2,s_height/1.5)
    screen.blit(textSurf,textRect)

    textSurf, textRect = text_objects('Controla las piezas con las flechas de',text)
    textRect.center = (s_width/2,s_height/1.3)
    screen.blit(textSurf,textRect)
    textSurf, textRect = text_objects('movimiento y no dejes que toquen el limite superior.',text)
    textRect.center = (s_width/2,s_height/1.2)
    screen.blit(textSurf,textRect)

    backButton = button(screen,"<------",s_width/20,s_height/1.14,s_width/5,s_height/10,(192,192,192),(150,150,150),2)

def instructions():
    while True:

        instructions_screen(400,300)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()

        pygame.display.update()    