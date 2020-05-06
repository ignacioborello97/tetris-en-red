import unittest
from board import Board

class BoardTestCase(unittest.TestCase):
    def setUp(self):
        self.board_instance = Board(20,10)

    def tearDown(self):
        self.board_instance = None

    def test_initial_values(self):
        self.assertIsNotNone(self.board_instance.x)
        self.assertIsNotNone(self.board_instance.y)
        self.assertIsNotNone(self.board_instance.positions)
        self.assertIsNone(self.board_instance.active_piece)
        self.assertIsNone(self.board_instance.lost)
        