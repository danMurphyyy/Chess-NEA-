from CONST import *
from square import Square
from piece import *

class board:

    def __init__(self):
        self.squares = [[0,0,0,0,0,0,0,0] for col in range (COLS)]

        self._create()

    def _create(self):
        for row in range (ROWS):
            for col in range (COLS):
                self.squares [row] [col] = Square(row, col)

    def _add_pieces(self, color):
        if color == 'White':
            row_pawn, row_other = (6, 7)
        else:
            row_pawn, row_other = (1, 0)

        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))



b = board()
b._create()