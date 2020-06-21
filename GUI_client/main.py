import pygame
from colores import *
from screens import Screen
from texts import Text
from buttons import Button
from input_boxes import InputBox
from boards import Board
from avatars import Avatar

pygame.init()


def login():
    nameInput = InputBox(100, 100, 200, 50)
    loginButton = Button('Log In', 150, 200, 100, 40, red, bright_red, 3)
    t = Text('Escribe tu nombre:', 30, black, 200, 50)
    inputs = [nameInput]
    buttons = [loginButton]
    text = [t]
    loginScreen = Screen(
        400, 300, silver, 'Log In - Tetris en Red', buttons, inputs, text)
    loginScreen.run()


def main_menu():

    buttons = []
    text = []
    mainMenuScreen = Screen(
        800, 700, silver, 'Menu principal - Tetris en Red', buttons, [], text)
    mainMenuScreen.run()


main_menu()
