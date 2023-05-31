import pygame

from const import *

class Dragger:

    def __init__(self):
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0
        
    # blit method
    
    def update_blit(self, surface):
        # img
        img = pygame.image.load(self.piece.img)
        # rect
        # img_center = (self.mouseX, self.mouseY)S
        p_rect = img.get_rect(center=(self.mouseX, self.mouseY))
        # blit
        surface.blit(img, p_rect)

    # other methods

    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos # (xcor, ycor)

    def save_initial(self, pos):
        self.initial_row = pos[1] // SQSIZE
        self.initial_col = pos[0] // SQSIZE

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False