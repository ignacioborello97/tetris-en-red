import pygame,sys
from pygame.locals import *
from views import ViewBuilder

class playViewBuilder(ViewBuilder):
    def __init__(self, width, height, bg, title='',boards=[],texts=[],avatares=[]):
        pygame.init()
        self.width = width
        self.height = height
        self.bg = bg
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption(title)
        self.screen.fill(self.bg)   
        self.boards = boards 
        self.texts = texts
        self.avatares = avatares

    def run(self):
        while True:
        
            for b in self.boards:
                b.draw(self.screen)

            for t in self.texts:
                t.draw(self.screen)

            for a in self.avatares:
                a.draw(self.screen)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                for b in self.boards:
                    b.handle_event(event)
            
            pygame.display.update()