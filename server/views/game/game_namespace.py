from datetime import datetime
from ...index import socketio
from ...controllers.game.game import GameController, Game
from ...controllers.player.player import PlayerController, Player
from ...lib.Observer import Observer


class GameNamespace(Observer):
    def __init__(self, game_id):
        self.subjects = []
        self.game_controller = GameController()
        self.player_controller = PlayerController()
        self.cont = 0

        self.game_id = game_id
        self.game: Game = self.game_controller.get(self.game_id)
        self.namespace = '/game/'+self.game.id
        socketio.on_event('key_press', self.key_press,
                          namespace=self.namespace)
        socketio.on_event('ready', self.ready, namespace=self.namespace)
        socketio.on_event('piece_fall', self.piece_fall,
                          namespace=self.namespace)

        self.subscribe(self.game_controller)
        self.subscribe(self.player_controller)

    def key_press(self, json):
        action_map = {
            "left": 'move_left',
            "right": 'move_right',
            "x": 'rotate_clock',
            "z": 'rotate_unclock',
            "down": 'accelerate'
        }

        if action_map[json["key"]]:
            self.game.distribute_pieces()
            self.player_controller.emit(
                'to_player', {'player_id': json["player_id"], 'action': action_map[json["key"]]})
            self.game.distribute_pieces()

    def ready(self, json):
        self.player_controller.set(json["player_id"], {"state": Player.READY})
        if self.game.game_ready():
            self.game.state = Game.STARTED
            socketio.emit(
                'game_state', {"game_state": "STARTED"}, namespace=self.namespace)

    def piece_fall(self, json):
        self.game.distribute_pieces()
        self.player_controller.emit(
            'to_player', {'player_id': json["player_id"], 'action': 'piece_fall'})
        self.game.distribute_pieces()

    def update(self, channel, data):
        if(channel == 'from_player'):
            if data['action'] == 'board_state':
                socketio.emit('board_state', {
                    "player_id": data['player_id'],
                    "board_state": data['board_state'],
                    "player_state": data['player_state']
                }, namespace=self.namespace)
