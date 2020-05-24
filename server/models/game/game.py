import random
import string

class Game():

    PENDING = 'PENDING'
    STARTED = 'STARTED'
    PAUSED = 'PAUSED'
    FINISHED = 'FINISHED'
    pieces = ['S','Z','L','J','T','I']

    @classmethod
    def generate_id(cls):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(6))
    
    def __init__(self):
        self.id = Game.generate_id()
        self.players = []
        self.state = Game.PENDING
        self.piece_list = []
        self.piece_counter = 0
        self.countdown = 30

    def refresh_pieces(self):
        # get slowest player in game
        slowest_player = self.players[0]
        for player in self.players:
            if player < slowest_player.count:
                slowest_player = player
        # dispose of pieces already used by all players
        for index, piece in enumerate(self.pieces):
            if piece.count < slowest_player.count:
                self.pieces.pop(index)
        # fill the array with new pieces and keep the counter up
        for i in range(10 - len(self.pieces)):
            self.pieces.append({"shape": random.choice(Game.pieces), "count": self.piece_counter})
            self.piece_counter += 1


    def add_player(self, player):
        self.players.append(player)
    
    def remove_player(self, player):
        self.players.remove(player)

    def json(self):
        return {
            "id": self.id,
            # "players": self.players,
            "state": self.state,
            # "piece_list": self.piece_list,
            "piece_counter": self.piece_counter,
            "countdown": self.countdown,
        }

            

    
    