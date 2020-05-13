import threading
import random

from pynput import keyboard
from server.models.block.block import Block
from server.models.board.board import Board
from server.models.piece.piece import Piece

my_board = Board(20, 10)

def get_random_piece():
    return random.choice(['S','Z','L','J','T','I'])

def on_press(key):
    try:
        if(key.char == 'z'):
            my_board.active_piece.rotate_unclock()
            my_board.active_piece.calculate_blocks()
            if not my_board.active_piece.check_state(my_board.positions):
                my_board.active_piece.rotate_clock()
        if(key.char == 'x'):
            my_board.active_piece.rotate_unclock()
            my_board.active_piece.calculate_blocks()
            if not my_board.active_piece.check_state(my_board.positions):
                my_board.active_piece.rotate_clock()

    except AttributeError:
        if(key == keyboard.Key.right):
            my_board.active_piece.x += 1
            my_board.active_piece.calculate_blocks()
            if not my_board.active_piece.check_state(my_board.positions):
                my_board.active_piece.x -= 1
        if(key == keyboard.Key.left):
            my_board.active_piece.x -= 1
            my_board.active_piece.calculate_blocks()
            if not my_board.active_piece.check_state(my_board.positions):
                my_board.active_piece.x += 1
        if(key == keyboard.Key.down):
            my_board.active_piece.y += 1
            my_board.active_piece.calculate_blocks()
            if not my_board.active_piece.check_state(my_board.positions):
                my_board.active_piece.y -= 1


#threading.Timer(0.13, ).start()
def tick():
    if my_board.active_piece == None:
        my_board.add_piece(Piece(get_random_piece()))
    else:
        my_board.active_piece.y += 1
        my_board.active_piece.calculate_blocks()
        if not my_board.active_piece.check_state(my_board.positions):
            my_board.active_piece.y -= 1
            my_board.active_piece.calculate_blocks()
            my_board.calculate_piece_fall()
            if(my_board.lost == True):
                print('T moriste xd')
                return 
            if(my_board.active_piece == None):
                my_board.add_piece(Piece(get_random_piece()))
        
    print(my_board)
    threading.Timer(0.4, tick).start()

# Non blocking keyboard listener
    

