from CONST import *
import pygame
# This imports pygame and attributes from the relevent classes

class Game:
    def __init__(self):
        pass
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
                    
