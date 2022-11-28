#imports
import AI
import UserInterface as UserInterface

CountMove = 0
#trenutno ima duplikati svih funkcija za svakog igraca jer mi bilo lakse tako da testiram 
def CreateMatrix(M: int, N: int):
    Matrix = [[(0,0) for x in range(M)] for y in range(N)]
    return Matrix

def IsMoveValidOne(a : int,b : int, Mat):
    if Mat[a-1][b][0] == 0 and Mat[a][b][0] == 0 and a != 0:
        return True
    else:
        return False

def IsMoveValidTwo(a : int,b : int, Mat):
    if b >= len(Mat[0])-1:
        return False
    if Mat[a][b+1][0] == 0 and Mat[a][b][0] == 0:
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

def PlayerOneMove(a : int,b : int, Mat):
    if IsMoveValidOne(a,b,Mat):
        global CountMove
        Mat[a - 1][b] = (-1,CountMove)
        Mat[a][b] = (1,CountMove)
        CountMove+=1
        PrintField(Mat)
        if CalcAvalaibleMovesPlayerTwo(Mat) == 0:
            print("Player one wins")
        else:
            print("Available moves for player Two :" , CalcAvalaibleMovesPlayerTwo(Mat))
        return True
    else:
        print("Invalide move")
        return False


def PlayerTwoMove(a : int,b : int, Mat):
    if IsMoveValidTwo(a,b,Mat):
        global CountMove
        Mat[a][b] = (-2,CountMove)
        Mat[a][b+1] = (2,CountMove)
        CountMove+=1
        PrintField(Mat)
        if CalcAvalaibleMovesPlayerOne(Mat) == 0:
            print("Player two wins")
        else:
            print("Available moves for player One :" , CalcAvalaibleMovesPlayerOne(Mat))
        return True
    else:
        print("Invalide move")
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