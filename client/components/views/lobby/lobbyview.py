import pygame,sys
from pygame.locals import *
from client.components.views.views import ViewBuilder
from client.components.entities.text.texts import Text
from client.components.entities.button.buttons import Button
from client.components.entities.colors.colores import *
from client.components.entities.avatars.avatars import Avatar


class lobbyViewBuilder(ViewBuilder):
    def __init__(self, width, height, bg, title=''):
        ViewBuilder.__init__(self, width, height, bg, title)
        self.buttons = []
        self.texts = []
        self.avatares = []

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

            for a in self.avatares:
                a.draw(self.screen)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                for b in self.buttons:
                    b.handle_event(event)
            
            pygame.display.update()

    def create(self,userAvatar,backAction=None,readyAction=None):
        backButton = Button('<------',self.width/15,self.height/1.15,self.width/4,self.height/12,white,(200,200,200),3,backAction)
        readyButton = Button('Ready!',self.width/3,self.height*(2/3),self.width/3,self.height/10,red,bright_red,4,readyAction)
        self.buttons = [backButton,readyButton]
        
        t1 = Text('Partida #ssad28w',int(self.width/13),black,self.width/2,self.height/17.5)
        t2 = Text('Player1',int(self.width/20),black,self.width/8,self.height/5)
        t3 = Text('Player2',int(self.width/20),black,self.width*(3/8),self.height/5)
        t4 = Text('Player3',int(self.width/20),black,self.width/1.6,self.height/5)
        t5 = Text('Player4',int(self.width/20),black,self.width*(7/8),self.height/5)
        t6 = Text('Estado: Listo',int(self.width/40),black,self.width/8,self.height*(18/35))
        t7 = Text('Estado: Esperando',int(self.width/40),black,self.width*(3/8),self.height*(18/35))
        t8 = Text('Estado: Listo',int(self.width/40),black,self.width/1.6,self.height*(18/35))
        t9 = Text('Estado: Listo',int(self.width/40),black,self.width*(7/8),self.height*(18/35))
        self.texts = [t1,t2,t3,t4,t5,t6,t7,t8,t9]   

        avatar1 = Avatar(self.width/16,self.height/3.5,self.width/8,self.height/7,userAvatar)
        avatar2 = Avatar(self.width/3.2,self.height/3.5,self.width/8,self.height/7,'perezoso100x100.png')
        avatar3 = Avatar(self.width/1.78,self.height/3.5,self.width/8,self.height/7,'unicornio100x100.png')
        avatar4 = Avatar(self.width/1.23,self.height/3.5,self.width/8,self.height/7,'t-rex100x100.png')
        self.avatares = [avatar1,avatar2,avatar3,avatar4]

    def destroy(self):
        self.corriendo = False