import pygame
import sys

from const import *
from map import *
from match import*
from entity import *
from game import *

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption('Chess')
        self.map = Map()
        self.game = Game()
        self.level = 0


    def run(self):
        
        screen = self.screen
        dragger = self.game.dragger
        game = self.game
        mat = self.game.mat      
        lvl = self.level      
        while True:
            
            Pcol, Prow = mat.Pl.piece.local
            self.map.show_bg(screen)
            game.show_piece(screen)
            game.show_hover(screen)
            game.show_moves(screen)
            if dragger.dragging:
                dragger.update_blit(screen)
                
            for event in pygame.event.get():
                #click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE
                    # if clicked square has a piece ?
                    if (clicked_col == Pcol)&(clicked_row == Prow):
                        piece = mat.squares[clicked_row][clicked_col].piece
                        dragger.save_initial(event.pos)
                        mat.calc_move()
                        game.show_moves(screen)
                        dragger.drag_piece(piece.piece)
                        
                    # click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        released_row = dragger.mouseY // SQSIZE
                        released_col = dragger.mouseX // SQSIZE

                        # valid move ?
                        for col, row in mat.Pl.piece.moves:
                            if(col == released_col)&(row == released_row):
                                mat.Pl_move(released_col,  released_row)
                                
                                # show methods
                                game.show_piece(screen)
                                # next turn
                                mat.emns_move()
                                break
                        
                    dragger.undrag_piece()       
                
                    
                # mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    motion_row = event.pos[1] // SQSIZE
                    motion_col = event.pos[0] // SQSIZE

                    game.set_hover(motion_row, motion_col)

                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        # show methods
                        game.show_hover(screen)
                        dragger.update_blit(screen)
                        
                # key press
                elif event.type == pygame.KEYDOWN:
                    
                    # changing themes
                    if event.key == pygame.K_t:
                        mat.Pl.promotion()
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if (mat.Pl == None):
                pygame.quit()
                sys.exit()
            if((len(mat.enms)==0)):
                lvl+=1
                if(lvl):
                    data = data2
                    self.game = Game()
                    self.game.mat = Match(data)
                    game = self.game
                    mat = self.game.mat 
            pygame.display.update()


main = Main()
main.run()