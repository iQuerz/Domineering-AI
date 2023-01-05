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
def getNextMoveMinMax(matrix, depth, playerOnMove):
    best_move = None
    best_val = -float("inf")
    available_moves = Engine.getAvailableMovesMatrices(matrix, playerOnMove)
    for move in available_moves:
        val = min_maxWithAlphaBeta(move, depth, -float("inf"), float("inf"), Engine.getNextPlayer(playerOnMove))
        if val > best_val:
                best_val = val
                best_move = move           
    return Engine.get_last_move(best_move)

def min_maxWithAlphaBeta(matrix, depth, alpha, beta, playerOnMove):
  if Engine.getAvailableMovesNumber(matrix, playerOnMove) == 0 or depth == 0:
    return Engine.getBoardState(matrix, playerOnMove)

  if playerOnMove == 1:
    max_val = -float("inf")
    available_moves = Engine.getAvailableMovesMatrices(matrix, playerOnMove)
    for move in available_moves:
      val = min_maxWithAlphaBeta(move, depth - 1, alpha, beta, Engine.getNextPlayer(playerOnMove))
      max_val = max(max_val, val)
      alpha = max(alpha, val)
      if beta <= alpha:
        break
    return max_val
  else:
    min_val = float("inf")
    available_moves = Engine.getAvailableMovesMatrices(matrix, playerOnMove)
    for move in available_moves:
      val = min_maxWithAlphaBeta(move, depth - 1, alpha, beta, Engine.getNextPlayer(playerOnMove))
      min_val = min(min_val, val)
      beta = min(beta, val)
      if beta <= alpha:
        break
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