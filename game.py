import pygame
from CONST import *
from board import board
from dragger import Dragger
from square import Square
# This imports pygame and attributes from the relevent classes

class Game:
    def __init__(self):
        self.next_player = 'white'
        self.board = board()
        self.dragger = Dragger()
# This initilises the attributes of the class
    
    def show_bg(self, surface):
        for row in range (ROWS):
            for col in range (COLS):
                # This alternates the colour of the squares
                if (row + col) % 2 == 0 :
                    color = (189,154,122) # light brown
                else:
                    color = (101, 67, 33) # dark brown
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
        # If the piece is being dragged
        if self.dragger.dragging:
            piece = self.dragger.piece

            # Loop through all the valid moves
            for move in piece.moves:
                #color
                color = '#C86464' if (move.final.row + move.final.col) % 2 == 0 else '#C84646'
                #rect
                rect = (move.final.col * SQSIZE, move.final.row * SQSIZE, SQSIZE, SQSIZE)
                #blit
                pygame.draw.rect(surface, color, rect)

    # other methods
                
    def next_turn(self):
        self.next_player = 'white' if self.next_player == 'black' else 'black'