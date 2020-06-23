import pygame
import sys
import socketio
from pygame.locals import *
from client.components.views.views import ViewBuilder
from client.components.entities.avatars.avatars import Avatar
from client.components.entities.text.texts import Text
from client.components.entities.colors.colores import *
from client.components.entities.board.boards import Board
from client_login import Client
from ....lib.lib_socket.lib_socket import GameNamespace, GameObserver


# def start_announce():
#     print('YA ESTAMOS LISTOS')
# # DEFINICION DEL SOCKET
# client = Client()
# sio = socketio.Client()
# sio.connect('http://localhost:5000', namespaces=['/game/' + client.get_idgame()])

# gamenamespace = GameNamespace('/game/' + client.get_idgame())
# gamenamespace.set_player(client.get_idplayer())
# gamenamespace.set_sio(sio)
# # ENCHUFAR EL SUBJECT AL socketio
# sio.register_namespace(gamenamespace)
# # CREAS UN OBSERVER DEL JUEGO
# game_observer = GameObserver()
# # PONES AL OBSERVER A MIRAR LOS EVENTOS
# game_observer.observe(gamenamespace)
# game_observer.set_start_action(start_announce)

# client.set_gamenamespace(gamenamespace)
# client.set_gameobserver(game_observer)
# players = client.get_game_players(client.get_idgame())
# print(str(players))
# board = players['id']
# print(str(board))

class playViewBuilder(ViewBuilder):
    def __init__(self, width, height, bg, title=''):
        ViewBuilder.__init__(self, width, height, bg, title)
        self.boards = []
        self.texts = []
        self.avatares = []

    # def updateBoard(self):
    #     def start_announce():
    #         print('YA ESTAMOS LISTOS')
    # # DEFINICION DEL SOCKET
    #     client = Client()
    #     sio = socketio.Client()
    #     sio.connect('http://localhost:5000', namespaces=['/game/' + client.get_idgame()])

    #     gamenamespace = GameNamespace('/game/' + client.get_idgame())
    #     gamenamespace.set_player(client.get_idplayer())
    #     gamenamespace.set_sio(sio)
    #     # ENCHUFAR EL SUBJECT AL socketio
    #     sio.register_namespace(gamenamespace)
    #     # CREAS UN OBSERVER DEL JUEGO
    #     game_observer = GameObserver()
    #     # PONES AL OBSERVER A MIRAR LOS EVENTOS
    #     game_observer.observe(gamenamespace)
    #     game_observer.set_start_action(start_announce)

    #     client.set_gamenamespace(gamenamespace)
    #     client.set_gameobserver(game_observer)
    

    def run(self):
        #pygame.init()
        self.corriendo = True
        self.screen = pygame.display.set_mode((self.width, self.height))
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
                # if event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_LEFT:
                #         key = 'left'
                #         self.press_key(key)
                #     if event.key == pygame.K_RIGHT:
                #         key = 'right'
                #         self.press_key(key)
            

            # self.boards[0].update()

            pygame.display.update()

    def create(self, userAvatar):
        print('CREATE DE VISTA DEL JUEGO')
        t1 = Text('Nombre', int(self.width/20), black,
                  self.width*(5/32), self.height/14)
        t2 = Text('Score: 250000', int(self.width/27), black,
                  self.width*(5/32), self.height*(19/35))
        t3 = Text('Lines: 1000', int(self.width/27), black,
                  self.width*(5/32), self.height*(43/70))
        t4 = Text('Next', int(self.width/27), black,
                  self.width*(5/32), self.height*(26/35))
        t5 = Text('Level 20', int(self.width/27),
                  black, self.width/2, self.height/14)
        t6 = Text('Player2', int(self.width/40), black,
                  self.width*(27/32), self.height*(2/35))
        t7 = Text('Player3', int(self.width/40), black,
                  self.width*(27/32), self.height*(27/70))
        t8 = Text('Player4', int(self.width/40), black,
                  self.width*(27/32), self.height*(7/10))
        t9 = Text('Score: 200000', int(self.width/40), black,
                  self.width*(27/32), self.height*(3/35))
        t10 = Text('Score: 100000', int(self.width/40), black,
                   self.width*(27/32), self.height*(29/70))
        t11 = Text('Score: 200250', int(self.width/40), black,
                   self.width*(27/32), self.height*(51/70))
        self.texts = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11]

        mainBoard = Board(self.width*(5/16), self.height /
                          7.7, self.width*(3/80))
        p2Board = Board(self.width*(127/160),
                        self.height*(4/35), self.width/100)
        p3Board = Board(self.width*(127/160), self.height *
                        (31/70), self.width/100)
        p4Board = Board(self.width*(127/160), self.height *
                        (53/70), self.width/100)
        self.boards = [mainBoard, p2Board, p3Board, p4Board]

        avatar = Avatar(self.width/10.67, self.height/4.67,
                        self.width/8, self.height/7, userAvatar)
        self.avatares = [avatar]
        # self.updateBoard()
        # dibujar pieza siguiente?

    def destroy(self):
        self.corriendo = False

    # def press_key(self, key):
    #     print('se apreto una tecla')
    #     gamenamespace.press_key(key)
        
