import random

def getNextMove(matrix, isMoveValid):
    while True:
        i=random.randrange(0, len(matrix))
        j=random.randrange(0, len(matrix[0]))
        if(isMoveValid(i, j, matrix)):
            return (i, j)