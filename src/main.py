import pygame
import sys

from const import *
from map import *
from match import*
from entity import *
from game import *
from sound import*

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption('Chess-PlatFormer')
        self.map = Map()
        self.game = Game()
        self.music = Sound()

    def intro(self):
        screen = self.screen
        dragger = self.game.dragger
        game = self.game
        music = self.music
        music.set_music(sound_begin)
        music.start()
        while True:
            color = (255,204,153)
            pygame.draw.rect(screen, color, (0,720,720,50))
            fornt = pygame.font.SysFont('monospace', 18) 
            color = (102,0,51)
            local = fornt.render("MENU",1,color)
            pos = local.get_rect()
            pos.center = (720/2, 720+50/2)
            screen.blit(local,pos)
            self.map.show_bg(screen)
            game.show_piece(screen)
            self.button(1 * SQSIZE,3 * SQSIZE,1 * SQSIZE,2 * SQSIZE,"green", "START", screen)
            self.button(5 * SQSIZE,3 * SQSIZE,1 * SQSIZE,2 * SQSIZE,"red", "EXIT", screen)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    if (self.button_active(1 * SQSIZE,3 * SQSIZE,1 * SQSIZE,2 * SQSIZE)):
                        game.mat.PL_turn = 8
                        return True 
                    if (self.button_active(5 * SQSIZE,3 * SQSIZE,1 * SQSIZE,2 * SQSIZE)):
                        pygame.quit()
                        sys.exit()
                
                elif event.type == pygame.MOUSEMOTION:
                    motion_row = event.pos[1] // SQSIZE
                    motion_col = event.pos[0] // SQSIZE

                    game.set_hover(motion_row, motion_col)
                    
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

    def run(self):
        screen = self.screen
        dragger = self.game.dragger
        game = self.game
        mat = self.game.mat
        music = self.music
        music.set_music(sound[game.mat.level])
        # mat.choice_lvl(4)    
        while True:
            Pcol, Prow = mat.Pl.piece.local
            self.map.show_bg(screen)
            game.show_hover(screen)
            game.show_moves(screen)
            game.show_piece(screen)
            game.show_level(screen)
            if dragger.dragging:
                dragger.update_blit(screen)
                #enm turn
            if(mat.PL_turn < 0):
                mat.emn_move()
                pygame.time.wait(350)
                
            for event in pygame.event.get():
                #click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if(mat.PL_turn > 0):
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
                                if(len(mat.enms) == 0):
                                    mat.level_up(music)
                                
                                # show methods
                                game.show_piece(screen)
                                dragger.update_blit(screen)
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
                    if event.key == pygame.K_r:
                        mat.reset()
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            #Win
            if(mat.level == "MAX"):
                self.Win()
            
            #Over
            if (mat.Pl == None):
                self.Over()
            pygame.display.update()
            
    def Over(self):
        screen = self.screen
        dragger = self.game.dragger
        game = self.game
        music = self.music
        music.set_music(sound_over)
        while True:
            self.Note(4 * SQSIZE, 2 * SQSIZE, "YOU DIE", 70, "red", screen)
            self.button(3 * SQSIZE,3 * SQSIZE,1 * SQSIZE,2 * SQSIZE, "green", "RETRY", screen)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    if self.button_active(3 * SQSIZE,3 * SQSIZE,1 * SQSIZE,2 * SQSIZE):
                        game.mat.reset()
                        music.set_music(sound[game.mat.level])
                        return 0
                
                elif event.type == pygame.MOUSEMOTION:
                    motion_row = event.pos[1] // SQSIZE
                    motion_col = event.pos[0] // SQSIZE

                    game.set_hover(motion_row, motion_col)
                    
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

    def Win(self):
        screen = self.screen
        dragger = self.game.dragger
        game = self.game
        music = self.music
        music.set_music(sound_complete)
        while True:
            self.Note(4 * SQSIZE, 2 * SQSIZE, "YOU WIN", 70, "green", screen)
            self.button(3 * SQSIZE,3 * SQSIZE,1 * SQSIZE,2 * SQSIZE, "red", "EXIT", screen)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    if self.button_active(3 * SQSIZE,3 * SQSIZE,1 * SQSIZE,2 * SQSIZE):
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.MOUSEMOTION:
                    motion_row = event.pos[1] // SQSIZE
                    motion_col = event.pos[0] // SQSIZE

                    game.set_hover(motion_row, motion_col)
                    
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
       
    def button(self,x,y,h,w,color,content,surface):
        rect = (x, y, w, h)
        # blit
        pygame.draw.rect(surface, color, rect)
        # color = "white"
        # fornt = pygame.font.SysFont('monospace', 30, bold=True)
        # local = fornt.render(content,1,color)
        # pos = local.get_rect()
        # pos.center = (x + w//2 , y + h//2)
        # surface.blit(local,pos)
        self.Note(x+w/2,y+h/2,content,30,"white",surface)
        self.button_hover(x,y,h,w,surface)
    
    def button_hover(self,x,y,h,w,surface):
        game = self.game
        if game.hovered_sqr:
            color = "dark gray"
            col,row = game.hovered_sqr.col, game.hovered_sqr.row
            if(x/SQSIZE-1<col<(x+w)/SQSIZE)&(y/SQSIZE-1<row<(y+h)/SQSIZE):
                # rect
                rect = (x,y,w,h)
                # blit
                pygame.draw.rect(surface, color, rect, width=3)
    
    def button_active(self,x,y,h,w):
        dragger = self.game.dragger
        if(x-1 < dragger.mouseX < x+w)&(y-1 < dragger.mouseY < y+h):
            return True
        return False
    
    def Note(self, x, y, content, size, color, surface):
        fornt = pygame.font.SysFont('monospace', size, bold=True)
        local = fornt.render(content,1,color)
        pos = local.get_rect()
        pos.center = (x , y)
        surface.blit(local,pos)

       
        
#RUN
main = Main()
if (main.intro()):
    main.run()