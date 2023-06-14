import pygame
import threading

class MusicThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.music_file = 'sound/The-Journey-Begins.mp3'

        self.playing = False

    def run(self):
        pygame.mixer.music.load(self.music_file)
        while True:
            if self.playing:
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy() and self.playing:
                    pygame.time.Clock().tick(10)
            else:
                pygame.mixer.music.stop()

    def set_music(self, music_file):
        self.music_file = music_file

    def play(self):
        self.playing = True

    def stop(self):
        self.playing = False
import pygame

pygame.init()
pygame.mixer.init()

# set up game window
WINDOW_SIZE = (400, 400)
screen = pygame.display.set_mode(WINDOW_SIZE)

# create music thread
music_thread = MusicThread()
music_thread.start()

# main game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # switch music file
                music_thread.set_music('sound/newgrounds_gts_cr.mp3')

    # update game state and draw screen
    # ...

    # display screen
    pygame.display.flip()

# stop music thread
music_thread.stop()
pygame.quit()
