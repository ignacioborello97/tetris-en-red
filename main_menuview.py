import pygame,sys
from pygame.locals import *
from views import ViewBuilder
from texts import Text
from buttons import Button
from colores import *

class mainmenuViewBuilder(ViewBuilder):
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

    def create(self,name='Nombre',createAction=None,searchAction=None,instrAction=None,configAction=None,aboutAction=None, newGame=None):
        self.name = name
        create_game = Button('Crear partida',self.width/4,self.height*(31/70),self.width/2,self.height/8.75,bright_red,red,6,createAction, newGame)
        search_game = Button('Buscar partida',self.width/4,self.height*(4/7),self.width/2,self.height/8.75,bright_green,green,6,searchAction)
        instructions = Button('Instrucciones',self.width/4,self.height*(7/10),self.width/2,self.height/8.75,bright_blue,blue,6,instrAction)
        configuration = Button('Configuracion',self.width/8,self.height*(31/35),self.width/4,self.height*(3/35),bright_yellow,yellow,6,configAction)
        about = Button('Acerca de',self.width/1.6,self.height*(31/35),self.width/4,self.height*(3/35),bright_yellow,yellow,6,aboutAction)
        self.buttons = [create_game,search_game,instructions,about,configuration]

        welcomeText = Text('¡Bienvenido ' + name + '!',int(self.width/13.33),black,self.width/2,self.height*(3/35))
        tetrisText = Text('Tetris en Red',int(self.width/6.67),black,self.width/2,self.height*(9/35))
        self.texts = [welcomeText,tetrisText]

    def destroy(self):
        self.corriendo = False
        
        
