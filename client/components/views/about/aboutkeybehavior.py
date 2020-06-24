import pygame
from ..keyboard_behavior.keyboard_behavior import keyboardBehavior
from client.components.entities.text.texts import Text
from client.components.entities.colors.colores import *
import random

class aboutKeyboardBehavior(keyboardBehavior):

    def __init__(self):
        self.backAction = None
        self.activo = False
        self.n1 = Text('Fran',50,bright_red,500,350)
        self.n2 = Text('Juli',50,bright_blue,200,250)
        self.n3 = Text('Sofi',50,bright_yellow,300,500)
        self.n4 = Text('Nacho',50,bright_green,400,120)
        self.lista_nombres = [self.n1,self.n2,self.n3,self.n4]
        self.velocidadx = 0.6
        self.velocidady = 0.6

    def handle_event(self,key):
        if key == 'escape':
            self.backAction()
        if key == 'x':
            self.activo = True

    def setBackAction(self,action):
        self.backAction = action

    def drawAction(self,surface):
        self.velocidadx = random.randint(-1,1)
        self.velocidady = random.randint(-1,1)
        for name in self.lista_nombres:
            name.x += self.velocidadx
            name.y += self.velocidady
            name.draw(surface)