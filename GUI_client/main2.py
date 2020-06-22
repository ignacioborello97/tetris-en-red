import pygame
from colores import *
from screens import Screen
from texts import Text
from buttons import Button
from input_boxes import InputBox
from boards import Board
from avatars import Avatar
from loginview import loginViewBuilder
from main_menuview import mainmenuViewBuilder
from instructionview import instructionViewBuilder
from joingameview import joingameViewBuilder
from lobbyview import lobbyViewBuilder
from playview import playViewBuilder
from aboutview import aboutViewBuilder
from configview import configViewBuilder

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('original-tetris-theme-tetris-soundtrack (1).ogg')

def TetrisEnRed():
    def login():
        s.run()

    def menu():
        m.create(s.getName(),lobby,join,instruction,config,about)
        m.run()
        
    def instruction():
        i.create(menu)
        i.run()

    def about():
        a.create(menu)
        a.run()

    def join():
        j.create(menu)
        j.run()

    def lobby():
        l.create(s.getAvatar(),menu,play)
        l.run()

    def play():
        p.create(s.getAvatar())
        p.run()
    
    def config():
        c.create(menu,musicOn,musicOff)
        c.run()

    def musicOn():
        pygame.mixer.music.play(100)

    def musicOff():
        pygame.mixer.music.stop()
    
    s = loginViewBuilder(800,600,silver,'Log In - Tetris en Red')
    s.create(menu)
    m = mainmenuViewBuilder(800,700,silver,'Menu principal - Tetris en Red')
    
    i = instructionViewBuilder(400,300,silver,'Instrucciones - Tetris en Red')
    
    a = aboutViewBuilder(400,300,silver,'Acerca de - Tetris en Red')
    
    j = joingameViewBuilder(400,300,silver,'Buscar partida - Tetris en Red')
   
    l = lobbyViewBuilder(800,700,silver,'Lobby - Tetris en Red')
    
    p = playViewBuilder(800,700,silver,'Tetris en Red')
    
    c = configViewBuilder(400,300,silver,'Configuracion - Tetris en Red')
    
    
    login()    
    
        
TetrisEnRed()




        

    
    
    





