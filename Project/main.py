import pygame, sys
import GameEngine as Engine
from UserInterface import *

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Domineering')      #naziv prozora
Icon = pygame.image.load('images/logo.png')     #logo igrice/prozora
pygame.display.set_icon(Icon)
    
def resetGame(Field):
    pygame.display.set_caption('Domineering')   #naziv prozora
    Field = Engine.CreateMatrix(ROWS,COLS)      #resetujemo matricu
    Engine.CountMove = 1                        #resetujemo brojac poteza
    mainLoop()                                  #crtamo tablu i igrace iznova

def mainLoop():
    Field = Engine.CreateMatrix(ROWS,COLS)
    global screen
    global game
    
    while True:
        show_bg(screen, Field)
        
        for event in pygame.event.get():  
            if event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = location[0]//SQSIZE # x koordinata pozicije klika
                row = location[1]//SQSIZE # y koordinata pozicije klika
                if not Engine.placeDomino(row, col, Field): 
                    InvalidMoveAlert()
                else:    
                    Engine.nextPlayer()
                if Engine.getAvailableMovesNumber(Field) == 0:
                    PlayerWonAlert(Engine.playerOnMove%2+1)
                    break

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:                       
                    resetGame()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        #ovo se uvek izvrsava, nema nikakav if, samo se vidi ko je na potezu
        location = pygame.mouse.get_pos()
        col = location[0]//SQSIZE
        row = location[1]//SQSIZE
        if Engine.playerOnMove==1:
            HoverPlayerOne(row, col, Field, screen)
        elif Engine.playerOnMove==2:
            HoverPlayerTwo(row, col, Field, screen)
        pygame.display.update()

mainLoop()