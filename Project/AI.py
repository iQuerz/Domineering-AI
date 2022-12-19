import random

def getNextMove(matrix, isMoveOK):
    while True:
        i=random.randrange(0, len(matrix))
        j=random.randrange(0, len(matrix[0]))
        if(isMoveOK(i, j, matrix)):
            return (i, j)