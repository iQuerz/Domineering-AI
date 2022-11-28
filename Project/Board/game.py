#deo koda preuzet sa https://github.com/AlejoG10/python-chess-ai-yt
import pygame

from const import *
from board import Board
from move import Move
from square import Square

class Game:

    PlayerOneImg = pygame.transform.scale(pygame.image.load("images/player_1.png"),(SQSIZE,(SQSIZE*2)))
    PlayerTwoImg = pygame.transform.scale(pygame.image.load("images/player_2.png"),((SQSIZE*2),SQSIZE))

    def __init__(self):
        self.next_player = 1
        self.hovered_sqr = None
        self.board = Board()
        #self.move = Move(initial,final)
        
    def show_bg(self, surface, field):

        for row in range(ROWS):
            for col in range (COLS):
                if (row + col) % 2 == 0:
                    color = (169,169,169) #gray
                else:
                    color = (255,250,250)  #white
                
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)  
                
                pygame.draw.rect(surface, color, rect) 
                if field[row][col] == 1:
                    surface.blit(self.PlayerOneImg, pygame.Rect(col*SQSIZE,(row-1)*SQSIZE,SQSIZE,2*SQSIZE))
                elif field[row][col] == 2:
                    surface.blit(self.PlayerTwoImg, pygame.Rect((col-1)*SQSIZE,row*SQSIZE,2*SQSIZE,SQSIZE))

                
      
    def reset(self):
        self.__init__() 