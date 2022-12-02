#imports
import AI
from UserInterface import *
import pymsgbox

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
            pymsgbox.alert('Player 1!', 'The winner is:', button='OK') #alert(text='', title='', button='OK')         
        else:
            print("Available moves for player Two:", CalcAvalaibleMovesPlayerTwo(Mat))
        return True    
    else:
        pymsgbox.alert('Try again!', 'Invalid move')
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
            pymsgbox.alert('Player 2!', 'The winner is:', button='OK')
        else:
            print("Available moves for player One:", CalcAvalaibleMovesPlayerOne(Mat))
        return True
    else:
        pymsgbox.alert('Try again!', 'Invalid move')
        print("Invalid move")
    return False
    
def PrintField(Field):
    for x in range(len(Field)):
        print(Field[x])
    print("----------------")
       
#primer igre

#Field = CreateMatrix(3,3)
#PrintField(Field)
#PlayerOneMove(1,0,Field)
#PlayerTwoMove(2,0,Field)
#PlayerOneMove(1,1,Field)

#status data