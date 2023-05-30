import pygame
import math
from const import *
# from square import Square
from piece import *
from dragger import *
# from move import Move
# from sound import Sound
import copy
import os

data_test = [[3,7],["pawn",[1,4]],["knight",[1,0]],["bishop",[2,0]]]

class Player:
    
    def __init__(self,local):
        self.piece = Pawn("white",local)
    
    def check_move(self):
        pass 
    
class Enemy:
    
    def __init__(self, data = []):
        self.enms = []
        self.setup(data)
        self.lc_list = self.all_local() 
        
    def all_local(self):
        list = []
        for e in self.enms:
            list.append(e.local)
        self.lc_list = list
        return list
        
    def check_move(self):
        for e in self.enms:
            e.moves = [m for m in e.valid_move() if m not in self.lc_list]
    
    def add_piece(self,name,local):
        if (name == "pawn"):
            self.enms.append(Pawn("black",local)) 
        if (name == "rook"):
            self.enms.append(Rook("black",local))
        if (name == "knight"):
            self.enms.append(Knight("black",local))
        if (name == "bishop"):
            self.enms.append(Bishop("black",local))
        if (name == "queen"):
            self.enms.append(Queen("black",local))
        if (name == "king"):
            self.enms.append(King("black",local))
    
    def setup(self,data):
        for name,local in data:
            self.add_piece(name,local)
        self.all_local()
        self.check_move()
        
class Entity:
    
    def __init__(self,data = data_test):
        self.Pl = Player(data[0])
        self.enm = Enemy()
        del data[0]
        self.enm.setup(data)

    def show_ett(self, surface):
        for e in self.enm.enms:
            piece = e
            col, row = e.local
            img = pygame.image.load(piece.img)
            img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
            rect = img.get_rect(center=img_center)
            surface.blit(img, rect)
    
    def Enm_move(self):
        Pcol, Prow = self.Pl.piece.local #get player local
        for e in self.enm.enms:
            if(len(e.moves) != 0): #have valid move ?
                bcol, brow = e.moves[0] #best move
                for col,row in e.moves:
                    if(math.sqrt((col-Pcol)**2+(row-Prow)**2) < math.sqrt((bcol-Pcol)**2+(brow-Prow)**2)):
                        bcol, brow = col, row
                self.enm.all_local()
                self.enm.check_move()
                
        
            
