import pygame
import sys
from pygame.locals import *
from client.components.views.views import ViewBuilder
from client.components.entities.text.texts import Text
from client.components.entities.button.buttons import Button
from client.components.entities.colors.colores import *
from client.components.entities.avatars.avatars import Avatar
from client_login import Client

client = Client()


class lobbyViewBuilder(ViewBuilder):
    def __init__(self, width, height, bg, title=''):
        ViewBuilder.__init__(self, width, height, bg, title)
        self.buttons = []
        self.texts = []
        self.avatares = []

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

            for a in self.avatares:
                a.draw(self.screen)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                for b in self.buttons:
                    b.handle_event(event)

            if(cont % 1000 == 0):
                players = client.get_game_players(client.get_idgame())
                self.draw_players(players)

            pygame.display.update()

    def draw_players(self, players):
        print('PLAYERS  :::::: '+str(players))

        self.avatares = []
        # Mapas de factores para acomodar texto e imagenes
        map_text = [1, 3, 5, 7]
        map_avatar = [1, 5, 9, 13]
        map_estados = {
            "PENDING": "Esperando",
            "READY": "Listo!"
        }
        for index, player in enumerate(players):
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
            self.texts.append(player_text)
            self.texts.append(player_state_text)
            self.avatares.append(player_avatar)
            # adios ʕ•ᴥ•ʔ

    def create(self, userAvatar, backAction=None, readyAction=None):
        backButton = Button('<------', self.width/15, self.height/1.15,
                            self.width/4, self.height/12, white, (200, 200, 200), 3, backAction)
        readyButton = Button('Ready!', self.width/3, self.height*(2/3),
                             self.width/3, self.height/10, red, bright_red, 4, readyAction)
        self.buttons = [backButton, readyButton]

        t1 = Text('Codigo para unirse : '+client.get_idgame(), int(self.width/13),
                  black, self.width/2, self.height/17.5)

        # t6 = Text('Estado: Listo', int(self.width/40),
        #           black, self.width/8, self.height*(18/35))
        # t7 = Text('Estado: Esperando', int(self.width/40),
        #           black, self.width*(3/8), self.height*(18/35))
        # t8 = Text('Estado: Listo', int(self.width/40),
        #           black, self.width/1.6, self.height*(18/35))
        # t9 = Text('Estado: Listo', int(self.width/40), black,
        #           self.width*(7/8), self.height*(18/35))
        self.texts = [t1]

    def destroy(self):
        self.corriendo = False
