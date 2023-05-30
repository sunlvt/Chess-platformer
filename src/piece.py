import os

def checkmove(col,row):
    if(col > 7)|(col < 0):
        return False
    if(row > 7)|(row < 0):
        return False
    return True  
     
class Piece:
    
    def __init__(self, name = "", color = "", local = "") :
        self.name = name
        self.color = color
        self.local = local
        self.stat = "normal"
        self.moves = []
        self.img = self.get_image()
    
    def clear_moves(self):
        self.moves = []
    
    def checkmove(col,row):
        if(col > 8)|(col < 1):
            return False
        if(row > 8)|(row < 1):
            return False
        return True
    
    def get_image(self):
        img = os.path.join(f'images/piece/{self.color}_{self.name}.png')
        return img
    
class Pawn(Piece):
    
    def __init__(self, color = "", local = "",):
        Piece.__init__(self,"pawm",color,local)
    
    def valid_move(self):
        col,row = self.local
        if(self.color == "black"):
            self.moves.append([col, row+1]) #Go up
        else:
            self.moves.append(
                [col,row-1] #Go up down
            )
class Knight(Piece):
    
    def __init__(self, color = "", local = "",):
        Piece.__init__(self,"knight",color,local)
    
    def valid_move(self):
        col,row = self.local
        col+=1
        row+=2
        if(checkmove(col,row)): #Up +2 - right +1
            self.moves.append([col,row])
        col-=2
        if(checkmove(col,row)): #Up +2 - left -1
            self.moves.append([col,row])
        row-=4
        if(checkmove(col,row)): #Down -2 - left -1
            self.moves.append([col,row])
        col+=2
        if(checkmove(col,row)): #Down -2 - right +1
            self.moves.append([col,row])
        row+=1
        col+=1
        if(checkmove(col,row)): #Down -1 - right +2
            self.moves.append([col,row])
        col-=4
        if(checkmove(col,row)): #Down -1 - left -2
            self.moves.append([col,row])
        row+=2
        if(checkmove(col,row)): #Up +1 - left -2
            self.moves.append([col,row])
        col+=4
        if(checkmove(col,row)): #Up +1 - right +2
            self.moves.append([col,row])
        
    
class Bishop(Piece):
    
    def __init__(self, color = "", local = "",):
        Piece.__init__(self,"bishop",color,local)
    
    def valid_move(self):
        col,row = self.local
        for i in range(8):
            if(i == col): continue
            self.moves.append([i,col+(i-col)]) #Up-rigt if(i>col) and Down-left if(i<col)
            self.moves.append([i,col-(i-col)]) #Up-left if(i<col) and Down-right if(i>col)
        
        
class Rook(Piece):
    
    def __init__(self, color = "", local = "",):
        Piece.__init__(self,"rook",color,local)
    
    def valid_move(self):
        col,row = self.local
        for i in range(8):
            if(i!=col):
                self.moves.append([i,row]) #go on row
            if(i!=row):
                self.moves.append([col,i]) #go on col
                
class Queen(Piece):
    
    def __init__(self, color = "", local = "",):
        Piece.__init__(self,"queen",color,local)
    
    def valid_move(self):
        col,row = self.local
        for i in range(8):
            if(i == col): continue
            self.moves.append([i,col+(i-col)]) #Up-rigt if(i>col) and Down-left if(i<col)
            self.moves.append([i,col-(i-col)]) #Up-left if(i<col) and Down-right if(i>col)
        for i in range(8):
            if(i!=col):
                self.moves.append([i,row]) #go on row
            if(i!=row):
                self.moves.append([col,i]) #go on col
        
class King(Piece):
    
    def __init__(self, color = "", local = "",):
        Piece.__init__(self,"King",color,local)
    
    def valid_move(self):
        col,row = self.local
        row+=1
        if(checkmove(col,row)): #Up
            self.moves.append([col,row]) 
        col+=1
        if(checkmove(col,row)): #Up-rigt
            self.moves.append([col,row])
        row-=1
        if(checkmove(col,row)): #Right
            self.moves.append([col,row])
        row-=1
        if(checkmove(col,row)): #Down-right
            self.moves.append([col,row]) 
        col-=1
        if(checkmove(col,row)): #Down
            self.moves.append([col,row])
        col-=1
        if(checkmove(col,row)): #Down-left
            self.moves.append([col,row])
        row+=1
        if(checkmove(col,row)): #Left
            self.moves.append([col,row])
        row+=1
        if(checkmove(col,row)): #Up-left
            self.moves.append([col,row])
    