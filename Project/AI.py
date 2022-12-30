import random
import GameEngine as Engine

def getNextMove(matrix, playerOnMove):
    while True:
        row=random.randrange(0, len(matrix))
        col=random.randrange(0, len(matrix[0]))
        if Engine.isMoveValid(row, col, matrix, playerOnMove):
            return (row, col)

def getBoardEvaluation(matrix, playerOnMove):
    return 1