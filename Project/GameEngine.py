#imports
from UserInterface import *
import copy

CountMove = 1 #krecemo od 1 da brojimo poteze
def RaiseCounter():
    global CountMove
    CountMove += 1

def CreateMatrix(rows: int, cols: int):
    Matrix = [[(0,0) for x in range(cols)] for y in range(rows)]
    return Matrix

def getNextPlayer(playerOnMove):
    return (playerOnMove % 2) + 1


#-----------------------------------------------------VALIDATION----------------------------------------------------------

def isMoveValid(row, col, Mat, playerOnMove): #is the given move valid for active player
    if Mat[row][col] == 0:
        return False
    match playerOnMove:
        case 1:
            if row != 0 and Mat[row-1][col][0] == 0 and Mat[row][col][0] == 0:
                return True
        case 2:
            if col < COLS-1 and Mat[row][col+1][0] == 0 and Mat[row][col][0] == 0:
                return True
    return False



#------------------------------------------CALCULATE MOVES/GENERATE NEW MOVE MATRICES---------------------------------------------------------
def getAvailableMovesNumber(mat, playerOnMove): #use for checking if the active player won
    counter = 0
    for row in range(playerOnMove%2,ROWS): # ako igra 1. player, pocinje od 2. reda, jer u prvom svakako ne moze da se igra
        for col in range(COLS - (playerOnMove-1)): # ako igra 2. player, oduzima 1 kolonu jer tu svakako ne moze da se igra
            if not mat[row][col][0] == 0: continue
            if not isMoveValid(row, col, mat, playerOnMove): continue
            counter+=1
    return counter

def getAvailableMovesNumberOptimized(mat, playerOnMove):
    currentPlayerCounter = 0
    oponentPlayerCounter = 0
    for row in range(ROWS):
        for col in range(COLS):
            if isMoveValid(row, col, mat, playerOnMove):
                currentPlayerCounter+=1
            if isMoveValid(row, col, mat, getNextPlayer(playerOnMove)):
                oponentPlayerCounter+=1
    return (currentPlayerCounter, oponentPlayerCounter)

def getBoardStateOptimized(matrix, playerOnMove):
    movesLeft = getAvailableMovesNumberOptimized(matrix, playerOnMove)
    moveDiff = 1*movesLeft[0] - 0.9*movesLeft[1] #movesLeft[0] for player 1  &  movesLeft[1] for player 2

    if movesLeft[0] == 0:   return P2_WIN_VALUE
    elif movesLeft[1] == 0: return P1_WIN_VALUE
    else:                   return moveDiff

#optimizacija treba
def get_last_move(matrix):
  last_move_number = 0
  last_move_coords = (0, 0)
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if matrix[i][j][1] > last_move_number and matrix[i][j][0] > 0:
        last_move_number = matrix[i][j][1]
        last_move_coords = (i, j)
  return last_move_coords

def getAvailableMovesMatrices(mat, playerOnMove): #vraca matrice available poteza za igraca koji je na potezu
    availableMoves = []
    for row in range(playerOnMove%2,ROWS): # ako igra 1. player, pocinje od 2. reda, jer u prvom svakako ne moze da se igra
        for col in range(COLS - (playerOnMove-1)): # ako igra 2. player, oduzima 1 kolonu jer tu svakako ne moze da se igra
            if isMoveValid(row,col,mat,playerOnMove):
                availableMoves.append(getNewMoveMatrix(row, col, mat, playerOnMove)) # proverava se validity podeza unutar getNewMoveMatrix
    return availableMoves

def getNewMoveMatrix(row, col, mat, playerOnMove):
    newMat = copy.deepcopy(mat)
    placeDomino(row, col, newMat, playerOnMove)
    return newMat



#-----------------------------------------------PLACE DOMINOS----------------------------------------------------------------

def placeDomino(row, col, mat, playerOnMove): #place active player's domino on the board if the move is valid.
    if not isMoveValid(row, col, mat, playerOnMove):
        return False #invalid move
    
    mat[row - playerOnMove%2][col + (playerOnMove+1)%2] = (-playerOnMove, CountMove) # oduzimam 1 od rows ako je prvi player, dodajem 1 u cols ako je drugi player
    mat[row][col] = (playerOnMove, CountMove)
    #PrintField(mat)
    #print(getBoardState(mat,playerOnMove))
    #print(get_last_move(mat))
    return True #move succesful
      
def PrintField(Field):
    for x in range(len(Field)):
        print(Field[x])
    print("------------------------")