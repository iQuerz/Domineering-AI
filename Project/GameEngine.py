#imports
import AI
from UserInterface import *
import copy
import pymsgbox

CountMove = 1 #krecemo od 1 da brojimo poteze

playerOnMove = 1 # NE DIRAJ PROMENLJIVU, KORISTI FUNKCIJU ISPOD. 1:prvi igrac na potezu, 2:drugi igrac na potezu
def nextPlayer():
    global playerOnMove
    playerOnMove = (playerOnMove % 2) + 1

def CreateMatrix(rows: int, cols: int):
    Matrix = [[(0,0) for x in range(cols)] for y in range(rows)]
    return Matrix

def isMoveValid(row, col, Mat):
    global playerOnMove
    match playerOnMove:
        case 1:
            if row != 0 and Mat[row-1][col][0] == 0 and Mat[row][col][0] == 0:
                return True
        case 2:
            if col < COLS-1 and Mat[row][col+1][0] == 0 and Mat[row][col][0] == 0:
                return True
    return False

def getAvailableMovesMatrices(mat): #vraca matrice available poteza za igraca koji je na potezu
    global playerOnMove
    availableMoves = []
    for row in range(playerOnMove%2,ROWS): # ako igra 1. player, pocinje od 2. reda, jer u prvom svakako ne moze da se igra
        for col in range(COLS - (playerOnMove-1)): # ako igra 2. player, oduzima 1 kolonu jer tu svakako ne moze da se igra
            availableMoves.append(getNewMoveMatrix(row, col, mat, playerOnMove)) # proverava se validity podeza unutar getNewMoveMatrix
    return availableMoves

def placeDomino(row, col, mat):
    if not isMoveValid(row, col, mat):
        print("invalid move")
        return False
    
    global CountMove
    global playerOnMove
    mat[row - playerOnMove%2][col + (playerOnMove+1)%2] = (-playerOnMove, CountMove) # oduzimam 1 od rows ako je prvi player, dodajem 1 u cols ako je drugi player
    mat[row][col] = (playerOnMove, CountMove)
    PrintField(mat)
    CountMove+=1
    nextPlayer()
    print("next player:", playerOnMove)
    return True
    
def getNewMoveMatrix(row, col, mat, playerNum):
    newMat = copy.deepcopy(mat)
    placeDomino(row, col, newMat)
    return newMat

def PrintField(Field):
    for x in range(len(Field)):
        print(Field[x])
    print("----------------")