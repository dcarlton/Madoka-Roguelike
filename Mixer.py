import pygame

class Mixer():
    instance = None

    def __init__(self):
        # Singleton
        pass

    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = Mixer()
            cls.instance.construct()
        return cls.instance

    def construct(self):
        pygame.mixer.init()
        self.primary = None

    def playSong(self, filename):
        if self.primary:
            self.primary.stop()
        self.primary = pygame.mixer.Sound(filename)
        self.primary.play()
