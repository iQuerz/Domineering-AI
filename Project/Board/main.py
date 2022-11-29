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
                    if GameState == True:
                        location = pygame.mouse.get_pos()
                        x = location[0]//SQSIZE
                        y = location[1]//SQSIZE
                        moveCounter = 0
                        Change = GameEngine.PlayerOneMove(y,x, Field)                       
                        if Change:
                            pygame.display.set_caption('Player 2 is on the move') #when state changes other player is on the move
                            GameState = False
                            moveCounter+=1
                    else:
                        location = pygame.mouse.get_pos()
                        x = location[0]//SQSIZE
                        y = location[1]//SQSIZE
                        Change = GameEngine.PlayerTwoMove(y,x, Field)                       
                        if Change:
                            pygame.display.set_caption('Player 1 is on the move') #when state changes other player is on the move
                            GameState = True 
                            moveCounter+=1                         
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

            
            #ovo se uvek izvrsava nma nikakv if samo se vidi ko je na potez
            location = pygame.mouse.get_pos()
            x = location[0]//SQSIZE
            y = location[1]//SQSIZE
            if GameState == True:
                game.HoverPlayerOne(x,y,Field,screen)
            else:
                game.HoverPlayerTwo(x,y,Field,screen)         
            pygame.display.set_caption('Winner is: Player')
            pygame.display.update()  

main = Main()
main.mainLoop()