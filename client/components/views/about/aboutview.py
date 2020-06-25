import pygame,sys
from pygame.locals import *
from client.components.views.views import ViewBuilder
from client.components.entities.text.texts import Text
from client.components.entities.button.buttons import Button
from client.components.entities.colors.colores import *
from .aboutkeybehavior import aboutKeyboardBehavior

class aboutViewBuilder(ViewBuilder):
    def __init__(self, width, height, bg, title=''):
        ViewBuilder.__init__(self, width, height, bg, title)
        self.buttons = [] 
        self.texts = []
        self.behavior = aboutKeyboardBehavior()

    def run(self):
        self.corriendo = True
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption(self.title)
        self.screen.fill(self.bg)   
        
        while self.corriendo:
            self.screen.fill(self.bg)
            for b in self.buttons:
                b.draw(self.screen)

            for t in self.texts:
                t.draw(self.screen)

            if self.behavior.activo:
                self.behavior.drawAction(self.screen)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                for b in self.buttons:
                    b.handle_event(event)

                if event.type == pygame.KEYDOWN:    
                    if event.key == pygame.K_x:
                        self.behavior.handle_event('x')
                    if event.key == pygame.K_ESCAPE:
                        self.behavior.handle_event('escape')

            
            pygame.display.update()

    def create(self,backAction=None):
        self.behavior.setBackAction(backAction)
        backButton = Button('<------',self.width/15,self.height/1.2,self.width/4,self.height/7.5,white,(200,200,200),3,backAction)
        self.buttons = [backButton]

        t1 = Text('Tetris en Red',int(self.width/6.67),black,self.width/2,self.height/7.5)
        t2 = Text('Tetricos',int(self.width/8),black,self.width/2,self.height*(11/30))
        t3 = Text('Copyright © 2020-2020',int(self.width/20),black,self.width/2,self.height*(3/5))
        t4 = Text('Version 1.0.0 - Build 1',int(self.width/20),black,self.width/2,self.height*(7/10))
        self.texts = [t1,t2,t3,t4]

    def destroy(self):
        self.corriendo = False