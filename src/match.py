from const import *
from entity import*
from map import*
from sound import*
import math



class Match: 
    def __init__(self,data = data_test):
        self.data = data
        self.build()
        self.add_PL(self.data[0])
        self.add_enm(self.data)
        self.calc_move()
        self.level = 0
        self.PL_turn = 0
        
    def build(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)
    
    def add_PL(self,local):
        col, row = local
        self.Pl = Player(local)
        self.squares[row][col].piece = self.Pl
                
    def add_enm(self,data):
        self.enms = []
        for i in range(1,len(data)):
            name,local = data[i]
            enm = Enemy()
            col, row = local
            enm.add_piece(name,local)
            self.enms.append(enm)
            self.squares[row][col].piece = enm
    
    def all_enm_local(self):
        list = []
        for e in self.enms:
            list.append(e.piece.local)
        return list

    def calc_move(self):
        
        #strang move
        def strang_move(piece = None):
            list = []
            pcol, prow = piece.piece.local
            for i in range(prow+1,ROWS): #go up
                if(self.squares[i][pcol].is_empty()): 
                    list.append([pcol,i])
                elif type(self.squares[i][pcol]) != type(piece): #is team?
                    list.append([pcol,i])
                    break
                else: break
            for i in range(prow-1,-1,-1): #go down
                if(self.squares[i][pcol].is_empty()):
                    list.append([pcol,i])
                elif type(self.squares[i][pcol]) != type(piece): #is team?
                    list.append([pcol,i])
                    break
                else: break
            for i in range(pcol+1,COLS): #go right
                if(self.squares[prow][i].is_empty()):
                    list.append([i,prow])
                elif type(self.squares[prow][i]) != type(piece): #is team?
                    list.append([i,prow])
                    break
                else: break
            for i in range(pcol-1,-1,-1): #go left
                if(self.squares[prow][i].is_empty()):
                    list.append([i,prow])
                elif type(self.squares[prow][i]) != type(piece): #is team?
                    list.append([i,prow])
                    break
                else: break
            if(piece.piece.color == "dark"): #is piece is enemy?
                list = [m for m in list if m not in self.all_enm_local()] #remove enm team move
            return list
        
        #diagonal move
        def diagonal_move(piece = None):
            list = []
            pcol, prow = piece.piece.local
            u, d = True, True # up, down is empty?
            for i in range(pcol+1,COLS): #go right
                
                if(u):
                    if(prow + (i-pcol) < 8):
                        if(self.squares[prow + (i-pcol)][i].is_empty()): #check up
                            list.append([i,prow + (i-pcol)])
                        elif type(self.squares[prow + (i-pcol)][i]) != type(piece): #is team?
                            list.append([i,prow + (i-pcol)])
                            u = False
                        else: u = False
                if(d):
                    if(prow - (i-pcol) > -1):
                        if(self.squares[prow - (i-pcol)][i].is_empty()): #check down
                            list.append([i,prow - (i-pcol)])
                        elif type(self.squares[prow - (i-pcol)][i]) != type(piece): #is team?
                            list.append([i,prow - (i-pcol)])
                            d = False
                        else: d = False
                if(u == False)&(d == False): break
            u, d = True, True # up, down is empty?
            for i in range(pcol-1,-1,-1): #go left
                if(d):
                    if(prow - (pcol - i) > -1):
                        if(self.squares[prow - (pcol - i)][i].is_empty()): #check down
                            list.append([i,prow - (pcol - i)])
                        elif type(self.squares[prow - (pcol - i)][i]) != type(piece): #is team?
                            list.append([i,prow - (pcol - i)])
                            d = False
                        else: d = False
                if(u):
                    if(prow + (pcol - i) < 8):
                        if(self.squares[prow + (pcol - i)][i].is_empty()): #check up
                            list.append([i,prow + (pcol - i)])
                        elif type(self.squares[prow + (pcol - i)][i]) != type(piece): #is team?
                            list.append([i,prow + (pcol - i)])
                            u = False
                        else: u = False
                if(u == False)&(d == False): break
            if(piece.piece.color == "dark"): #is piece is enemy?
                list = [m for m in list if m not in self.all_enm_local()] #remove enm team move
            return list
        
        #knight move
        def knight_move(piece = None):
            pcol, prow = piece.piece.local
            list = [
                     [pcol+1,prow+2], #up2-right1
                     [pcol-1,prow+2], #up2-left1
                     [pcol-1,prow-2], #down2-left1
                     [pcol+1,prow-2], #down2-right1
                     [pcol-2,prow+1], #up1-left2
                     [pcol-2,prow-1], #down1-left2
                     [pcol+2,prow+1], #up1-right2
                     [pcol+2,prow-1] #down1-right2
                     ]
            if(piece.piece.color == "dark"): #is piece is enemy?
                list = [m for m in list if m not in self.all_enm_local()] #remove enm team move
            for i in range(len(list)): #out map
                if i > len(list)-1:
                    break
                col, row = list[i]
                while(col > 7)|(col < 0)|(row > 7)|(row < 0):
                    if i > len(list)-1:
                        break
                    col, row = list[i]
                    if(col > 7)|(col < 0):
                        del list[i]
                        continue
                    if(row > 7)|(row < 0):
                        del list[i]
                        continue
            return list
        
        #king move
        def king_move(piece = None):
            pcol, prow = piece.piece.local
            list = [
                     [pcol,prow+1], #up
                     [pcol+1,prow+1], #up-right
                     [pcol+1,prow], #right
                     [pcol+1,prow-1], #down-right
                     [pcol,prow-1], #down
                     [pcol-1,prow-1], #down-left
                     [pcol-1,prow], #left
                     [pcol-1,prow+1] #up-left
                     ]
            if(piece.piece.color == "dark"): #is piece is enemy?
                list = [m for m in list if m not in self.all_enm_local()] #remove enm team move
            for i in range(len(list)): #out map
                if i > len(list)-1:
                    break
                col, row = list[i]
                while(col > 7)|(col < 0)|(row > 7)|(row < 0):
                    if i > len(list)-1:
                        break
                    col, row = list[i]
                    if(col > 7)|(col < 0):
                        del list[i]
                        continue
                    if(row > 7)|(row < 0):
                        del list[i]
                        continue
            return list
        
        #enemy move            
        for e in self.enms:
            #Rook
            if(e.piece.name == "rook"):
                e.piece.moves = strang_move(e)
                
            #Bishop          
            if(e.piece.name == "bishop"):
                e.piece.moves = diagonal_move(e)
            
            #Queen
            if(e.piece.name == "queen"):
                e.piece.moves = diagonal_move(e)+strang_move(e)
            
            #Knight
            if(e.piece.name == "knight"):
                e.piece.moves = knight_move(e)
                
            #King
            if(e.piece.name == "king"):
                e.piece.moves = king_move(e)
            
            #Pawn
            if(e.piece.name == "pawn"):
                e.piece.moves = king_move(e)
                # col, row = e.piece.local
                # if(self.squares[col][row+1].is_empty()):
                #     e.piece.moves = [[col,row+1]]
                # elif( type(self.squares[col][row+1]) != type(piece)):
                #     e.piece.moves = [[col,row+1]]     
    
        #player move
        e = self.Pl
        if e!= None:
            #Rook
            if(e.piece.name == "rook"):
                e.piece.moves = strang_move(e)
                
            #Bishop          
            if(e.piece.name == "bishop"):
                e.piece.moves = diagonal_move(e)
            
            #Queen
            if(e.piece.name == "queen"):
                e.piece.moves = diagonal_move(e)+strang_move(e)
            
            #Knight
            if(e.piece.name == "knight"):
                e.piece.moves = knight_move(e)
                
            #King
            if(e.piece.name == "king"):
                e.piece.moves = king_move(e)
            
            #Pawn
            if(e.piece.name == "pawn"):
                e.piece.moves = king_move(e)                                                        
        
    def emns_move(self):
        Pcol, Prow = self.Pl.piece.local #Player local
        if (self.Pl == None): return 0
        for e in self.enms:
            if (self.Pl == None): break
            if(len(e.piece.moves)!=0):
                bcol, brow = e.piece.moves[0] #best move
                for col,row in e.piece.moves:
                    if(math.sqrt((col-Pcol)**2+(row-Prow)**2) < math.sqrt((bcol-Pcol)**2+(brow-Prow)**2)):
                        bcol, brow = col, row
                e.piece.local = [bcol, brow]
                self.enm_capture(bcol,brow)
                e.piece.clear_moves()
                self.reload()
                self.calc_move()      
                
    def emn_move(self):
        Pcol, Prow = self.Pl.piece.local #Player local
        if (self.Pl == None): return 0
        e = self.enms[len(self.enms)+self.PL_turn]
        self.PL_turn+=1
        if(self.PL_turn==0): self.PL_turn = 8
        if(len(e.piece.moves)!=0):
            bcol, brow = e.piece.moves[0] #best move
            for col,row in e.piece.moves:
                if(math.sqrt((col-Pcol)**2+(row-Prow)**2) < math.sqrt((bcol-Pcol)**2+(brow-Prow)**2)):
                    bcol, brow = col, row
            e.piece.local = [bcol, brow]
            self.enm_capture(bcol,brow)
            e.piece.clear_moves()
            self.reload()
            self.calc_move()      

    def enm_capture(self, col, row):
        pcol, prow = self.Pl.piece.local
        if(col == pcol)&(row == prow):
            self.Pl = None
    
    def Pl_move(self,col,row):
        self.Pl.piece.local = [col,row]
        self.Pl_capture(col,row)
        self.reload()
        self.calc_move()
        # self.emns_move()
        self.PL_turn-=1
        if(self.PL_turn==0):
            self.PL_turn-=len(self.enms)
    
    def Pl_capture(self, col, row):
        if not self.squares[row][col].is_empty():
            for i in range(len(self.enms)):
                ecol, erow = self.enms[i].piece.local
                if(ecol == col)&(erow == row):
                    del self.enms[i]
                    break
        # if(len(self.enms) == 0):
        #     self.level_up()
        
    def level_up(self, music):
        self.level+=1
        if self.level > len(level)-1:
            self.level = "MAX"
            return 0
        music.set_music(sound[self.level])
        self.PL_turn = 8
        self.data = level[self.level]
        self.calc_move()
        self.build()
        self.add_PL(self.data[0])
        self.add_enm(self.data)
        
    def reset(self):
        self.build()
        self.PL_turn = 8
        self.add_PL(self.data[0])
        self.add_enm(self.data)
        self.calc_move()
        
    def reload(self):
        self.build()
        for e in self.enms:
            if e != None:
                col, row = e.piece.local
                self.squares[row][col].piece = e
        p = self.Pl
        if p != None:
            col, row = p.piece.local
            self.squares[row][col].piece = p
    
    def choice_lvl(self, num):
        self.level = num
        self.PL_turn = 8
        self.data = level[self.level-1]
        self.build()
        self.add_PL(self.data[0])
        self.add_enm(self.data)
        