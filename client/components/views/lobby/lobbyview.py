import pygame
import sys
import socketio
from pygame.locals import *
from client.components.views.views import ViewBuilder
from client.components.entities.text.texts import Text
from client.components.entities.button.buttons import Button
from client.components.entities.colors.colores import *
from client.components.entities.avatars.avatars import Avatar
from client_login import Client
from ....lib.lib_socket.lib_socket import GameNamespace, GameObserver
from .lobbykeybehavior import lobbyKeyboardBehavior

client = Client()

class lobbyViewBuilder(ViewBuilder):
    def __init__(self, width, height, bg, title=''):
        ViewBuilder.__init__(self, width, height, bg, title)
        self.buttons = []
        self.texts = []
        self.avatares = []
        self.texts_names = []
        self.texts_states = []
        self.backAction = None
        self.readyAction = None
        self.behavior = lobbyKeyboardBehavior(self.send_ready)

    def run(self):
        self.corriendo = True
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.screen.fill(self.bg)
        cont = 0
        while self.corriendo:
            cont += 1
            self.screen.fill(self.bg)
            for b in self.buttons:
                b.draw(self.screen)

            for t in self.texts:
                t.draw(self.screen)

            for t in self.texts_names:
                t.draw(self.screen)

            for t in self.texts_states:
                t.draw(self.screen)

            for a in self.avatares:
                a.draw(self.screen)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                for b in self.buttons:
                    b.handle_event(event)

                if event.type == pygame.KEYDOWN:    
                    if event.key == pygame.K_ESCAPE:
                        self.behavior.handle_event('escape')
                    if event.key == pygame.K_RETURN:
                        self.behavior.handle_event('enter')

            if(cont % 1000 == 0):
                players = client.get_game_players(client.get_idgame())
                self.draw_players(players)
          
                
            pygame.display.update()


    def draw_players(self, players):
        self.avatares = []
        self.texts_states = []
        # Mapas de factores para acomodar texto e imagenes
        map_text = [1, 3, 5, 7]
        map_avatar = [1, 5, 9, 13]
        map_estados = {
            "PENDING": "Esperando",
            "READY": "Listo!"
        }
        print('players : ',str(players))
        for index, player in enumerate(players):
            print('player : ',str(player))
            print('map_estados : ',str(map_estados))
            STATE = map_estados[player['state']]
            factor_text = map_text[index]
            factor_avatar = map_avatar[index]
            # Dibujar jugador
            player_text = Text(player['name'], int(self.width/20),
                               black, self.width*(factor_text/8), self.height/5)
            # Dibujar texto
            player_state_text = Text('Estado: '+STATE, int(self.width/40),
                                     black, self.width*(factor_text/8), self.height*(18/35))
            # Dibujar Avatar
            player_avatar = Avatar(
                self.width*(factor_avatar/16), self.height/3.5, self.width/8, self.height/7, player['avatar'])
            # Agregar textos y imagenes a sus respectivos arrays
            self.texts_names.append(player_text)
            self.texts_states.append(player_state_text)
            self.avatares.append(player_avatar)
            # adios ʕ•ᴥ•ʔ

    def create(self, userAvatar, backAction=None, readyAction=None):
        self.behavior.setBackAction(backAction)
        self.behavior.setReadyAction(readyAction)

        backButton = Button('<------', self.width/15, self.height/1.15,
                            self.width/4, self.height/12, white, (200, 200, 200), 3, backAction)
        readyButton = Button('Ready!', self.width/3, self.height*(2/3),
                             self.width/3, self.height/10, red, bright_red, 4, readyAction, self.send_ready)
        self.buttons = [backButton, readyButton]

        t1 = Text('Codigo para unirse : '+client.get_idgame(), int(self.width/13),black, self.width/2, self.height/17.5)

        self.texts = [t1]

        # DEFINICION DEL SOCKET
        sio = socketio.Client()
        sio.connect('http://localhost:5000', namespaces=['/game/' + client.get_idgame()])

        gamenamespace = GameNamespace('/game/' + client.get_idgame())
        gamenamespace.set_player(client.get_idplayer())
        gamenamespace.set_sio(sio)
        # ENCHUFAR EL SUBJECT AL socketio
        sio.register_namespace(gamenamespace)
        # CREAS UN OBSERVER DEL JUEGO
        game_observer = GameObserver()
        # PONES AL OBSERVER A MIRAR LOS EVENTOS
        game_observer.observe(gamenamespace)
        game_observer.set_start_action(self.start_announce)

        client.set_gamenamespace(gamenamespace)
        client.set_gameobserver(game_observer)

    def destroy(self):
        self.corriendo = False

    def send_ready(self):
        print('APRETAR EL BOTON READY')
        gamenamespace = client.get_gamenamespace()
        gamenamespace.ready()
        
    def start_announce(self):
        print('YA ESTAMOS LISTOS')