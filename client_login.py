import requests

class Client():

    def __init__(self):
        # while True:
        #     self.name = str(input("enter a name"))
        #     if self.name.isalpha():
        #         break
        #     print("Nombre no valido. Pruebe de nuevo")
        # self.avatar = input("enter an avatar")
        # self.create_player(self.name, self.avatar)
        # self.create_game()
        # self.add_player(self.id_game, self.id_player)
        self.id_player = ''
        self.id_game = ''

    def create_player(self, name, avatar):
        message = {
            "name": name,
            "avatar": avatar
        }

        response = requests.post('http://localhost:5000/player', json=message)
        player = response.json()
        print(response.json())
        self.id_player = player['id']
        print("id jugador  ", self.id_player)

    def create_game(self):
        response = requests.post('http://localhost:5000/game')
        game = response.json()
        self.id_game = game['id']
        print(response.json())

    def add_player(self, id_game, id_player):
        message = {
            "id": id_player
        }
        address = 'http://localhost:5000/game/' + id_game + '/players'
        print(address)
        response = requests.post(address, json=message)
        print(response.json())

    def get_idplayer(self):
        return self.id_player

    def get_idgame(self):
        return self.id_game


