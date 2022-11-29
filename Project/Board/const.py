from tkinter import *
import sys

ROWS = 8
COLS = 8

AI_TURN = 0 #0=pvp, 1=prvi igra AI, 2=drugi

length = len(sys.argv)
if length >= 3:
    ROWS = int(sys.argv[1])
    COLS = int(sys.argv[2])
    if length >= 4:
        AI_TURN = int(sys.argv[3])

WIDTH = COLS * 80
HEIGHT = ROWS * 80

SQSIZE = WIDTH // COLS