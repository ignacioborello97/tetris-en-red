import pygame,sys
from pygame.locals import *
from client.components.views.views import ViewBuilder
from client.components.entities.text.texts import Text
from client.components.entities.button.buttons import Button
from client.components.entities.colors.colores import *

class instructionViewBuilder(ViewBuilder):
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

    def create(self,backAction=None):
        backButton = Button('<------',self.width/15,self.height/1.2,self.width/4,self.height/7.5,white,(200,200,200),3,backAction)
        self.buttons = [backButton]

        t1 = Text('Crear una partida',int(self.width/20),black,self.width/2,self.height/15)
        t2 = Text('Al pulsar el boton se creara una partida y obtendras el codigo',int(self.width/33),black,self.width/2,self.height/6)
        t3 = Text('de la misma. Pasaselo a tus amigos para que jueguen contigo.',int(self.width/33),black,self.width/2,self.height*(7/30))
        t4 = Text('Unirse a una partida',int(self.width/20),black,self.width/2,self.height/3)
        t5 = Text('Ingresa el codigo de la partida a la que',int(self.width/33),black,self.width/2,self.height*(13/30))
        t6 = Text('quieres unirte e ingresalo para poder jugar.',int(self.width/33),black,self.width/2,self.height/2)
        t7 = Text('Jugando',int(self.width/20),black,self.width/2,self.height*(3/5))
        t8 = Text('Controla las piezas con las flechas de',int(self.width/33),black,self.width/2,self.height*(7/10))
        t9 = Text('movimiento y no dejes que toquen el limite superior.',int(self.width/33),black,self.width/2,self.height*(23/30))
        self.texts = [t1,t2,t3,t4,t5,t6,t7,t8,t9]

    def destroy(self):
        self.corriendo = False
        

