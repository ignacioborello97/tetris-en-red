import unittest
import random
from .piece import Piece


class PieceTestCase(unittest.TestCase):
    def setUp(self):
        self.shape = random.choice(['S','Z','L','J','T','I'])
        self.piece = Piece(self.shape)

    def tearDown(self):
        self.board_instance = None

    def test_default_values(self):
        # nothing is null
        self.assertIsNotNone(self.piece.shape, 'shape must not be null')
        self.assertIsNotNone(self.piece.x, 'x must not be null')
        self.assertIsNotNone(self.piece.y, 'y must not be null')
        self.assertIsNotNone(self.piece.rotation, 'rotation must not be null')
        self.assertIsNotNone(self.piece.template, 'template must not be null')
        self.assertIsNotNone(self.piece.blocks, 'blocks must not be null')
        # check values
        self.assertEqual(self.piece.shape, self.shape,'shape must be same as input')
        self.assertEqual(self.piece.x, 5,'x must be five')
        self.assertEqual(self.piece.y, 0,'y must be zero')
        self.assertEqual(self.piece.rotation, 0,'rotation must be zero')
        #self.assertEqual(self.piece.template, Piece.templates[self.piece][0],'template must be initial one')

    def test_rotate_clock(self):
        # save previous rotation
        prev_rotation = self.piece.rotation
        # rotate piece clockwise
        self.piece.rotate_clock()
        # check rotation
        self.assertEqual(self.piece.rotation, prev_rotation + 1, 'rotation must augment')
    
    def test_rotate_unclock(self):
        # save previous rotation
        prev_rotation = self.piece.rotation
        # rotate piece clockwise
        self.piece.rotate_unclock()
        # check rotation
        self.assertEqual(self.piece.rotation, prev_rotation - 1, 'rotation must decrement')

    def test_calculate_blocks(self):
        expected_coords = {
            "T":[(5, 1), (6, 1), (7, 1), (6, 2)],
            "L":[(6, 0), (6, 1), (6, 2), (7, 2)],
            "S":[(6, 0), (6, 1), (7, 1), (7, 2)],
            "J":[(6, 0), (6, 1), (5, 2), (6, 2)],
            "I":[(5, 1), (6, 1), (7, 1), (8, 1)],
            "Z":[(7, 0), (6, 1), (7, 1), (6, 2)],
        }
        # generate list of positions
        block_list = [(block.x, block.y) for block in self.piece.calculate_blocks()]
        # check if it's value is the expected one
        self.assertEqual(expected_coords[self.piece.shape], block_list, 'piece blocks must corresponds to letters on the shape template')

    def test_check_state(self):
        # test grids
        positions = [[(x, y, 'P') for x in range(10)] for y in range(20)] # full grid positions
        self.assertFalse(self.piece.check_state(positions), 'Full grid must return False')
        
        positions = [[(x, y, 'P' if y == 1 else '.') for x in range(10)] for y in range(20)] # grid positions with occupied block
        self.assertFalse(self.piece.check_state(positions), 'Occupied block must return False')
        
        positions = [[(x, y, '.') for x in range(10)] for y in range(20)] # empty grid positions
        self.assertTrue(self.piece.check_state(positions), 'Full grid must return True')

        # test positions
        self.piece.y = 20
        self.piece.calculate_blocks()
        self.assertFalse(self.piece.check_state(positions), 'Index out of bound must return False')
        
        self.piece.y = -2
        self.piece.calculate_blocks()
        self.assertFalse(self.piece.check_state(positions), 'Index out of bound must return False')
        
        self.piece.y = 5
        self.piece.x = -2
        self.piece.calculate_blocks()
        self.assertFalse(self.piece.check_state(positions), 'Index out of bound must return False')
        
        self.piece.x = 10
        self.piece.calculate_blocks()
        self.assertFalse(self.piece.check_state(positions), 'Index out of bound must return False')

