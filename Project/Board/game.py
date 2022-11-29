#deo koda preuzet sa https://github.com/AlejoG10/python-chess-ai-yt
import pygame
from const import *

class Game:

    PlayerOneImg = pygame.transform.scale(pygame.image.load("images/player_1.png"),(SQSIZE,(SQSIZE*2)))
    PlayerTwoImg = pygame.transform.scale(pygame.image.load("images/player_2.png"),((SQSIZE*2),SQSIZE))

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
                if field[row][col][0] == 1:
                    surface.blit(self.PlayerOneImg, pygame.Rect(col*SQSIZE, (row-1)*SQSIZE, SQSIZE, 2*SQSIZE))
                elif field[row][col][0] == 2:
                    surface.blit(self.PlayerTwoImg, pygame.Rect((col-1)*SQSIZE, row*SQSIZE, 2*SQSIZE, SQSIZE))

    
    def show_winner(self, surface): #ispisivanje ko je pobednik
                                       
        white = (255, 255, 255)
        black = (0, 0, 0)        

        # create a font object.
        # 1st parameter is the font file
        # which is present in pygame.
        # 2nd parameter is size of the font
        font = pygame.font.Font('freesansbold.ttf', 28)
        # create a text surface object,
        # on which text is drawn on it.
        text = font.render('Player wins', True, black, white)
         
        # create a rectangular object for the
        # text surface object
        textRect = text.get_rect()
        
        # set the center of the rectangular object.
        textRect.center = (WIDTH // 2, HEIGHT // 2.2)
        
        # completely fill the surface object
        # with white color
              
        # copying the text surface object
        # to the display surface object
        # at the center coordinate.
        surface.blit(text, textRect)         
      
    def reset(self):
        self.__init__()