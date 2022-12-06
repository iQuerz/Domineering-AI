#UI uradjen po ugledu na https://github.com/AlejoG10/python-chess-ai-yt
import pygame, sys
import GameEngine

ROWS = COLS = 8 #default values

AI_TURN = 0 #0=pvp, 1=prvi igra AI, 2=drugi

length = len(sys.argv)
if length >= 3:
    if int(sys.argv[1]) > 20 or int(sys.argv[2]) > 20:
        print("Maksimalne dimenzije su 20x20!")
        print("Tabla postavljena na podrazumevanu vrednost 8x8")
    else:
        ROWS = int(sys.argv[1])
        COLS = int(sys.argv[2])
elif length >= 4:
        AI_TURN = int(sys.argv[3])

WIDTH = COLS * 70
HEIGHT = ROWS * 70

SQSIZE = WIDTH // COLS #square size

class Game:

    PlayerOneImg = pygame.transform.scale(pygame.image.load("images/player_1.png"), (SQSIZE, (SQSIZE*2)))
    PlayerTwoImg = pygame.transform.scale(pygame.image.load("images/player_2.png"), ((SQSIZE*2), SQSIZE))
    black = (0, 0, 0)
    white = (255, 255, 255)
       
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
                font = pygame.font.SysFont('georgia', 16)
                font_label = pygame.font.SysFont('georgia', 13) #font za numeraciju
                text = str(field[row][col][1])
                text = font.render(text, True, self.white)
                textRect = text.get_rect()
                
                #numaracija table
                lbl_row = font_label.render(str(ROWS-row), 1, self.black)
                lbl_pos_row = (2, 2 + row * SQSIZE)
                # blit
                surface.blit(lbl_row, lbl_pos_row)    
                
                lbl_col = font_label.render(Game.get_alphacol(col), 1, self.black)
                lbl_pos_col = (col * SQSIZE + SQSIZE - 10, HEIGHT - 15)
                # blit
                surface.blit(lbl_col, lbl_pos_col)

                if field[row][col][0] == 1:
                    surface.blit(self.PlayerOneImg, pygame.Rect(col*SQSIZE, (row-1)*SQSIZE, SQSIZE, 2*SQSIZE))
                    textRect.center = ((col*SQSIZE)+(SQSIZE//2), ((row-1)*SQSIZE)+SQSIZE)
                    surface.blit(text, textRect)
                elif field[row][col][0] == 2:
                    surface.blit(self.PlayerTwoImg, pygame.Rect((col-1)*SQSIZE, row*SQSIZE, 2*SQSIZE, SQSIZE))
                    textRect.center = ((col*SQSIZE), ((row-1)*SQSIZE)+(SQSIZE*1.5))
                    surface.blit(text, textRect)
                
    @staticmethod
    def get_alphacol(col):
        ALPHACOLS = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u'}
        return ALPHACOLS[col]
                    
    def HoverPlayerOne(self, rows:int, cols:int, field, surface):
        if GameEngine.IsMoveValidOne(rows, cols, field):
           surface.blit(self.PlayerOneImg, pygame.Rect(cols*SQSIZE, (rows-1)*SQSIZE, SQSIZE, 2*SQSIZE))

    def HoverPlayerTwo(self, rows:int, cols:int, field, surface):
        if GameEngine.IsMoveValidTwo(rows, cols, field):
            surface.blit(self.PlayerTwoImg, pygame.Rect(cols*SQSIZE, rows*SQSIZE, 2*SQSIZE, SQSIZE))