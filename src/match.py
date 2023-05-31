import pygame
import sys

from const import *
from entity import*
from map import*

data_test = [[3,7],["pawn",[1,4]],["knight",[1,0]],["bishop",[2,0]]]

class Match: 
    def __init__(self,data = data_test):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
        self.build()
        self.add_PL(data[0])
        del data[0]
        self.add_enm(data)
        
    def build(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)
    
    def add_PL(self,local):
        col, row = local
        self.squares[row][col].piece = Player(local)
                
    def add_enm(self,data):
        self.enms = []
        enm = Enemy()
        for name,local in data:
            col, row = local
            enm.add_piece(name,local)
            self.enms.append(enm)
            self.squares[row][col].piece = enm
    
    def all_enm_local(self):
        list = []
        for e in self.enms:
            list.append(e.local)
        return list
        

    def calc_move(self):
        for e in self.enms:
            # e.moves = [m for m in e.valid_move() if m not in self.all_enm_local()] #remove enm team move
            #Rook
            if(type(e)=="Rook"):
                u,d,r,l = 8,-1,8,-1
                ecol, erow = e.local
                for col,row in e.moves:
                    if(type(self.squares[row][col].piece) == "Enemy"):
                        if(row == erow): 
                            if(r > col > ecol): r = col 
                            if(ecol > col > l): l = col    
                        else: 
                            if(u > row > erow): u = row
                            if(erow > row > d): d = row 
                list = []
                for col,row in e.moves:  
                    if(l < col < r): 
                        if(d < row < u):
                            list.append([col,row])
                e.moves = list
                      
            if(type(e)=="Bishop"): 
                ecol, erow = e.local
                
                for col,row in e.moves:
                    pass