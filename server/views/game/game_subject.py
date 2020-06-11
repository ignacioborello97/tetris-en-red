from ...index import socketio
from ...controllers.game.game import GameController

class GameSubject:
    def __init__(self, game_id):
        game_controller = GameController()
        self.game_id = game_id
        self.game = game_controller.get_game()
        socketio.on_event('key_press', self.key_press, namespace='/game/'+game.id)

    def key_press(self, json):
        print(str(json))