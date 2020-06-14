import string, random
from ..board.board import Board

class Player:

    @classmethod
    def generate_id(cls):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(6))

    IDDLE = 'IDDLE'
    PENDING = 'PENDING'
    READY = 'READY'
    PLAYING = 'PLAYING'
    SPECTATING = 'SPECTATING'

    def __init__(self, name, avatar):
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

    def has_piece(self):
        return self.board.active_piece is not None

    def action_move_left(self):
        self.board.active_piece.x -= 1
        self.apply_action({"x": 1})
    
    def action_move_right(self):
        self.board.active_piece.x += 1
        self.apply_action({"x": -1})
    
    def action_rotate_clock(self):
        # self.board.active_piece.rotation += 1
        self.board.active_piece.rotate_clock()
        self.apply_action({"rotation": -1})
    
    def action_rotate_unclock(self):
        # self.board.active_piece.rotation -= 1
        self.board.active_piece.rotate_unclock()
        self.apply_action({"rotation": 1})
    
    def action_accelerate(self):
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