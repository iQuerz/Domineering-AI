import random

def getNextMove(matrix, isMoveOK, playerOnMove):
    while True:
        row=random.randrange(0, len(matrix))
        col=random.randrange(0, len(matrix[0]))
        if isMoveOK(row, col, matrix, playerOnMove):
            return (row, col)