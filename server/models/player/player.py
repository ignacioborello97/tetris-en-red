import string
import random
from ..board.board import Board
from ...lib.Observer import Observer


class Player(Observer):

    @classmethod
    def generate_id(cls):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(6))

    IDDLE = 'IDDLE'
    PENDING = 'PENDING'
    READY = 'READY'
    PLAYING = 'PLAYING'
    LOSER = 'LOSER'
    SPECTATING = 'SPECTATING'

    def __init__(self, name, avatar):
        super().__init__()
        self.id = Player.generate_id()
        self.name = name
        self.avatar = avatar
        self.state = Player.IDDLE
        self.score = 0
        self.count = 0
        self.lines = 0
        self.tetris = 0
        self.board = Board(20, 10)

    def set_state(self, state):
        if(state in [Player.IDDLE, Player.PENDING, Player.READY, Player.PLAYING, Player.SPECTATING]):
            self.state = state

    def drop_piece(self, piece):
        self.board.add_piece(piece)
        self.emit_state()

    def has_piece(self):
        return self.board.active_piece != None

    def action_move_left(self, data):
        self.board.active_piece.x -= 1
        self.apply_action({"x": 1})

    def action_move_right(self, data):
        self.board.active_piece.x += 1
        self.apply_action({"x": -1})

    def action_rotate_clock(self, data):
        # self.board.active_piece.rotation += 1
        self.board.active_piece.rotate_clock()
        self.apply_action({"rotation": -1})

    def action_rotate_unclock(self, data):
        # self.board.active_piece.rotation -= 1
        self.board.active_piece.rotate_unclock()
        self.apply_action({"rotation": 1})

    def action_accelerate(self, data):
        self.board.active_piece.y += 1
        self.apply_action({"y": -1})

    def apply_action(self, correction):
        self.board.active_piece.calculate_blocks()
        if not self.board.active_piece.check_state(self.board.positions):
            if "x" in correction:
                self.board.active_piece.x += correction["x"]
            if "y" in correction:
                self.board.active_piece.y += correction["y"]
            if "rotation" in correction:
                if(correction["rotation"] > 0):
                    self.board.active_piece.rotate_clock()
                else:
                    self.board.active_piece.rotate_unclock()
        self.emit_state()

    def action_piece_fall(self, data):
        if self.board and self.board.active_piece:
            self.board.active_piece.y += 1
            self.board.active_piece.calculate_blocks()
            if not self.board.active_piece.check_state(self.board.positions):
                self.board.active_piece.y -= 1
                self.board.active_piece.calculate_blocks()
                self.board.calculate_piece_fall()
                if(self.board.lost == True):
                    self.state.LOSER
        self.emit_state()

    def emit_state(self):
        for subject in self.subjects:
            subject.emit('from_player', {
                "action": "board_state",
                "player_id": self.id,
                "board_state": self.board.get_board_state(),
                "player_state": self.json()
            })

    @classmethod
    def from_dict(self, data):
        return Player(data["name"], data["avatar"])

    def update(self, channel, data):
        if(channel == "to_player"):
            if 'player_id' in data and data['player_id'] == self.id:
                method = getattr(self, 'action_'+data['action'])
                if method:
                    method(data)

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "avatar": self.avatar,
            "state": self.state,
            "score": self.score,
            "count": self.count,
            "lines": self.lines,
            "tetris": self.tetris,
        }
