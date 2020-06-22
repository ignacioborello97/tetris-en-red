import pygame,sys
from pygame.locals import *
from views import ViewBuilder

class lobbyViewBuilder(ViewBuilder):
    def __init__(self, width, height, bg, title='',buttons=[],texts=[],avatares=[],menuView=None):
        pygame.init()
        self.width = width
        self.height = height
        self.bg = bg
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption(self.title)
        self.screen.fill(self.bg)   
        self.buttons = [] 
        self.texts = []
        self.avatares = []
        self.menuView = menuView

    def run(self):
        while True:
        
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

    def create(self):
        backButton = Button('<------', 30, 510, 150, 60, white,
                        (200, 200, 200), 3, main_menu_screen)
        readyButton = Button('Ready!', 267, 420, 267, 60, green, bright_green, 4)
        self.buttons = [backButton, readyButton]

        t1 = Text('Partida #ssad28w', 60, black, 400, 40)
        t2 = Text('Player1', 40, black, 100, 140)
        t3 = Text('Player2', 40, black, 300, 140)
        t4 = Text('Player3', 40, black, 500, 140)
        t5 = Text('Player4', 40, black, 700, 140)
        t6 = Text('Estado: Listo', 20, black, 100, 360)
        t7 = Text('Estado: Esperando', 20, black, 300, 360)
        t8 = Text('Estado: Listo', 20, black, 500, 360)
        t9 = Text('Estado: Listo', 20, black, 700, 360)
        self.texts = [t1, t2, t3, t4, t5, t6, t7, t8, t9]

        avatar1 = Avatar(50, 200, 100, 100, 'dragon100x100.png')
        avatar2 = Avatar(250, 200, 100, 100, 'perezoso100x100.png')
        avatar3 = Avatar(450, 200, 100, 100, 'unicornio100x100.png')
        avatar4 = Avatar(650, 200, 100, 100, 't-rex100x100.png')
        self.avatar = [avatar1, avatar2, avatar3, avatar4]