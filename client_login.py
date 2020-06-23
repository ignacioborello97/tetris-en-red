import requests
from client.lib.lib_socket.lib_socket import GameObserver, GameNamespace


class Client():

    id_player: str = ''
    id_game: str = ''

    gamenamespace: GameNamespace
    gameobserver: GameObserver

    def __init__(self):
        pass

    def create_player(self, name: str, avatar):
        message = {
            "name": name,
            "avatar": avatar
        }

        response = requests.post('http://localhost:5000/player', json=message)
        player = response.json()
        print(response.json())
        Client.id_player = player['id']
        print("id jugador  ", Client.id_player)

    def create_game(self):
        response = requests.post('http://localhost:5000/game')
        game = response.json()
        Client.id_game = game['id']
        print(response.json())

    def add_player(self, id_game, id_player):
        message = {
            "id": id_player
        }
        address = 'http://localhost:5000/game/' + id_game + '/players'
        print(address)
        response = requests.post(address, json=message)
        return response.json()

    def get_idplayer(self):
        return Client.id_player

    def get_idgame(self):
        return Client.id_game

    def get_game_players(self, id_game):
        address = 'http://localhost:5000/game/' + id_game + '/players'
        response = requests.get(address)
        return response.json()

    def set_game_id(self, game_id):
        Client.id_game = game_id

    def set_gamenamespace(self, gamenamespace):
        Client.gamenamespace = gamenamespace

    def set_gameobserver(self, gameobserver):
        Client.gameobserver = gameobserver

    def get_gamenamespace(self) -> GameNamespace:
        return Client.gamenamespace

    def get_gameobserver(self) -> GameObserver:
        return Client.gameobserver
