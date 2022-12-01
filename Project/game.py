#deo koda preuzet sa https://github.com/AlejoG10/python-chess-ai-yt
import pygame
import GameEngine
from const import *

class Game:

    PlayerOneImg = pygame.transform.scale(pygame.image.load("images/player_1.png"), (SQSIZE, (SQSIZE*2)))
    PlayerTwoImg = pygame.transform.scale(pygame.image.load("images/player_2.png"), ((SQSIZE*2), SQSIZE))
    black = (0, 0, 0)
    white = (255, 255, 255)

    def __init__(self):
        pass
        
    def show_bg(self, surface, field):
        for row in range(ROWS):
            for col in range (COLS):
                if (row + col) % 2 == 0:
                    color = (153,153,153) #gray
                else:
                    color = (255,250,250)  #white
                
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)  
                
                pygame.draw.rect(surface, color, rect) 

                #Font
                font = pygame.font.Font('freesansbold.ttf', 18)
                text = str(field[row][col][1]+1)
                text = font.render(text, True, self.white)
                textRect = text.get_rect()

                if field[row][col][0] == 1:
                    surface.blit(self.PlayerOneImg, pygame.Rect(col*SQSIZE, (row-1)*SQSIZE, SQSIZE, 2*SQSIZE))
                    textRect.center = ((col*SQSIZE)+(SQSIZE//2), ((row-1)*SQSIZE)+SQSIZE)
                    surface.blit(text, textRect)
                elif field[row][col][0] == 2:
                    surface.blit(self.PlayerTwoImg, pygame.Rect((col-1)*SQSIZE, row*SQSIZE, 2*SQSIZE, SQSIZE))
                    textRect.center = ((col*SQSIZE), ((row-1)*SQSIZE)+(SQSIZE*1.5))
                    surface.blit(text, textRect)

    def HoverPlayerOne(self, rows:int, cols:int, field, surface):
        if GameEngine.IsMoveValidOne(rows, cols, field):
           surface.blit(self.PlayerOneImg, pygame.Rect(cols*SQSIZE, (rows-1)*SQSIZE, SQSIZE, 2*SQSIZE)) 

    def HoverPlayerTwo(self, rows:int, cols:int, field, surface):
        if GameEngine.IsMoveValidTwo(rows, cols, field):
            surface.blit(self.PlayerTwoImg, pygame.Rect(cols*SQSIZE, rows*SQSIZE, 2*SQSIZE, SQSIZE))           
      
    def reset(self):
        self.__init__()