import pygame
import sys
from const import*
from piece import *
from map import*
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess_Platformer')
map = Map()
while True:
    map.show_bg(screen)
    img = pygame.image.load('image\piece\dark_bishop.png')
    img = pygame.transform.scale(img, (SQSIZE, SQSIZE))
    i_rect = img.get_rect(center = (4 * SQSIZE + SQSIZE // 2, 4 * SQSIZE + SQSIZE // 2))
    screen.blit(img, i_rect)                 
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
