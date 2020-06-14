import copy

class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.positions = [[(x, y, '.') for x in range(width)] for y in range(height)]
        self.active_piece =  None
        self.lost = False

    def add_piece(self, piece):
        self.active_piece = piece

    def calculate_piece_fall(self):
        # get all blocks from the fallen piece and save them
        reset_piece = False
        positions = copy.deepcopy(self.positions)
        for block in self.active_piece.blocks:
            positions[block.y][block.x] = (block.x, block.y, self.active_piece.shape)
            # piece reached bottom
            if block.y == len(positions) - 1:
                reset_piece = True
            # piece reached another piece
            if block.y + 1 < len(positions) and positions[block.y + 1][2] != '.':
                reset_piece = True
            # lost game
            if block.y  <  2:
                self.lost = True
        # check if any row is completed
        completed_rows = []
        for index, rows in enumerate(positions, start = 0):
            accumulator = True 
            for x, y, shape in rows:
                if shape == '.':
                    accumulator = False
            if accumulator == True:
                completed_rows.append(index)

        # take completed rows away and add new ones
        if len(completed_rows) > 0:
            for i in completed_rows:
                positions.pop(i)
                positions.insert(0, [(x, 0, '.') for x in range(len(positions[0]))])
            # reset positions (previous step messed (x, y) up with the removing and adding)
            for _y, row in enumerate(positions, start = 0):
                for _x, (x, y, shape) in enumerate(row, start = 0):
                    positions[_y][_x] = (_x, _y, shape)
            self.positions = positions
            # remove active piece
            self.active_piece = None
        if reset_piece == True:
            # remove active piece
            self.positions = positions
            self.active_piece = None

    def get_board_state(self):
        positions = copy.deepcopy(self.positions)
        for block in self.active_piece.calculate_blocks():
            positions[block.y][block.x] = (block.x, block.y, self.active_piece.shape)
        return positions

    def __str__(self):
        positions = self.get_board_state()

        output = '\n\n\n\n\n\n\n\n\n\n'
        for row in positions:
            output += '                                  '
            for x, y, shape in row:
                output += shape
            output += '\n'
        output += '\n\n\n\n\n\n\n\n\n\n\n\n'
        return output











            

    