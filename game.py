import pygame
from CONST import *
from board import board
from dragger import Dragger
from square import Square
from config import Config
# This imports pygame and attributes from the relevent classes

class Game:
    def __init__(self):
        self.next_player = 'white'
        self.hovered_sqr = None
        self.board = board()
        self.dragger = Dragger()
        self.config = Config()
# This initilises the attributes of the class
    
    def show_bg(self, surface):

        theme = self.config.theme

        for row in range (ROWS):
            for col in range (COLS):
                # This alternates the colour of the squares
                if (row + col) % 2 == 0 :
                    color = theme.bg.light # light brown
                else:
                    color = theme.bg.dark # dark brown
                # This creates the rectangle for the board in pygame
                rect = (col*SQSIZE, row*SQSIZE, SQSIZE, SQSIZE)
                # This displays the pygame rectangle 
                pygame.draw.rect (surface, color, rect)
    # This method creates and shows the board using pygame
    
    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece
                    
                    if piece != self.dragger.piece:
                    # All Pieces
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)     
                        img_centre = col * SQSIZE + SQSIZE // 2
                        piece.texture_rect = img.get_rect(center=(img_centre, row * SQSIZE + SQSIZE // 2))
                        surface.blit(img, piece.texture_rect)

    def show_moves(self, surface):

        theme = self.config.theme

        # If the piece is being dragged
        if self.dragger.dragging:
            piece = self.dragger.piece

            # Loop through all the valid moves
            for move in piece.moves:
                #color
                color = theme.moves.light if (move.final.row + move.final.col) % 2 == 0 else theme.moves.dark
                #rect
                rect = (move.final.col * SQSIZE, move.final.row * SQSIZE, SQSIZE, SQSIZE)
                #blit
                pygame.draw.rect(surface, color, rect)

    def show_last_move(self, surface):

        theme = self.config.theme

        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final

            for pos in [initial, final]:
                # color
                color = theme.trace.light if (pos.row + pos.col) % 2 == 0 else theme.trace.dark
                # rect
                rect = (pos.col * SQSIZE, pos.row * SQSIZE, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)

    def show_hover(self,surface):
        if self.hovered_sqr:
            # color
            color = (180, 180, 180)
            #rect
            rect = (self.hovered_sqr.col * SQSIZE, self.hovered_sqr.row*SQSIZE, SQSIZE, SQSIZE)
            #blit
            pygame.draw.rect(surface, color, rect, width=3)

    # other methods
                
    def next_turn(self):
        self.next_player = 'white' if self.next_player == 'black' else 'black'

    def set_hover(self,  row, col):
        self.hovered_sqr = self.board.squares[row][col]

    def change_theme (self):
        self.config.change_theme()

    def sound_effect(self, captured=False):
        if captured:
            self.config.capture_sound.play()
        else:
            self.config.move_sound.play()