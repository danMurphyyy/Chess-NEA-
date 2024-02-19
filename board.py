from CONST import *
from square import Square

class board:

    def __init__(self):
        self.squares = []

    def _create(self):
        self.squares = [[0,0,0,0,0,0,0,0] for col in range (COLS)]
        
        for row in range (ROWS):
            for col in range (COLS):
                self.squares [row] [col] = Square(row, col)

    def _add_pieces(self, color):
        pass

b = board()
b._create()