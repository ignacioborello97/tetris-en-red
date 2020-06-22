import pygame,sys
from pygame.locals import *

class ViewBuilder:
    def __init__(self,width,height,bg,title=''):
        #es el constructor de las views con los parametros en comun
        self.width = width
        self.height = height
        self.bg = bg   
        self.title = title

    def run(self):
        #esta funcion corre la pantalla y maneja eventos
        raise NotImplementedError
        pass

    def create(self):
        #añade lo que debe dibujar cada view
        raise NotImplementedError
        pass

    def destroy(self):
        #borra la vista cuando es necesario
        raise NotImplementedError
        pass

