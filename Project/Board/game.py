#deo koda preuzet sa https://github.com/AlejoG10/python-chess-ai-yt
import pygame

from const import *
from board import Board
from move import Move
from square import Square

class Game:

    def __init__(self):
        self.next_player = 1
        self.hovered_sqr = None
        self.board = Board()
        #self.move = Move(initial,final)
    
    def show_text(self, surface): #probao sam da ispisem text pored table
                                       
        white = (255, 255, 255)
        black = (0, 0, 0)      
        X = 500
        Y = 500      

        # create a font object.
        # 1st parameter is the font file
        # which is present in pygame.
        # 2nd parameter is size of the font
        font = pygame.font.Font('freesansbold.ttf', 28)
        # create a text surface object,
        # on which text is drawn on it.
        text = font.render('Unesi broj kolona:', True, black, None)       
        text2 = font.render('Unesi broj vrsta:', True, black, None)  
        # create a rectangular object for the
        # text surface object
        textRect = text.get_rect()
        textRect2 = text2.get_rect()
        # set the center of the rectangular object.
        textRect.center = (X // 2, Y // 2.2)
        textRect2.center = (X // 2, Y // 2)
        # completely fill the surface object
        # with white color
              
        # copying the text surface object
        # to the display surface object
        # at the center coordinate.
        surface.blit(text, textRect)
        surface.blit(text2, textRect2)
        
    def show_bg(self, surface):
        
        for row in range(ROWS):
            for col in range (COLS):
                if (row + col) % 2 == 0:
                    color = (169,169,169) #gray
                else:
                    color = (255,250,250)  #white
                
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)  
                
                pygame.draw.rect(surface, color, rect) 
        
    def reset(self):
        self.__init__() 