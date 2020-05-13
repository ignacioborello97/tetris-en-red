import unittest
from .board import Board
from ..piece.piece import Piece

class BoardTestCase(unittest.TestCase):
    def setUp(self):
        self.width = 10
        self.height = 20
        self.board_instance = Board(self.height, self.width)

    def tearDown(self):
        self.board_instance = None

    def test_initial_values(self):
        # check height initialization
        self.assertIsNotNone(self.board_instance.height, 'height must not be null')
        self.assertEqual(self.board_instance.height, self.height, 'height must be equal to height parameter')
        # check width initialization
        self.assertIsNotNone(self.board_instance.width, 'width must not be null')
        self.assertEqual(self.board_instance.width, self.width, 'width must be equal to width parameter')
        # check positions initialization
        self.assertIsNotNone(self.board_instance.positions, 'board positions must not be null')
        self.assertIsInstance(self.board_instance.positions, list, 'board positions must be a list list')
        self.assertEqual(len(self.board_instance.positions), self.height, 'board positions have height elements')
        for row in self.board_instance.positions:
            self.assertIsInstance(row, list, 'each element of board positions must be a list')
            self.assertEqual(len(row), self.width, 'each element of board positions must have width elements')
        # check active piece initialization
        self.assertIsNone(self.board_instance.active_piece, 'active piece must start empty (None)')
        # check lost initialization
        self.assertFalse(self.board_instance.lost, 'th lsot flag must start as False')

    def test_add_piece(self):
        # create a test piece
        piece = Piece('L', 0, 5)
        # add the test piece
        self.board_instance.add_piece(piece)
        #check if the piece was set correctly
        self.assertIsNotNone(self.board_instance.active_piece, 'piece must be set')
        self.assertIs(self.board_instance.active_piece, piece, 'piece must be the same as the input')

    def test_calculate_piece_fall(self):
        # define mock positions
        self.board_instance.positions = [[(x,y,'.') for x in range(self.width)] for y in range(self.height)]
        for j in range(1,4):
            for i in range(len(self.board_instance.positions[len(self.board_instance.positions) - j])): # setting up something like this                                                                                                                  
                self.board_instance.positions[len(self.board_instance.positions) - j][i] = (            #       .......
                    self.board_instance.positions[len(self.board_instance.positions) - j][i][0],        #       .......
                    self.board_instance.positions[len(self.board_instance.positions) - j][i][1], 'X')   #       .......
                                                                                                        #       .......
        for i in range(len(self.board_instance.positions[len(self.board_instance.positions) - 4])):     #       .......
            if self.board_instance.positions[len(self.board_instance.positions) - 4][i][0] != 5:        #       XXX.XXX
                self.board_instance.positions[len(self.board_instance.positions) - 4][i] = (            #       XXXXXXX
                    self.board_instance.positions[len(self.board_instance.positions) - 4][i][0],        #       XXXXXXX
                    self.board_instance.positions[len(self.board_instance.positions) - 4][i][1],'X')    #       XXXXXXX

        # generate mock falling piece
        piece = Piece('T', 4, 0)
        self.board_instance.add_piece(piece)

        # execute method
        self.board_instance.calculate_piece_fall()
        
        # test if las 3 lines got deleted  and 4th was "moved" lines
        for i in range(4, 2):
            self.assertEqual(
                self.board_instance.positions[len(self.board_instance.positions) - i],
                [(x,len(self.board_instance.positions) - i,'.') for x in range(self.width)],
                'line '+str(len(self.board_instance.positions) - i)+' must be deleted'
            )
        
        # test if last line is the incomplete one
        self.assertEqual(
            self.board_instance.positions[len(self.board_instance.positions) - 1],
            [(x,len(self.board_instance.positions) - 1,'X' if x != 5 else '.') for x in range(self.width)],
            'line '+str(len(self.board_instance.positions) - 1)+' must have the incomplete one'
        )

        # generate mock fallen piece
        piece = Piece('T', 4, len(self.board_instance.positions) - 3)
        self.board_instance.add_piece(piece)

        # execute method
        self.board_instance.calculate_piece_fall()

        # test if last line got deleted 
        self.assertEqual(
            self.board_instance.positions[len(self.board_instance.positions) - 1],
            [(x,len(self.board_instance.positions) - 1, 'T' if x in [4,5,6] else '.') for x in range(self.width)],
            'line '+str(len(self.board_instance.positions) - 1)+' must be empty'
        )
        
        #profit?


if __name__ == '__main__':
    unittest.main()
        