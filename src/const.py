# Screen dimensions
WIDTH = 720
HEIGHT = 770

# Board dimensions
ROWS = 8
COLS = 8
SQSIZE = WIDTH // COLS
data_test = [[3,7],
             ["pawn",[1,4]],
             ["knight",[1,0]],
             ["bishop",[5,0]]]


data1 = [[3,7],["pawn",[0,2]],["pawn",[2,2]],["pawn",[4,2]],["pawn",[6,2]],
         ["rook",[7,0]],["knight",[1,0]],["knight",[6,0]],["rook",[0,0]]]
data2 = [[3,7],["pawn",[0,3]],["bishop",[0,1]],["pawn",[1,2]],["bishop",[4,1]],
         ["pawn",[4,2]],["pawn",[6,1]],["rook",[4,0]],["knight",[2,1]],["knight",[6,2]],["rook",[3,0]]]
data3 = [[3,7],["bishop",[1,1]],["pawn",[2,2]], ["bishop",[3,1]],["pawn",[6,2]],
         ["rook",[5,0]],["knight",[1,2]],["knight",[5,2]],["rook",[2,1]],["rook",[7,1]],["queen",[3,0]]]
data4 = [[3,7], ["bishop",[0,2]],["knight",[2,2]], ["knight",[4,2]],["bishop",[6,2]],
         ["rook",[7,0]],["queen",[3,0]],["queen",[4,0]],["rook",[0,0]]]
level = [data1,data2,data3,data4]

Note = ["Turtorial", "level 1", "level 2", "level 3", "level 4"]
sound_begin = "sound/The-Journey-Begins.mp3"
sound_over = "sound/Game-Over.mp3"
sound_complete = "sound/Level_Complete.mp3"
sound = [
    "sound/Eclipse.mp3",
    "sound/Pisco-Disco.mp3",
    "sound/Happy-Plum-Tiny-Escape-OST.mp3",
    "sound/4western_adventures.mp3",
    "sound/newgrounds_gts_cr.mp3",
]