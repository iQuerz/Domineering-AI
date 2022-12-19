#UI uradjen po ugledu na https://github.com/AlejoG10/python-chess-ai-yt
import pygame, sys
import GameEngine as Engine
import pymsgbox as msgbox

ROWS = COLS = 8 #default values
AI_TURN = 0 #0=Human-v-Human, 1=prvi igra AI, 2=drugi igra AI

#fetch from args
length = len(sys.argv)
if length <3:
    print("Uneli ste lose argumente! Tabla postavljena na podrazumevanu vrednost 8x8")
if length == 3:
    if int(sys.argv[1]) > 20 or int(sys.argv[2]) > 20:
        print("Maksimalne dimenzije su 20x20!")
        print("Tabla postavljena na podrazumevanu vrednost 8x8")
    else:
        ROWS = int(sys.argv[1])
        COLS = int(sys.argv[2])
elif length == 4:
    if int(sys.argv[1]) > 20 or int(sys.argv[2]) > 20:
        print("Maksimalne dimenzije su 20x20!")
        print("Tabla postavljena na podrazumevanu vrednost 8x8")
    else:
        ROWS = int(sys.argv[1])
        COLS = int(sys.argv[2])
        AI_TURN = int(sys.argv[3])
        print("Human vs Computer")

if AI_TURN == 0:
    print("Human vs Human")

WIDTH = COLS * 70
HEIGHT = ROWS * 70
SQSIZE = WIDTH // COLS #square size

PlayerOneImg = pygame.transform.scale(pygame.image.load("images/player_1.png"), (SQSIZE, (SQSIZE*2)))
PlayerTwoImg = pygame.transform.scale(pygame.image.load("images/player_2.png"), ((SQSIZE*2), SQSIZE))
    
def show_bg(surface, field):
    black = (0, 0, 0)
    white = (255, 255, 255)

    for row in range(ROWS):
        for col in range (COLS):
            if (row + col) % 2 == 0:
                color = (153,153,153) #gray
            else:
                color = (255,255,255) #white
            
            rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)                             
            pygame.draw.rect(surface, color, rect)
            
            #Font
            font = pygame.font.SysFont('calibri', 16)
            font_label = pygame.font.SysFont('calibri', 13) #font za numeraciju
            text = str(field[row][col][1])
            text = font.render(text, True, white)
            textRect = text.get_rect()
            
            #numaracija table
            lbl_row = font_label.render(str(ROWS-row), 1, black)
            lbl_pos_row = (2, 2 + row * SQSIZE)
            # blit
            surface.blit(lbl_row, lbl_pos_row)    
            
            lbl_col = font_label.render(get_alphacol(col), 1, black)
            lbl_pos_col = (col * SQSIZE + SQSIZE - 10, HEIGHT - 15)
            # blit
            surface.blit(lbl_col, lbl_pos_col)

            if field[row][col][0] == 1:
                surface.blit(PlayerOneImg, pygame.Rect(col*SQSIZE, (row-1)*SQSIZE, SQSIZE, 2*SQSIZE))
                textRect.center = ((col*SQSIZE)+(SQSIZE//2), ((row-1)*SQSIZE)+SQSIZE)
                surface.blit(text, textRect)
            
            elif field[row][col][0] == -2:
                surface.blit(PlayerTwoImg, pygame.Rect((col-1)*SQSIZE, row*SQSIZE, 2*SQSIZE, SQSIZE))
                textRect.center = (((col-1)*SQSIZE)+SQSIZE, ((row-1)*SQSIZE)+(SQSIZE*1.5))
                surface.blit(text, textRect)


def get_alphacol(col):
    ALPHACOLS = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U'}
    return ALPHACOLS[col]

def HoverPlayerOne(rows:int, cols:int, field, surface):
    if Engine.isMoveValid(rows, cols, field, 1):
        surface.blit(PlayerOneImg, pygame.Rect(cols*SQSIZE, (rows-1)*SQSIZE, SQSIZE, 2*SQSIZE))

def HoverPlayerTwo(rows:int, cols:int, field, surface):
    if Engine.isMoveValid(rows, cols, field, 2):
        surface.blit(PlayerTwoImg, pygame.Rect(cols*SQSIZE, rows*SQSIZE, 2*SQSIZE, SQSIZE))

def InvalidMoveAlert():
    msgbox.alert(text='You\'re trying to make an invalid move. Try again', title='Invalid move', button='OK')

def PlayerWonAlert(playerNum):
    msgbox.alert(text=f'Player {playerNum} won.', title='Good game.', button='OK')
