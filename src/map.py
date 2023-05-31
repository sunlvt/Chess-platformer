import pygame
import sys

from const import *
# from game import Game
# from square import Square

WIDTH = 600
HEIGHT = 600

class Map:
    def __init__(self):
        pass
    
    def show_bg(self,surface):
        for row in range(ROWS):
            for col in range(COLS):
                # color
                color = (229, 204, 255) if (row + col) % 2 == 0 else (166, 100, 100)
                # rect
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)

class Square:
    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece
        
    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def is_empty(self):
        return self.piece == None


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess_Platformer')
map = Map()
while True:
    map.show_bg(screen)
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

