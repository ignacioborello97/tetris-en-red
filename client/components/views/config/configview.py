import pygame,sys
from pygame.locals import *
from client.components.views.views import ViewBuilder
from client.components.entities.text.texts import Text
from client.components.entities.button.buttons import Button
from client.components.entities.colors.colores import *

class configViewBuilder(ViewBuilder):
    def __init__(self, width, height, bg, title=''):
        ViewBuilder.__init__(self, width, height, bg, title)
        self.buttons = [] 
        self.texts = []

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

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                for b in self.buttons:
                    b.handle_event(event)
            
            pygame.display.update()

    def create(self,backAction=None,onAction=None,offAction=None):
        backButton = Button('<------',self.width/15,self.height/1.2,self.width/4,self.height/7.5,white,(200,200,200),3,backAction)
        onButton = Button('Music On',self.width/6,self.height/3,self.width/3,self.height/6,green,bright_green,3,onAction)
        offButton = Button('Music Off',self.width*(3/6),self.height/3,self.width/3,self.height/6,red,bright_red,3,offAction)
        self.buttons = [backButton,onButton,offButton]

        t1 = Text('Elige si quieres jugar con música',int(self.width/20),black,self.width/2,self.height/10)
        self.texts = [t1]

    def destroy(self):
        self.corriendo = False