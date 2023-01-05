import random
import GameEngine as Engine

def getNextMove(matrix, playerOnMove):
    while True:
        row=random.randrange(0, len(matrix))
        col=random.randrange(0, len(matrix[0]))
        if Engine.isMoveValid(row, col, matrix, playerOnMove):
            return (row, col)
    
def getNextMoveMinMax(matrix, depth, playerOnMove):
    bestMoveMatrix = None
    bestMoveValue = -float("inf")
    availableMovesMatrices = Engine.getAvailableMovesMatrices(matrix, playerOnMove)
    for moveMatrix in availableMovesMatrices:
        val = min_maxWithAlphaBeta(moveMatrix, depth, -float("inf"), float("inf"), Engine.getNextPlayer(playerOnMove))
        if val > bestMoveValue:
            bestMoveValue = val
            bestMoveMatrix = moveMatrix
    return Engine.get_last_move(bestMoveMatrix)

transposition_table = {}
def min_maxWithAlphaBeta(matrix, depth, alpha, beta, playerOnMove):
    # Check if the position is in the transposition table
    key = str(matrix)
    if key in transposition_table:
        return transposition_table[key]

    if depth==0 or Engine.getAvailableMovesNumber(matrix, playerOnMove) == 0:
        return Engine.getBoardState(matrix, playerOnMove)

    if playerOnMove == 1:
        max_val = -float("inf")
        availableMovesMatrices = Engine.getAvailableMovesMatrices(matrix, playerOnMove)
        for moveMatrix in availableMovesMatrices:
            val = min_maxWithAlphaBeta(moveMatrix, depth - 1, alpha, beta, Engine.getNextPlayer(playerOnMove))
            max_val = max(max_val, val)
            alpha = max(alpha, val)
            if beta <= alpha:
                break
        transposition_table[key] = max_val
        return max_val

    else:
        min_val = float("inf")
        availableMovesMatrices = Engine.getAvailableMovesMatrices(matrix, playerOnMove)
        for moveMatrix in availableMovesMatrices:
            val = min_maxWithAlphaBeta(moveMatrix, depth - 1, alpha, beta, Engine.getNextPlayer(playerOnMove))
            min_val = min(min_val, val)
            beta = min(beta, val)
            if beta <= alpha:
                break
        transposition_table[key] = min_val
        return min_val

def min_max(matrix, depth, playerOnMove):
  if Engine.getAvailableMovesNumber(matrix, playerOnMove) == 0 or depth == 0:
    return Engine.getBoardState(matrix, playerOnMove)
  
  if playerOnMove == 1:
    max_val = -float("inf")
    available_moves = Engine.getAvailableMovesMatrices(matrix, playerOnMove)
    for move in available_moves:
      val = min_max(move, depth - 1, Engine.getNextPlayer(playerOnMove))
      max_val = max(max_val, val)
    return max_val
  else:
    min_val = float("inf")
    available_moves = Engine.getAvailableMovesMatrices(matrix, playerOnMove)
    for move in available_moves:
      val = min_max(move, depth - 1, Engine.getNextPlayer(playerOnMove))
      min_val = min(min_val, val)
    return min_val