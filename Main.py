import sys
import pygame
from game import Game
from CONST import *
from board import board
# Imports relevent to the main class

class main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # size of window
        pygame.display.set_caption('Chess')  
        # title of window
        self.game = Game()
        # game class
        self.board = board()

    def mainloop(self):

        screen = self.screen
        game = self.game
        dragger = self.game.dragger
        board = self.game.board

        while True:
        # Loops indefinatley 

            Game.show_bg(self, screen)
            Game.show_pieces(self, screen)
            # calls the method to show the board and pieces from the game class

            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():

                # Mouse Pressed
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clickedRow = dragger.mouseY // SQSIZE
                    clickedCol = dragger.mouseX // SQSIZE

                    # Does clicked square have a piece
                    if board.squares[clickedRow][clickedCol].has_piece():
                        piece = board.squares[clickedRow][clickedCol].piece
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)

                # Mouse Motion
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        dragger.update_blit(screen)


                # Mouse released
                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()

                # Quit Application
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # If statement in a for loop to exit out of pygame when cross is clicked


            pygame.display.update()



main = main()
main.mainloop()
#calls the mainloop method so the game runs when the program is run