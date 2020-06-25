import pygame,sys
from pygame.locals import *
from client.components.entities.colors.colores import *

class Avatar:
    def __init__(self,x,y,w,h,img=''):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = img
        self.rect = pygame.Rect(x, y, w, h)
        self.avatar = pygame.image.load(self.img)
        self.getChosen = False

    def draw(self,surface):
        self.mx, self.my = pygame.mouse.get_pos()

        surface.blit(self.avatar,(self.x,self.y))
        pygame.draw.rect(surface,black,self.rect,2)

        if self.x+self.w > self.mx > self.x and self.y+self.h > self.my > self.y:
            pygame.draw.rect(surface,black,self.rect,6)

    def do_action(self):
        self.getChosen = True

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.getChosen = True

    def getAvatar(self):
        return self.img

    