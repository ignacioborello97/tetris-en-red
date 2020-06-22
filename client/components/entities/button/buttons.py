import pygame
from ..colors.colores import *


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

class Button:

    def __init__(self,msg,x,y,w,h,ic,ac,bs,action=None, action2=None):
        self.font = pygame.font.SysFont('comicsansms', int(w/8))
        self.rect = pygame.Rect(x,y,w,h)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.msg = msg
        self.ic = ic
        self.ac = ac
        self.color = ic
        self.bs = bs
        self.action = action
        self.action2 = action2

    def draw(self,surface):    
        self.mx, self.my = pygame.mouse.get_pos()
        
        pygame.draw.rect(surface, self.ic, self.rect)
        pygame.draw.rect(surface, black,self.rect,self.bs)

        if self.x+self.w > self.mx > self.x and self.y+self.h > self.my > self.y:
            pygame.draw.rect(surface, self.ac, self.rect)
            pygame.draw.rect(surface, black,self.rect,self.bs)           

        draw_text(self.msg,self.font,black,surface,self.x+self.w/2,self.y+self.h/2)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                if self.action != None:
                    if self.action2 != None:
                        self.action2()
                    self.action()
                    
                