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
        # What row pawns go on
        if color == 'White':
            row_pawn, row_other = (6, 7)
        else:
            row_pawn, row_other = (1, 0)

        # Puts a pawn on every column on that row
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        # Knight
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))

        # Bishop
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))

        # Rook
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))

        # Queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))

        # King
        self.squares[row_other][4] = Square(row_other, 4, King(color))

b = board()
b._create()