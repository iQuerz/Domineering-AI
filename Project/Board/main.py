import pygame, sys

from const import *
from game import Game

class Main:
    def __init__ (self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Domineering')       
        self.game = Game()        
       
        
    def mainLoop(self):
        
        display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
        screen = self.screen
        game = self.game

        while True:
            # show methods
            game.show_bg(screen)
            game.show_text(display_surface)
            for event in pygame.event.get():   
                # key press
                if event.type == pygame.KEYDOWN:

                     # reseting a game
                    if event.key == pygame.K_r:
                        game.reset()
                        game = self.game
                        board = self.game.board

                # quit application
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()  

main = Main()
main.mainLoop()    