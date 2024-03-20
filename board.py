from CONST import *
from square import Square
from piece import *
from square import Square
from move import Move

class board:

    def __init__(self):
        self.squares = [[0,0,0,0,0,0,0,0] for col in range (COLS)]
        squares = self.squares

        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def calc_moves(self, piece, row, col):
        # This method will calculate all possible (valid) moves
        # of a specific piece on a specific position

        def knight_moves():
            # There are 8 possible moves for a kinght
            possible_moves = [
                (row-2, col+1),
                (row-1, col+2),
                (row+1, col+2),
                (row+2, col-1),
                (row+2, col-1),
                (row+1, col-2),
                (row-1, col-2),
                (row-2, col-1),
            ]

            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move

                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares(possible_move_row)(possible_move_col).isempty_or_rival(piece.color):
                        # Create the squares of the move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        # create a new move
                        move = Move(initial, final)
                        piece.add_move(move)

        if isinstance(piece, Pawn):
            pass

        elif isinstance(piece, Knight):
            knight_moves()

        elif isinstance(piece, Bishop):
            pass

        elif isinstance(piece, Rook):
            pass

        elif isinstance(piece, Queen):
            pass

        elif isinstance(piece, King):
            pass

    def _create(self):
        for row in range (ROWS):
            for col in range (COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        # What row pawns go on
        if color == 'white':
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