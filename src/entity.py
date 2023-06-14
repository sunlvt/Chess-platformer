from const import *
from piece import *
from dragger import *

class Player:
    Pmt = ["pawn","queen","rook","bishop","knight"]
    def __init__(self,local):
        self.piece = Pawn("white",local)
    
    def promotion(self):
        col,row = self.piece.local
        name = self.Pmt.index(self.piece.name)
        if(name == len(self.Pmt)-1): name = -1
        name = self.Pmt[name+1]
        if(name == "rook"):
            self.piece = Rook("white",[col,row])
        if(name == "bishop"):
            self.piece = Bishop("white",[col,row])
        if(name == "knight"):
            self.piece = Knight("white",[col,row])
        if(name == "queen"):
            self.piece = Queen("white",[col,row])
    
class Enemy:
    
    def __init__(self, data = []):
        self.piece = None
        
    def all_local(self):
        list = []
        for e in self.enms:
            list.append(e.local)
        self.lc_list = list
        return list
        
    def check_move(self):
        for e in self.enms:
            e.moves = [m for m in e.valid_move() if m not in self.lc_list] #remove team move
    
    def add_piece(self,name,local):
        if (name == "pawn"):
            self.piece = (Pawn("dark",local)) 
        if (name == "rook"):
            self.piece = (Rook("dark",local))
        if (name == "knight"):
            self.piece = (Knight("dark",local))
        if (name == "bishop"):
            self.piece = (Bishop("dark",local))
        if (name == "queen"):
            self.piece = (Queen("dark",local))
        if (name == "king"):
            self.piece = (King("dark",local))
    
        
# class Entity:
    
#     def __init__(self,data = data_test):
#         self.Pl = Player(data[0])
#         self.enm = Enemy()
#         del data[0]
#         self.enm.setup(data)

#     def show_ett(self, surface):
#         for e in self.enm.enms:
#             piece = e
#             col, row = e.local
#             img = pygame.image.load(piece.img)
#             img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2
#             rect = img.get_rect(center=img_center)
#             surface.blit(img, rect)
    
#     def Enm_move(self):
#         Pcol, Prow = self.Pl.piece.local #get player local
#         for e in self.enm.enms:
#             if(len(e.moves) != 0): #have valid move ?
#                 bcol, brow = e.moves[0] #best move
#                 for col,row in e.moves:
#                     if(math.sqrt((col-Pcol)**2+(row-Prow)**2) < math.sqrt((bcol-Pcol)**2+(brow-Prow)**2)):
#                         bcol, brow = col, row
#                 e.local = [bcol, brow]
#                 e.clear_moves()
#                 self.enm.all_local()
#                 self.enm.check_move()
                
        
            
