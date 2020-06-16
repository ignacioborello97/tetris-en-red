import pygame
from buttons import text_objects, button

def lobby_screen(s_width,s_height):

    black = (0,0,0)
    silver = (128,128,128)
    green = (0,180,0)
    bright_green = (0,255,0)

    screen = pygame.display.set_mode((s_width,s_height))
    pygame.display.set_caption('Lobby - Tetris en Red')
    screen.fill(silver)

    pygame.font.init()

    titleText = pygame.font.SysFont('comicsansms',int(s_width/13.33))
    textSurf, textRect = text_objects('Partida #ssad28w',titleText)
    textRect.center = (s_width/2,s_height/15)
    screen.blit(textSurf,textRect)

    text = pygame.font.SysFont('comicsansms',int(s_width/20))
    textSurf, textRect = text_objects('Player1',text)
    textRect.center = (s_width/8,s_height*(7/30))
    screen.blit(textSurf,textRect)

    textSurf, textRect = text_objects('Player2',text)
    textRect.center = (s_width*(3/8),s_height*(7/30))
    screen.blit(textSurf,textRect)

    textSurf, textRect = text_objects('Player3',text)
    textRect.center = (s_width*(5/8),s_height*(7/30))
    screen.blit(textSurf,textRect)

    textSurf, textRect = text_objects('Player4',text)
    textRect.center = (s_width*(7/8),s_height*(7/30))
    screen.blit(textSurf,textRect)
    
    text = pygame.font.SysFont('comicsansms',int(s_width/40))
    textSurf, textRect = text_objects('Estado: Listo',text)
    textRect.center = (s_width/8,s_height*(3/5))
    screen.blit(textSurf,textRect)

    textSurf, textRect = text_objects('Estado: Esperando',text)
    textRect.center = (s_width*(3/8),s_height*(3/5))
    screen.blit(textSurf,textRect)

    textSurf, textRect = text_objects('Estado: Listo',text)
    textRect.center = (s_width*(5/8),s_height*(3/5))
    screen.blit(textSurf,textRect)

    textSurf, textRect = text_objects('Estado: Listo',text)
    textRect.center = (s_width*(7/8),s_height*(3/5))
    screen.blit(textSurf,textRect)

    p1avatarRect = pygame.draw.rect(screen,(black),(s_width/16,s_height*(11/30),s_width/8,s_height/6),4)

    p2avatarRect = pygame.draw.rect(screen,(black),(s_width/3.2,s_height*(11/30),s_width/8,s_height/6),4)

    p3avatarRect = pygame.draw.rect(screen,(black),(s_width/1.778,s_height*(11/30),s_width/8,s_height/6),4)

    p4avatarRect = pygame.draw.rect(screen,(black),(s_width/1.23,s_height*(11/30),s_width/8,s_height/6),4)

    readyButton = button(screen, 'Ready!',s_width/3,s_height*(2/3),s_width/3,s_height/10,green,bright_green,4)

    backButton = button(screen,"<--------",s_width/16,s_height*(53/60),s_width/6.667,s_height/15,(192,192,192),(150,150,150),2)

def lobby():
    while True:

        lobby_screen(800,600)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()

        pygame.display.update()