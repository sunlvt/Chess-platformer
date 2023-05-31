import pygame

from const import *
from entity import *
from dragger import Dragger
from config import Config
from match import *
from map import*

#font

def show_local(col,row,surface):
    color = (180, 180, 180)
    fornt = pygame.font.SysFont('monospace', 18, bold=True) 
    local = fornt.render(str(col)+","+str(row),1,color)
    pos = (col * SQSIZE+5, 5 + row * SQSIZE)
    surface.blit(local,pos)

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
            show_local(col,row,surface)
        e = self.mat.Pl
        if not self.dragger.dragging:
            col ,row = e.piece.local
            img = pygame.image.load(e.piece.img)
            img = pygame.transform.scale(img, (SQSIZE, SQSIZE))
            img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
            p_rect = img.get_rect(center = img_center)
            surface.blit(img, p_rect)
            show_local(col,row,surface)
        
        
        
    def show_moves(self, surface):
        if(self.dragger.dragging):
            piece = self.mat.Pl.piece
            # loop all valid moves
            for col, row in piece.moves:
                # color
                color = (246,255,167)
                # rect
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect)
                color = (180, 180, 180)
                # rect
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                # blit
                pygame.draw.rect(surface, color, rect, width=1)


    def show_hover(self, surface):
        if self.hovered_sqr:
            col,row = self.hovered_sqr.col,self.hovered_sqr.row
            # color
            color = (180, 180, 180)
            # rect
            rect = (self.hovered_sqr.col * SQSIZE, self.hovered_sqr.row * SQSIZE, SQSIZE, SQSIZE)
            # blit
            pygame.draw.rect(surface, color, rect, width=3)
            
            show_local(col,row,surface)
            
            color = (0, 0, 0)
            pygame.draw.rect(surface, color, (600,0,100,600))
            
            if(self.dragger.dragging):
                color = (52, 56, 218)
            else: 
                color = (0, 0, 0)
            fornt = pygame.font.SysFont('monospace', 18, bold=True)
            local = fornt.render("dragging",1,color)
            pos = (8 * SQSIZE+5, 5 + 1 * SQSIZE)
            surface.blit(local,pos)
            
            
            color = (255,57,43)
            fornt = pygame.font.SysFont('monospace', 12)
            local = fornt.render(str(type(self.hovered_sqr.piece)),1,color)
            pos = (8 * SQSIZE+5, 5 + 2 * SQSIZE)
            surface.blit(local,pos)
            
            col,row = self.mat.Pl.piece.local
            if(col == self.hovered_sqr.col)&(row == self.hovered_sqr.row):
                color = (49, 240, 88)
            else: color = (0, 0, 0)
            fornt = pygame.font.SysFont('monospace', 18, bold=True)
            local = fornt.render("correct",1,color)
            pos = (8 * SQSIZE+5, 5 + 0 * SQSIZE)
            surface.blit(local,pos)
            
# other methods

    def next_turn(self):
        self.pl_turn = 0 if self.pl_turn == 1 else 1

    def set_hover(self, row, col):
        if col > 7: col = 7
        self.hovered_sqr = self.mat.squares[row][col]

    # def play_sound(self, captured=False):
    #     if captured:
    #         self.config.capture_sound.play()
    #     else:
    #         self.config.move_sound.play()

    def reset(self):
        self.__init__()