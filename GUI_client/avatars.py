import pygame
from colores import *

class Avatar:
    def __init__(self,x,y,w,h,img=''):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = img
        self.rect = pygame.Rect(x, y, w, h)
        self.avatar = pygame.image.load(self.img)

    def draw(self,surface):
        pygame.draw.rect(surface,black,self.rect,2)
        surface.blit(self.avatar,(self.x,self.y))

    def handle_events(self,event):
        pass

    def get_avatar(self):
        return self.img