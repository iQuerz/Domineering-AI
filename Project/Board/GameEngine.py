#imports
import pygame
from const import *
import AI
import UserInterface as UserInterface
from game import Game
from tkinter import *  
from tkinter import messagebox  
    
CountMove = 0
#trenutno ima duplikati svih funkcija za svakog igraca jer mi bilo lakse tako da testiram 
def CreateMatrix(rows: int, cols: int):
    Matrix = [[(0,0) for x in range(cols)] for y in range(rows)]
    return Matrix

def IsMoveValidOne(rows : int, cols : int, Mat):
    if Mat[rows-1][cols][0] == 0 and Mat[rows][cols][0] == 0 and rows != 0:
        return True
    else:
        return False

def IsMoveValidTwo(rows : int, cols : int, Mat):
    if cols >= len(Mat[0])-1:
        return False
    if Mat[rows][cols+1][0] == 0 and Mat[rows][cols][0] == 0:
        return True
    else:
        return False

def CalcAvalaibleMovesPlayerOne(Mat):
    count = 0
    for x in range(1, len(Mat)):
        #print(x)
        for i in range(len(Mat[0])):
            #print(i)
            if IsMoveValidOne(x,i,Mat):
                count+=1
    return count

def CalcAvalaibleMovesPlayerTwo(Mat):
    count = 0
    for x in range(len(Mat)):
        #print(x)
        for i in range(len(Mat[0])-1):
            #print(i)
            if IsMoveValidTwo(x,i,Mat):
                count+=1
    return count
    
def PlayerOneMove(rows : int, cols : int, Mat):
    if IsMoveValidOne(rows,cols,Mat):
        global CountMove
        Mat[rows - 1][cols] = (-1,CountMove)
        Mat[rows][cols] = (1,CountMove)
        CountMove+=1
        PrintField(Mat)
        if CalcAvalaibleMovesPlayerTwo(Mat) == 0:
            print("Player one wins") 
            Tk().wm_withdraw()          
            messagebox.showinfo('Domineering','Player one wins')           
        else:
            print("Available moves for player Two:", CalcAvalaibleMovesPlayerTwo(Mat))
        return True    
    else:
        pygame.display.set_caption('INVALID MOVE - try again') #stampa u zaglavlju
        print("Invalid move")
        return False

def PlayerTwoMove(rows : int, cols : int, Mat):
    if IsMoveValidTwo(rows,cols,Mat):
        global CountMove
        Mat[rows][cols] = (-2,CountMove)
        Mat[rows][cols+1] = (2,CountMove)
        CountMove+=1
        PrintField(Mat)
        if CalcAvalaibleMovesPlayerOne(Mat) == 0:
            print("Player two wins")  
            Tk().wm_withdraw()         
            messagebox.showinfo('Domineering','Player two wins')         
        else:
            print("Available moves for player One:", CalcAvalaibleMovesPlayerOne(Mat))
        return True
    else:
        pygame.display.set_caption('INVALID MOVE - try again') #stampa u zaglavlju
        pygame.display.quit
        print("Invalid move")
        return False

def PrintField(Field):
    for x in range(len(Field)):
        print(Field[x])
    print("----------------")

def show_winner(surface, player): #ispisivanje ko je pobednik
                                       
        white = (255, 255, 255)
        black = (0, 0, 0)

        # create a font object.
        # 1st parameter is the font file
        # which is present in pygame.
        # 2nd parameter is size of the font
        font = pygame.font.Font('freesansbold.ttf', 28)
        # create a text surface object,
        # on which text is drawn on it.
        text = font.render('Player ' + player + ' wins', True, black, white)
         
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
        
#primer igre

#Field = CreateMatrix(3,3)
#PrintField(Field)
#PlayerOneMove(1,0,Field)
#PlayerTwoMove(2,0,Field)
#PlayerOneMove(1,1,Field)

#status data