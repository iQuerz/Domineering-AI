import pygame, sys
import GameEngine
from GameEngine import IsMoveValidOne, IsMoveValidTwo
from const import *
from game import Game

class Main:
    def __init__ (self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Domineering')      #naziv prozora
        Icon = pygame.image.load('images/logo.png')     #logo igrice/prozora
        pygame.display.set_icon(Icon)     
        self.game = Game()

    def mainLoop(self):
        
        Field = GameEngine.CreateMatrix(ROWS,COLS)
        screen = self.screen
        game = self.game
        GameState = True
        
        while True:
            
            # show methods
            game.show_bg(screen, Field)
                
            for event in pygame.event.get():  
                if event.type == pygame.MOUSEBUTTONDOWN:
                    location = pygame.mouse.get_pos()
                    print(location)
                    col = location[0]//SQSIZE # x koordinata pozicije klika
                    row = location[1]//SQSIZE # y koordinata pozicije klika

                    if GameState == True:
                        if GameEngine.PlayerOneMove(row,col, Field):
                            pygame.display.set_caption('Player 2 is on the move') #when state changes other player is on the move
                            GameState = False
                    else:
                        if GameEngine.PlayerTwoMove(row,col, Field):
                            pygame.display.set_caption('Player 1 is on the move') #when state changes other player is on the move
                            GameState = True

                # key press
                elif event.type == pygame.KEYDOWN:
                     # reseting a game
                    if event.key == pygame.K_r: #ako se klikne R resetuje se igrica
                        game.reset()
                        game = self.game
                
                # quit application
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                          
            #pygame.display.set_caption('Winner is: Player' + )
            pygame.display.update()

main = Main()
main.mainLoop()