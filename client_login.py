import requests


class Client():

    id_player = ''
    id_game = ''

    def __init__(self):
        # while True:
        #     self.name = str(input("enter a name"))
        #     if self.name.isalpha():
        #         break
        #     print("Nombre no valido. Pruebe de nuevo")
        # self.avatar = input("enter an avatar")
        # self.create_player(self.name, self.avatar)
        # self.create_game()
        # self.add_player(Client.id_game, Client.id_player)
        pass

    def create_player(self, name, avatar):
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
