import pygame
import sys

from const import *
from map import Map
from entity import *

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
        pygame.display.set_caption('Chess')
        self.map = Map()
        self.ett = Entity()

    def run(self):
        
        screen = self.screen
        while True:
            self.map.show_bg(screen)
            self.ett.show_ett(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()


main = Main()
main.run()