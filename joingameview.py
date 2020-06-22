import pygame,sys
from pygame.locals import *
from views import ViewBuilder
from texts import Text
from buttons import Button
from input_boxes import InputBox
from colores import *

class joingameViewBuilder(ViewBuilder):
    def __init__(self, width, height, bg, title=''):
        ViewBuilder.__init__(self, width, height, bg, title)
        self.buttons = []
        self.texts = []
        self.inputs = []
        
    def run(self):
        self.corriendo = True
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption(self.title)
        self.screen.fill(self.bg)  
        while True:
            for i in self.inputs:
                i.update()
            self.screen.fill(self.bg)
            
            for b in self.buttons:
                b.draw(self.screen)

            for i in self.inputs:
                i.draw(self.screen)
            
            for t in self.texts:
                t.draw(self.screen)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                for b in self.buttons:
                    b.handle_event(event)

                for i in self.inputs:
                    i.handle_event(event)
            
            pygame.display.update()
    
    def create(self,backAction=None,joinAction=None, lookGame=None):
        backButton = Button('<------',self.width/15,self.height/1.2,self.width/4,self.height/7.5,white,(200,200,200),3,backAction)
        joinButton = Button('Join Game',self.width/3,self.height/2,self.width/3,self.height/6,red,bright_red,4,joinAction, lookGame)
        self.buttons = [backButton,joinButton]

        t1 = Text('Ingresa el codigo',int(self.width/20),black,self.width/2,self.height/12)
        self.texts = [t1]

        inputCode = InputBox(self.width/4,self.height/4,self.width/2,50)
        self.inputs = [inputCode]

    def destroy(self):
        self.corriendo = False

    def get_lookGame(self):
        #print(self.inputs[0].get_username())
        return self.inputs[0].get_username()