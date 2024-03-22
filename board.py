from CONST import *
from square import Square
from piece import *
from square import Square
from move import Move

class board:

    def __init__(self):
        self.squares = [[0,0,0,0,0,0,0,0] for col in range (COLS)]
        squares = self.squares
        self.last_move = None
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def move(self, piece, move):
        initial = move.initial
        final = move.final

        # Console board move update
        self.squares[initial.row][initial.col].piece = None
        self.squares[final.row][final.col].piece = piece

        # move
        piece.moved = True

        # clear valid moves
        piece.clear_moves()

        # set last move
        self.last_move = move

    def valid_move(self, piece, move):
        return move in piece.moves

    def calc_moves(self, piece, row, col):
        # This method will calculate all possible (valid) moves
        # of a specific piece on a specific position

        def pawn_moves():
            #Steps
            if piece.moved:
                steps = 1
            else:
                steps = 2

            # Vertical moves
            start = row + piece.dir
            end = row + (piece.dir * (1 + steps))
            for possible_move_row in range(start, end, piece.dir):
                if Square.in_range(possible_move_row):
                    if self.squares[possible_move_row][col].isempty():
                        # Create initial and final move squares
                        initial = Square(row, col)
                        final = Square(possible_move_row, col)
                        # Create a new move
                        move = Move(initial, final)
                        piece.add_move(move)
                    # Blocked
                    else: 
                        break
                # Not in Range
                else: 
                    break

                
            # Diagonal Moves
            possible_move_row = row + piece.dir
            possible_move_cols = [col-1, col+1]
            for possible_move_col in possible_move_cols:
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                        # create initial and final move squares
                        initial = Square(row,col)
                        final = Square(possible_move_row, possible_move_col)
                            # create a new move
                        move = Move(initial, final)
                            #append new move
                        piece.add_move(move)

            # Pawn Promotion
                        
            # Pawn En Passant

        def knight_moves():
            # There are 8 possible moves for a kinght
            possible_moves = [
                (row-2, col-1),
                (row-1, col+2),
                (row+1, col+2),
                (row+2, col-1),
                (row+2, col+1),
                (row+1, col-2),
                (row-1, col-2),
                (row-2, col+1),
            ]

            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move

                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.color):
                        # Create the squares of the move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        # create a new move
                        move = Move(initial, final)
                        piece.add_move(move)

        def straight_line_moves(incrs):
            for incr in incrs:
                row_incr, col_incr = incr
                possible_move_row = row + row_incr
                possible_move_col = col + col_incr

                while True:
                    if Square.in_range(possible_move_row, possible_move_col):

                        # create squares of the possible new move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)

                        #create a possible new move
                        move = Move(initial, final)

                        # empty
                        if self.squares[possible_move_row][possible_move_col].isempty():
                            # append a new move
                            piece.add_move(move)
                    
                        # has enemy piece
                        if self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                            piece.add_move(move)
                            break

                        # has team piece
                        if self.squares[possible_move_row][possible_move_col].has_team_piece(piece.color):
                            break
                    else:
                        break

                    # incrementing incrs
                    possible_move_row, possible_move_col = possible_move_row + row_incr, possible_move_col + col_incr
                    
        def king_moves():
            
            # Normal Moves

            adjs = [
                (row-1, col+0), # up
                (row-1, col+1), # up-right
                (row+0, col+1), # right
                (row+1, col+1), # down-right
                (row+1, col+0), # down
                (row+1, col-1), # down-left
                (row+0, col-1), # left
                (row-1, col-1), # up-left
            ]

            for possible_move in adjs:
                possible_move_row, possible_move_col = possible_move

                if Square.in_range(possible_move_row,possible_move_col):
                    if self. squares[possible_move_row][possible_move_col].isempty_or_rival(piece.color):
                        # Create the squares of the move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        # create a new move
                        move = Move(initial, final)
                        piece.add_move(move)

            # Castling moves
                        
            # Queen-side Castling
                        
            # King-side Castling
                        
            

        if isinstance(piece, Pawn):
            pawn_moves()

        elif isinstance(piece, Knight):
            knight_moves()

        elif isinstance(piece, Bishop):
            straight_line_moves([
                (-1, 1), # up-right
                (-1, -1), # up-left
                (1, 1), # down-right
                (1, -1), # down-left
            ])

        elif isinstance(piece, Rook):
            straight_line_moves([
                (1, 0), # down
                (-1, 0), # up
                (0, 1), # right
                (0, -1), # left
            ])

        elif isinstance(piece, Queen):
            straight_line_moves([
                (-1, 1), # up-right
                (-1, -1), # up-left
                (1, 1), # down-right
                (1, -1), # down-left
                (1, 0), # down
                (-1, 0), # up
                (0, 1), # right
                (0, -1), # left
            ])

        elif isinstance(piece, King):
            king_moves()

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