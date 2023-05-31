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
        self.ett = Entity()
        self.game = Game()

    def run(self):
        
        screen = self.screen
        dragger = self.game.dragger
        game = self.game
        mat = self.game.mat
        while True:
            self.map.show_bg(screen)
            self.ett.show_ett(screen)
            for event in pygame.event.get():
                #click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE

                    # if clicked square has a piece ?
                    if not mat.squares[clicked_row][clicked_col].is_empty():
                        piece = mat.squares[clicked_row][clicked_col].piece
                        if piece.sqr == game.Pl.sqr:
                            mat.calc_moves(piece, clicked_row, clicked_col, bool=True)
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(piece)
                            
                
                    
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
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()


main = Main()
main.run()