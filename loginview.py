import pygame,sys
from pygame.locals import *
from views import ViewBuilder
from texts import Text
from buttons import Button
from input_boxes import InputBox
from avatars import Avatar
from colores import *

class loginViewBuilder(ViewBuilder):
    def __init__(self, width, height, bg, title=''):
        ViewBuilder.__init__(self, width, height, bg, title)
        self.buttons = []
        self.texts = []
        self.avatares = []
        self.inputs = []       

    def run(self):
        self.corriendo = True
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption(self.title)
        self.screen.fill(self.bg)
        while self.corriendo:
            for i in self.inputs:
                i.update()
            self.screen.fill(self.bg)

            for b in self.buttons:
                b.draw(self.screen)

            for t in self.texts:
                t.draw(self.screen)

            for a in self.avatares:
                a.draw(self.screen)

            for i in self.inputs:
                i.draw(self.screen)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                for b in self.buttons:
                    b.handle_event(event)

                for a in self.avatares:
                    a.handle_event(event)

                for i in self.inputs:
                    i.handle_event(event)
            
            pygame.display.update()

    def create(self,logAction=None, logAction2 =None):
        nameInput = InputBox(self.width/2.67,self.height/6,self.width/4,self.height/12)
        self.inputs = [nameInput]
        
        loginButton = Button('Log In',self.width/2.67,self.height/1.2,self.width/4,self.height/7.5,red,bright_red,3,logAction, logAction2)
        self.buttons = [loginButton]

        t = Text('Escribe tu nombre:',int(self.width/26.67),black,self.width/2,self.height/12)
        t2 = Text('Escoge tu avatar:',int(self.width/26.67),black,self.width/2,self.height*(11/30))
        self.texts = [t,t2]

        avatar1 = Avatar(self.width/10,self.height/2,self.width/8,self.height/6,'dragon100x100.png')
        avatar2 = Avatar(self.width*(13/40),self.height/2,self.width/8,self.height/6,'perezoso100x100.png')
        avatar3 = Avatar(self.width*(11/20),self.height/2,self.width/8,self.height/6,'unicornio100x100.png')
        avatar4 = Avatar(self.width*(3/4),self.height/2,self.width/8,self.height/6,'t-rex100x100.png')
        self.avatares = [avatar1,avatar2,avatar3,avatar4]

    def destroy(self):
        self.corriendo = False

    def getName(self):
        return self.inputs[0].get_username()

    def getAvatar(self):
        for a in self.avatares:
            if a.getChosen:
                avatarChosen = a.getAvatar()

        return avatarChosen
        