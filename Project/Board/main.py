import pygame, sys
import GameEngine
from const import *
from game import Game

class Main:
    def __init__ (self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Domineering')       
        self.game = Game()


    def mainLoop(self):
        
        Field = GameEngine.CreateMatrix(ROWS,COLS)
        display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
        screen = self.screen
        game = self.game
        GameState = True

        while True:
            
            # show methods
            game.show_bg(screen, Field)
           #game.show_text(display_surface)
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
                elif event.type == pygame.MOUSEBUTTONUP:
                    if GameState == True:
                        location = pygame.mouse.get_pos()
                        x = location[0]//SQSIZE
                        y = location[1]//SQSIZE
                        Change = GameEngine.PlayerOneMove(y,x, Field)
                        if Change:
                                GameState = False
                    else:
                        location = pygame.mouse.get_pos()
                        x = location[0]//SQSIZE
                        y = location[1]//SQSIZE
                        Change = GameEngine.PlayerTwoMove(y,x, Field)
                        if Change:
                                GameState = True


            pygame.display.update()  

main = Main()
main.mainLoop()