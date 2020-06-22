import pygame
from colores import *
from screens import Screen
from texts import Text
from buttons import Button
from input_boxes import InputBox
from boards import Board
from avatars import Avatar

pygame.init()

def instructions_screen():
    backButton = Button('<------',30,250,100,40,white,(200,200,200),3,main_menu_screen)
    buttons = [backButton]

    t1 = Text('Crear una partida',20,black,200,20)
    t2 = Text('Al pulsar el boton se creara una partida y obtendras el codigo',12,black,200,50)
    t3 = Text('de la misma. Pasaselo a tus amigos para que jueguen contigo.',12,black,200,70)
    t4 = Text('Unirse a una partida',20,black,200,100)
    t5 = Text('Ingresa el codigo de la partida a la que',12,black,200,130)
    t6 = Text('quieres unirte e ingresalo para poder jugar.',12,black,200,150)
    t7 = Text('Jugando',20,black,200,180)
    t8 = Text('Controla las piezas con las flechas de',12,black,200,210)
    t9 = Text('movimiento y no dejes que toquen el limite superior.',12,black,200,230)
    text = [t1,t2,t3,t4,t5,t6,t7,t8,t9]

    instructionsScreen = Screen(400,300,silver,'Instrucciones - Tetris en Red',buttons,[],text)
    instructionsScreen.run()

def about_screen():
    backButton = Button('<------',30,250,100,40,white,(200,200,200),3,main_menu_screen)
    buttons = [backButton]

    t1 = Text('Tetris en Red',60,black,200,40)
    t2 = Text('Tetricos',50,black,200,110)
    t3 = Text('Copyright © 2020-2020',20,black,200,180)
    t4 = Text('Version 1.0.0 - Build 1',20,black,200,210)
    text = [t1,t2,t3,t4]

    aboutScreen = Screen(400,700,silver,'Acerca de - Tetris en Red',buttons,[],text)
    aboutScreen.run()

def main_menu_screen():
    create_game = Button('Crear partida',200,310,400,80,bright_red,red,6)
    search_game = Button('Buscar partida',200,400,400,80,bright_green,green,6)
    instructions = Button('Instrucciones',200,490,400,80,bright_blue,blue,6,instructions_screen)
    about = Button('Configuracion',100,620,200,60,bright_yellow,yellow,6,about_screen)
    configuration = Button('Acerca de',500,620,200,60,bright_yellow,yellow,6)
    buttons = [create_game,search_game,instructions,about,configuration]

    welcomeText = Text('¡Bienvenido Nombre!',60,black,400,60)
    tetrisText = Text('Tetris en Red',120,black,400,180)
    text = [welcomeText,tetrisText]
    
    mainMenuScreen = Screen(800,700,silver,'Menu principal - Tetris en Red',buttons,[],text)
    mainMenuScreen.run()

def login_screen():
    nameInput = InputBox(300,100,200,50)
    inputs = [nameInput]
    
    loginButton = Button('Log In',300,500,200,80,red,bright_red,3,main_menu_screen)
    buttons = [loginButton]

    t = Text('Escribe tu nombre:',30,black,400,50)
    t2 = Text('Escoge tu avatar:',30,black,400,220)
    text = [t,t2]

    avatar1 = Avatar(80,300,100,100,'dragon100x100.png')
    avatar2 = Avatar(260,300,100,100,'perezoso100x100.png')
    avatar3 = Avatar(440,300,100,100,'unicornio100x100.png')
    avatar4 = Avatar(600,300,100,100,'t-rex100x100.png')
    images = [avatar1,avatar2,avatar3,avatar4]

    loginScreen = Screen(800,600,silver,'Log In - Tetris en Red',buttons,inputs,text,[],images)
    loginScreen.run()

login_screen()



def play_screen():
    t1 = Text('Nombre',40,black,125,50)
    t2 = Text('Score: 250000',30,black,125,380)
    t3 = Text('Lines: 1000',30,black,125,430)
    t4 = Text('Next',30,black,125,520)
    t5 = Text('Level 20',30,black,400,50)
    t6 = Text('Player2',20,black,675,40)
    t7 = Text('Player3',20,black,675,270)
    t8 = Text('Player4',20,black,675,490)
    t9 = Text('Score: 200000',20,black,675,60)
    t10 = Text('Score: 100000',20,black,675,290)
    t11 = Text('Score: 200250',20,black,675,510)
    text = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11]

    mainBoard = Board(250,100,30)
    p2Board = Board(635,80,8)
    p3Board = Board(635,310,8)
    p4Board = Board(635,530,8)
    boards = [mainBoard,p2Board,p3Board,p4Board]

    avatar = Avatar(75,150,100,100,'dragon100x100.png')
    avatar = [avatar]

    #dibujar pieza siguiente?

    playScreen = Screen(800,700,silver,'Tetris en Red',[],[],text,boards,avatar)
    playScreen.run()

def lobby_screen():
    backButton = Button('<------',30,510,150,60,white,(200,200,200),3,main_menu_screen)
    readyButton = Button('Ready!',267,420,267,60,green,bright_green,4)
    buttons = [backButton,readyButton]


    t1 = Text('Partida #ssad28w',60,black,400,40)
    t2 = Text('Player1',40,black,100,140)
    t3 = Text('Player2',40,black,300,140)
    t4 = Text('Player3',40,black,500,140)
    t5 = Text('Player4',40,black,700,140)
    t6 = Text('Estado: Listo',20,black,100,360)
    t7 = Text('Estado: Esperando',20,black,300,360)
    t8 = Text('Estado: Listo',20,black,500,360)
    t9 = Text('Estado: Listo',20,black,700,360)
    text = [t1,t2,t3,t4,t5,t6,t7,t8,t9]   

    avatar1 = Avatar(50,200,100,100,'dragon100x100.png')
    avatar2 = Avatar(250,200,100,100,'perezoso100x100.png')
    avatar3 = Avatar(450,200,100,100,'unicornio100x100.png')
    avatar4 = Avatar(650,200,100,100,'t-rex100x100.png')
    avatar = [avatar1,avatar2,avatar3,avatar4]

    lobbyScreen = Screen(800,600,silver,'Lobby - Tetris en Red',buttons,[],text,[],avatar)
    lobbyScreen.run()