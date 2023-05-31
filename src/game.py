import pygame

from const import *
from entity import *
from dragger import Dragger
from config import Config
from match import *
from map import*

class Game:

    def __init__(self):
        self.pl_turn = 1
        self.hovered_sqr = None
        self.dragger = Dragger()
        # self.config = Config()
        self.mat = Match()

    # blit methods
    def show_piece(self, surface):
        for e in self.mat.enms:
            col,row = e.piece.local
            img = pygame.image.load(e.piece.img)
            img = pygame.transform.scale(img, (SQSIZE, SQSIZE))
            img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
            p_rect = img.get_rect(center = img_center)
            surface.blit(img, p_rect)
        e = self.mat.Pl
        if not self.dragger.dragging:
            col ,row = e.piece.local
            img = pygame.image.load(e.piece.img)
            img = pygame.transform.scale(img, (SQSIZE, SQSIZE))
            img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
            p_rect = img.get_rect(center = img_center)
            surface.blit(img, p_rect)
        
    def show_moves(self, surface):
        if(self.dragger.dragging):
            piece = self.mat.Pl.piece
            # loop all valid moves
            for col, row in piece.moves:
                # color
                color = (247,247,47)
                # rect
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)


    def show_hover(self, surface):
        if self.hovered_sqr:
            # color
            color = (180, 180, 180)
            # rect
            rect = (self.hovered_sqr.col * SQSIZE, self.hovered_sqr.row * SQSIZE, SQSIZE, SQSIZE)
            # blit
            pygame.draw.rect(surface, color, rect, width=3)

    # other methods

    def next_turn(self):
        self.pl_turn = 0 if self.pl_turn == 1 else 1

    def set_hover(self, row, col):
        self.hovered_sqr = self.mat.squares[row][col]

    # def play_sound(self, captured=False):
    #     if captured:
    #         self.config.capture_sound.play()
    #     else:
    #         self.config.move_sound.play()

    def reset(self):
        self.__init__()