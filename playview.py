import pygame,sys
from pygame.locals import *
from views import ViewBuilder
from avatars import Avatar
from texts import Text
from boards import Board
from colores import *

class playViewBuilder(ViewBuilder):
    def __init__(self, width, height, bg, title=''):
        ViewBuilder.__init__(self, width, height, bg, title)
        self.boards = []
        self.texts = []
        self.avatares = []

    def run(self):
        self.corriendo = True
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption(self.title)
        self.screen.fill(self.bg)   
        while self.corriendo:
            self.screen.fill(self.bg)
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
            
            pygame.display.update()

    
    def create(self,userAvatar):
        t1 = Text('Nombre',int(self.width/20),black,self.width*(5/32),self.height/14)
        t2 = Text('Score: 250000',int(self.width/27),black,self.width*(5/32),self.height*(19/35))
        t3 = Text('Lines: 1000',int(self.width/27),black,self.width*(5/32),self.height*(43/70))
        t4 = Text('Next',int(self.width/27),black,self.width*(5/32),self.height*(26/35))
        t5 = Text('Level 20',int(self.width/27),black,self.width/2,self.height/14)
        t6 = Text('Player2',int(self.width/40),black,self.width*(27/32),self.height*(2/35))
        t7 = Text('Player3',int(self.width/40),black,self.width*(27/32),self.height*(27/70))
        t8 = Text('Player4',int(self.width/40),black,self.width*(27/32),self.height*(7/10))
        t9 = Text('Score: 200000',int(self.width/40),black,self.width*(27/32),self.height*(3/35))
        t10 = Text('Score: 100000',int(self.width/40),black,self.width*(27/32),self.height*(29/70))
        t11 = Text('Score: 200250',int(self.width/40),black,self.width*(27/32),self.height*(51/70))
        self.texts = [t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11]

        mainBoard = Board(self.width*(5/16),self.height/7,self.width*(3/80))
        p2Board = Board(self.width*(127/160),self.height*(4/35),self.width/100)
        p3Board = Board(self.width*(127/160),self.height*(31/70),self.width/100)
        p4Board = Board(self.width*(127/160),self.height*(53/70),self.width/100)
        self.boards = [mainBoard,p2Board,p3Board,p4Board]

        avatar = Avatar(self.width/10.67,self.height/4.67,self.width/8,self.height/7,userAvatar)
        self.avatares = [avatar]

        #dibujar pieza siguiente?

    def destroy(self):
        self.corriendo = False