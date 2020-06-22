import pygame,sys
from pygame.locals import *
from views import ViewBuilder

class loginViewBuilder(ViewBuilder):
    def __init__(self, width, height, bg, title='',buttons=[],texts=[],avatares=[],inputs=[]):
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
        self.inputs = []

    def run(self):
        while True:
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
    
    def create(self):
        nameInput = InputBox(300, 100, 200, 50)
        self.inputs = [nameInput]

        loginButton = Button('Log In', 300, 500, 200, 80, red, bright_red, 3)
        self.buttons = [loginButton]

        t = Text('Escribe tu nombre:', 30, black, 400, 50)
        t2 = Text('Escoge tu avatar:', 30, black, 400, 220)
        self.texts = [t, t2]

        avatar1 = Avatar(80, 300, 100, 100, 'dragon100x100.png')
        avatar2 = Avatar(260, 300, 100, 100, 'perezoso100x100.png')
        avatar3 = Avatar(440, 300, 100, 100, 'unicornio100x100.png')
        avatar4 = Avatar(600, 300, 100, 100, 't-rex100x100.png')
        self.avatares = [avatar1, avatar2, avatar3, avatar4]