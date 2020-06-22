import pygame
pygame.init()

class Text:
    def __init__(self,text,fs,color,x,y):
        self.text = text
        self.fs = fs
        self.font = pygame.font.SysFont('comicsansms', self.fs)
        self.color = color
        self.x = x
        self.y = y
               
    def draw(self,surface):
        textobj = self.font.render(self.text,1,self.color)
        textrect = textobj.get_rect()
        textrect.center = (self.x,self.y)
        surface.blit(textobj, textrect)