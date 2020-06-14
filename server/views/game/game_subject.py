from ...index import socketio
from ...controllers.game.game import GameController

class GameSubject:
    def __init__(self, game_id):
        self.game_controller = GameController()
        self.cont = 0

        self.game_id = game_id
        self.game = self.game_controller.get_game(self.game_id)
        self.namespace = '/game/'+self.game.id
        socketio.on_event('key_press', self.key_press, namespace=self.namespace)
        socketio.on_event('ready', self.ready, namespace=self.namespace)
        socketio.on_event('piece_fall', self.piece_fall, namespace=self.namespace)

    def key_press(self, json):
        player = self.game.get_player(json["player_id"])

        action_map = {
            "left":player.action_move_left,
            "right":player.action_move_right,
            "x":player.action_rotate_clock,
            "z":player.action_rotate_unclock,
            "down":player.action_accelerate
        }

        action_map[json["key"]]()

        self.game_controller.distribute_pieces(self.game_id)
        board_state = self.game_controller.get_board(self.game_id, json["player_id"])
        socketio.emit('board_state', {"board_state": board_state}, namespace=self.namespace)

    
    def ready(self, json):
        print(str(json))
        if(self.game.get_player(json["player_id"]) is not None):
            self.game_controller.ready_player(self.game_id, json["player_id"])
            if(self.game_controller.get_game_ready(self.game_id)):
                self.game_controller.distribute_pieces(self.game_id)
                self.game_controller.start_game(self.game_id)
                socketio.emit('game_state', {"game_state":"STARTED"}, namespace=self.namespace)
    
    def piece_fall(self, json):
        self.game_controller.distribute_pieces(self.game_id)
        board = self.game.get_player(json["player_id"]).board

        board.active_piece.y += 1
        board.active_piece.calculate_blocks()
        if not board.active_piece.check_state(board.positions):
            board.active_piece.y -= 1
            board.active_piece.calculate_blocks()
            board.calculate_piece_fall()
            if(board.lost == True):
                socketio.emit('player_lose', {"player_id": json["player_id"]}, namespace=self.namespace)
                return 
            if(board.active_piece == None):
                self.game_controller.distribute_pieces(self.game_id)
            
        board_state = self.game_controller.get_board(self.game_id, json["player_id"])
        socketio.emit('board_state', {"board_state": board_state}, namespace=self.namespace)