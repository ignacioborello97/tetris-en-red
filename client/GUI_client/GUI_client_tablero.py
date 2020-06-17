import pygame
from buttons import text_objects
from matriz import draw_playboard, matriz 

def board_screen(s_width,s_height):
    play_width = s_width*(3/8)
    play_height = s_height*(6/7)
    block_size = play_width/10
    other_play_width = s_width/10
    other_play_height = s_height/4.375
    other_block_size = other_play_width/10
    yellow = (250,250,0)
    silver = (128,128,128)
    black = (0,0,0)
    matriz_server = matriz

    screen = pygame.display.set_mode((s_width,s_height))
    pygame.display.set_caption('Tetris en Red')
    screen.fill(silver)
    pygame.font.init()

    nameText = pygame.font.SysFont('comicsansms',int(s_width/30))
    textSurf, textRect = text_objects('Nombre',nameText)
    textRect.center = (s_width/6.4,s_height/14)
    screen.blit(textSurf,textRect)

    text = pygame.font.SysFont('comicsansms',int(s_width/26.67))
    textSurf, textRect = text_objects('Score: 250000',text)
    textRect.center = (s_width/6.4,s_height/1.842)
    screen.blit(textSurf,textRect)
    
    textSurf, textRect = text_objects('Lines: 1000',text)
    textRect.center = (s_width/6.4,s_height/1.628)
    screen.blit(textSurf,textRect)
    
    textSurf, textRect = text_objects('Next',text)
    textRect.center = (s_width/6.4,s_height/1.346)
    screen.blit(textSurf,textRect)
    
    textSurf, textRect = text_objects('Level: 20',text)
    textRect.center = (s_width/2,s_height/14)
    screen.blit(textSurf,textRect)

    text = pygame.font.SysFont('comicsansms',int(s_width/40))
    textSurf, textRect = text_objects('Player2',text)
    textRect.center = (s_width/1.185,s_height/17.5)
    screen.blit(textSurf,textRect)
    textSurf, textRect = text_objects('Score: 200000',text)
    textRect.center = (s_width/1.185,s_height*(3/35))
    screen.blit(textSurf,textRect)
    
    textSurf, textRect = text_objects('Player3',text)
    textRect.center = (s_width/1.185,s_height*(27/70))
    screen.blit(textSurf,textRect)
    textSurf, textRect = text_objects('Score: 202000',text)
    textRect.center = (s_width/1.185,s_height*(29/70))
    screen.blit(textSurf,textRect)
    
    textSurf, textRect = text_objects('Player4',text)
    textRect.center = (s_width/1.185,s_height*(7/10))
    screen.blit(textSurf,textRect)
    textSurf, textRect = text_objects('Score: 102000',text)
    textRect.center = (s_width/1.185,s_height*(51/70))
    screen.blit(textSurf,textRect)

    avatarRect = pygame.draw.rect(screen,yellow,(s_width/16,s_height/7,s_width/5.333,s_height/3.5),6)

    nextpieceRect = pygame.draw.rect(screen,yellow,(s_width/16,s_height*(11/14),s_width/5.333,s_height*(3/14)),6)

    boardRect = pygame.draw.rect(screen,yellow,((s_width-play_width)/2,(s_height-play_height),play_width,play_height),6)
    draw_playboard(screen,matriz_server,(s_width-play_width)/2,(s_height-play_height),block_size)

    p2boardRect = pygame.draw.rect(screen,yellow,(s_width/1.26,s_height/8.75,other_play_width,other_play_height),4)
    draw_playboard(screen,matriz_server,s_width/1.26,s_height/8.75,other_block_size)

    p3boardRect = pygame.draw.rect(screen,yellow,(s_width/1.26,s_height*(31/70),other_play_width,other_play_height),4)
    draw_playboard(screen,matriz_server,s_width/1.26,s_height*(31/70),other_block_size)

    p4boardRect = pygame.draw.rect(screen,yellow,(s_width/1.26,s_height*(53/70),other_play_width,other_play_height),4)
    draw_playboard(screen,matriz_server,s_width/1.26,s_height*(53/70),other_block_size)


def play_board():
    while True:

        board_screen(800,700)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()

        pygame.display.update()