import pygame,sys
from pygame.locals import *
from views import ViewBuilder

class joingameViewBuilder(ViewBuilder):
    def __init__(self, width, height, bg, title='',buttons=[],inputs=[]):
        pygame.init()
        self.width = width
        self.height = height
        self.bg = bg
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption(title)
        self.screen.fill(self.bg)   
        self.buttons = buttons 
        self.inputs = inputs

    def run(self):
        while True:
            for i in self.inputs:
                i.update()
            self.screen.fill(self.bg)
            
            for b in self.buttons:
                b.draw(self.screen)

            for i in self.inputs:
                i.draw(self.screen)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                for b in self.buttons:
                    b.handle_event(event)

                for i in self.inputs:
                    i.handle_event(event)
            
            pygame.display.update()