from CONST import *
import pygame
from board import board
# This imports pygame and attributes from the relevent classes

class Game:
    def __init__(self):
        self.board = board()
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
                    try:
                        img = pygame.image.load(piece.texture)
                    except pygame.error as e:
                        print(f"Error loading image for {piece}: {e}")
                        continue
                    
                    img_centre = col * SQSIZE + SQSIZE // 2
                    piece.texture_rect = img.get_rect(center=(img_centre, row * SQSIZE + SQSIZE // 2))
                    surface.blit(img, piece.texture_rect)