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
from .playkeybehavior import playKeyboardBehavior

client = Client()

class playViewBuilder(ViewBuilder):
    def __init__(self, width, height, bg, title=''):
        ViewBuilder.__init__(self, width, height, bg, title)
        self.boards = []
        self.texts = []
        self.avatares = []
        self.behavior = playKeyboardBehavior(self.press_key)

    def run(self):
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
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        key = 'left'
                        self.behavior.handle_event(key)
                    if event.key == pygame.K_RIGHT:
                        key = 'right'
                        self.behavior.handle_event(key)
                    if event.key == pygame.K_DOWN:
                        key = 'down'
                        self.behavior.handle_event(key)
                    if event.key == pygame.K_z:
                        key = 'z'
                        self.behavior.handle_event(key)
                    if event.key == pygame.K_x:
                        key = 'x'
                        self.behavior.handle_event(key)

            pygame.display.update()

    def create(self, userAvatar):
        self.contador_de_frames = 0

        t1 = Text(client.get_player_name(), int(self.width/20), black,
                  self.width*(5/32), self.height/14)
        t2 = Text('Score: ', int(self.width/27), black,
                  self.width*(5/32), self.height*(19/35))
        t3 = Text('Lines: ', int(self.width/27), black,
                  self.width*(5/32), self.height*(43/70))
        t4 = Text('Next', int(self.width/27), black,
                  self.width*(5/32), self.height*(26/35))
        t5 = Text('Level', int(self.width/27),
                  black, self.width/2, self.height/14)
        t6 = Text('', int(self.width/40), black,
                  self.width*(27/32), self.height*(2/35))
        t7 = Text('', int(self.width/40), black,
                  self.width*(27/32), self.height*(27/70))
        t8 = Text('', int(self.width/40), black,
                  self.width*(27/32), self.height*(7/10))
        t9 = Text('', int(self.width/40), black,
                  self.width*(27/32), self.height*(3/35))
        t10 = Text('', int(self.width/40), black,
                   self.width*(27/32), self.height*(29/70))
        t11 = Text('', int(self.width/40), black,
                   self.width*(27/32), self.height*(51/70))
        self.texts = [
            t1,  # 0  -> Nombre Cliente    
            t2,  # 1  -> Puntaje Cliente    
            t3,  # 2  -> Lineas Cliente    
            t4,  # 3  -> Pieza Siguiente
            t5,  # 4  -> Level    
            t6,  # 5  -> Nombre Player 2    
            t7,  # 6  -> Nombre Player 3    
            t8,  # 7  -> Nombre Player 4    
            t9,  # 8  -> Score Player 2        
            t10, # 9  -> Score Player 3        
            t11  # 10 -> Score Player 4         
            ]

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

        self.clientnamespace = client.get_gamenamespace()

        self.gameobserver = client.get_gameobserver()
        self.gameobserver.set_update_board_action(self.draw_board)

    def destroy(self):
        self.corriendo = False

    def draw_board(self, data):
        if self.contador_de_frames == 0:
            players = client.get_game_players(client.get_idgame())
            self.players = []
            self.player_boards = []
            board_used = 1
            for player in players:
                if player['id'] != client.get_idplayer():
                    self.player_boards.append(self.boards[board_used])
                    self.players.append(player)
                    board_used += 1

        player_id = data['player_id']
        board_state = data['board_state']
        player_state = data['player_state']

        if player_id == client.get_idplayer():
            self.boards[0].update(board_state)
            self.texts[1].text = 'Score: ' + str(player_state["score"])
            self.texts[2].text = 'Lines: ' + str(player_state["lines"])
            self.texts[4].text = 'Level: ' + str(player_state["level"])

        for index, player in enumerate(self.players):
            if player_id == player["id"]:
                self.player_boards[index].update(board_state)
                self.texts[5+index].text = player["name"]
                self.texts[8+index].text = 'Score: ' + str(player["score"])

    def press_key(self, key):
        self.clientnamespace.press_key(key)
