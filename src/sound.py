import pygame
import threading
from const import*
class Sound(threading.Thread):
    def __init__(self):
        super().__init__()
        self.music_file = sound_begin
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
