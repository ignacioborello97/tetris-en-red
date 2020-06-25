import requests
from client.lib.lib_socket.lib_socket import GameObserver, GameNamespace


class Client():

    id_player: str = ''
    id_game: str = ''
    player_name: str = ''
    server_ip: str = 'http://localhost:5000'
    gamenamespace: GameNamespace
    gameobserver: GameObserver

    def __init__(self):
        pass

    def create_player(self, name: str, avatar):
        message = {
            "name": name,
            "avatar": avatar
        }
        response = requests.post(self.get_serverIP() + '/player', json=message)
        player = response.json()
        Client.id_player = player['id']
        Client.player_name = name


    def create_game(self):
        response = requests.post(self.get_serverIP() + '/game')
        game = response.json()
        Client.id_game = game['id']


    def add_player(self, id_game, id_player):
        message = {
            "id": id_player
        }
        address = self.get_serverIP() + '/game/' + id_game + '/players'
        print(address)
        response = requests.post(address, json=message)
        return response.json()

    def get_idplayer(self):
        return Client.id_player

    def get_idgame(self):
        return Client.id_game

    def get_game_players(self, id_game):
        address = self.get_serverIP() + '/game/' + id_game + '/players'
        response = requests.get(address)
        return response.json()

    def set_game_id(self, game_id):
        Client.id_game = game_id

    def set_gamenamespace(self, gamenamespace):
        Client.gamenamespace = gamenamespace

    def set_gameobserver(self, gameobserver):
        Client.gameobserver = gameobserver

    def set_serverIP(self,server_ip):
        Client.server_ip = server_ip

    def get_gamenamespace(self) -> GameNamespace:
        return Client.gamenamespace

    def get_gameobserver(self) -> GameObserver:
        return Client.gameobserver

    def get_player_name(self):
        return Client.player_name

    def get_serverIP(self):
        return Client.server_ip