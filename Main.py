import sys
from pygame import *
from game import Game
from CONST import *
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

    def mainloop(self):
        while True:
        # Loops indefinatley 

            self.game.show_bg(self.screen)
            # calls the method to show the board from the game class

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                # If statement in a for loop to exit out of pygame when cross is clicked


            pygame.display.update()



main = main()
main.mainloop()
#calls the mainloop method so the game runs when the program is run