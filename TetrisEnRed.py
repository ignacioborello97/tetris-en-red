import pygame
from client.components.entities.colors.colores import *
# #from screens import Screen
# from texts import Text
# from buttons import Button
# from input_boxes import InputBox
# from boards import Board
# from avatars import Avatar
from client.components.views.login.loginview import loginViewBuilder
from client.components.views.main_menu.main_menuview import mainmenuViewBuilder
from client.components.views.instructions.instructionview import instructionViewBuilder
from client.components.views.joingame.joingameview import joingameViewBuilder
from client.components.views.lobby.lobbyview import lobbyViewBuilder
from client.components.views.game.playview import playViewBuilder
from client.components.views.about.aboutview import aboutViewBuilder
from client.components.views.config.configview import configViewBuilder
from client_login import Client

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('original-tetris-theme-tetris-soundtrack (1).ogg')
cliente = Client()

def TetrisEnRed():
    def login():
        s.run()
        

    def menu():
        m.create(s.getName(), lobby, join, instruction, config, about, createGame)
        m.run()
        
    def instruction():
        i.create(menu)
        i.run()

    def about():
        a.create(menu)
        a.run()

    def join():
        j.create(menu, lobby, lookGame)
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

    def createPlayer():
        cliente.create_player(s.getName(), s.getAvatar())

    def createGame():
        cliente.create_game()
        cliente.add_player(cliente.get_idgame(), cliente.get_idplayer())
    
    def lookGame():
        cliente.add_player(j.get_lookGame(), cliente.get_idplayer())
    
    s = loginViewBuilder(800,600,silver,'Log In - Tetris en Red')
    s.create(menu, createPlayer)
    m = mainmenuViewBuilder(800,700,silver,'Menu principal - Tetris en Red')
    
    i = instructionViewBuilder(400,300,silver,'Instrucciones - Tetris en Red')
    
    a = aboutViewBuilder(400,300,silver,'Acerca de - Tetris en Red')
    
    j = joingameViewBuilder(400,300,silver,'Buscar partida - Tetris en Red')
   
    l = lobbyViewBuilder(800,700,silver,'Lobby - Tetris en Red')
    
    p = playViewBuilder(800,700,silver,'Tetris en Red')
    
    c = configViewBuilder(400,300,silver,'Configuracion - Tetris en Red')
    
    
    login()    
    
        
TetrisEnRed()




        

    
    
    





