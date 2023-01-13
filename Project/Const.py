import sys

ROWS = COLS = 8 #default values
AI_TURN = 0 #0=Human-v-Human, 1=prvi igra AI, 2=drugi igra AI

#fetch from args
length = len(sys.argv)
if length < 3:
    print("Uneli ste lose argumente! Tabla postavljena na podrazumevanu vrednost 8x8")
if length >= 3:
    if int(sys.argv[1]) > 20 or int(sys.argv[2]) > 20:
        print("Maksimalne dimenzije su 20x20!")
        print("Tabla postavljena na podrazumevanu vrednost 8x8")
    else:
        ROWS = int(sys.argv[1])
        COLS = int(sys.argv[2])
if length >= 4:
        AI_TURN = int(sys.argv[3])
        print("Human vs Computer")

if AI_TURN == 0:
    print("Human vs Human")

WIDTH = COLS * 70
HEIGHT = ROWS * 70
SQSIZE = WIDTH // COLS #square size
AI_DEPTH = 2 + AI_TURN
