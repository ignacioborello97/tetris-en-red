import pygame
from buttons import text_objects, button

def about_screen(s_width,s_height):

    black = (0,0,0)
    silver = (128,128,128)

    screen = pygame.display.set_mode((s_width,s_height))
    pygame.display.set_caption('Acerca de - Tetris en Red')
    screen.fill(silver)

    pygame.font.init()

    titleText = pygame.font.SysFont('comicsansms',int(s_width/6.67))
    textSurf, textRect = text_objects('Tetris en Red',titleText)
    textRect.center = (s_width/2,s_height/8)
    screen.blit(textSurf,textRect)

    subtitleText = pygame.font.SysFont('comicsansms',int(s_width/8))
    textSurf, textRect = text_objects('Tetricos',subtitleText)
    textRect.center = (s_width/2,s_height*(3/8))
    screen.blit(textSurf,textRect)   

    text = pygame.font.SysFont('comicsansms', int(s_width/20))
    textSurf, textRect = text_objects('Copyright © 2020-2020',text)
    textRect.center = (s_width/2,s_height*(5/8))
    screen.blit(textSurf,textRect) 

    textSurf, textRect = text_objects('Version 1.0.0 - Build 1',text)
    textRect.center = (s_width/2,s_height*(3/4))
    screen.blit(textSurf,textRect)

    backButton = button(screen,"<------",s_width/20,s_height/1.14,s_width/5,s_height/10,(192,192,192),(150,150,150),2)

def about():
    while True:

        about_screen(400,300)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()

        pygame.display.update()

