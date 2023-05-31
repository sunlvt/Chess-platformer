import pygame
import sys
# Screen dimensions
WIDTH = 700
HEIGHT = 600

# Board dimensions
ROWS = 8
COLS = 8
SQSIZE = (WIDTH-100) // COLS
# data_test = [[3,7],
#              ["pawn",[1,4]],
#              ["knight",[1,0]],
#              ["bishop",[2,0]]]


data_test = [[3,7],["pawn",[0,2]],["pawn",[2,2]],["pawn",[4,2]],["pawn",[6,2]],["rook",[7,0]],["knight",[1,0]],["knight",[6,0]],["rook",[0,0]]]
data2 = [[3,7],["pawn",[0,3]],["bishop",[0,1]],["pawn",[1,2]],["bishop",[4,1]],["pawn",[4,2]],["pawn",[6,1]],["rook",[4,0]],["knight",[2,1]],["knight",[6,2]],["rook",[3,0]]]
data3 = [[3,7],["bishop",[1,1]],["pawn",[2,2]], ["bishop",[3,1]],["pawn",[6,2]],["rook",[5,0]],["knight",[1,2]],["knight",[5,2]],["rook",[2,1]],["rook",[7,1]],["queen",[3,0]]]
data4 = [[3,7], ["bishop",[0,2]],["knight",[2,2]], ["knight",[4,2]],["bishop",[6,2]],["rook",[7,0]],["queen",[3,0]],["queen",[4,0]],["rook",[0,0]]]
# level = [data1,data2,data3,data4]