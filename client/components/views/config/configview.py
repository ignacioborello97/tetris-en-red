import pygame,sys
from pygame.locals import *
from client.components.views.views import ViewBuilder
from client.components.entities.text.texts import Text
from client.components.entities.button.buttons import Button
from client.components.entities.inputbox.input_boxes import InputBox
from client.components.entities.colors.colores import *
from client_login import Client
from .configkeybehavior import configKeyboardBehavior

client = Client()
class configViewBuilder(ViewBuilder):
    def __init__(self, width, height, bg, title=''):
        ViewBuilder.__init__(self, width, height, bg, title)
        self.buttons = [] 
        self.texts = []
        self.inputs = []
        self.volver='Login'
        self.backAction = None
        self.onAction = None
        self.offAction = None
        self.behavior = configKeyboardBehavior(self.conectar)

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

            for i in self.inputs:
                i.draw(self.screen)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                
                for b in self.buttons:
                    b.handle_event(event)

                for i in self.inputs:
                    i.handle_event(event)

                if event.type == pygame.KEYDOWN:    
                    if event.key == pygame.K_ESCAPE:
                        self.behavior.handle_event('escape')
                    if event.key == pygame.K_RETURN:
                        self.behavior.handle_event('enter')
                    if event.key == pygame.K_p:
                        self.behavior.handle_event('p')
                    if event.key == pygame.K_SPACE:
                        self.behavior.handle_event('espacio')
            
            pygame.display.update()

    def create(self,backAction1=None,backAction2=None,onAction=None,offAction=None):
        if self.volver=='Login':
            self.backAction = backAction1
        else:
            self.backAction = backAction2
        self.onAction = onAction
        self.offAction = offAction
        
        self.behavior.setBackAction(self.backAction)
        self.behavior.setMusicOnAction(self.onAction)
        self.behavior.setMusicOffAction(self.offAction)

        inputIP = InputBox(self.width/8,self.height/1.75,self.width/1.33,self.height/14)
        self.inputs = [inputIP]

        backButton = Button('<------',self.width/15,self.height/1.2,self.width/4,self.height/7.5,white,(200,200,200),3,self.backAction)
        onButton = Button('Music On',self.width/6,self.height/4,self.width/3,self.height/6,green,bright_green,3,self.onAction)
        offButton = Button('Music Off',self.width*(3/6),self.height/4,self.width/3,self.height/6,red,bright_red,3,self.offAction)
        connectButton = Button('Conectar',self.width/3,self.height/1.5,self.width/3,self.height/8,green,bright_green,3,self.conectar)
        self.buttons = [backButton,onButton,offButton,connectButton]

        t1 = Text('Elige si quieres jugar con música',int(self.width/20),black,self.width/2,self.height/10)
        t2 =  Text('Pon la direccion ip del server',int(self.width/20),black,self.width/2,self.height/2)
        self.texts = [t1,t2]

    def set_volver(self,pantalla):
        self.volver = pantalla

    def destroy(self):
        self.corriendo = False

    def conectar(self):
        ip = self.getServerIp()
        client.set_serverIP(ip)
        
    def getServerIp(self):
        return self.inputs[0].get_username()
