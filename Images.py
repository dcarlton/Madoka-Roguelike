import pygame
from Enumerations import Sprites

class Images():
    instance = None

    def __init__(self):
        # Singleton
        pass

    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = Images()
            cls.instance.construct()
        return cls.instance

    def construct(self):
        self.images = dict()
        self.images[Sprites.HOMURA_STANDING] = pygame.image.load("HomuraStanding.png").convert()
        self.images[Sprites.MAMI_STANDING] = pygame.image.load("MamiStanding.png").convert()
        self.images[Sprites.FAMILIAR_STANDING] = pygame.image.load("FamiliarStanding.png").convert()
        self.images[Sprites.WITCH_STANDING] = pygame.image.load("WitchStanding.png").convert()
        self.images[Sprites.WALPURGISNACHT_STANDING] = pygame.image.load("WalpurgisnachtStanding.png").convert()
        self.images[Sprites.TIME_STOP_EFFECT] = pygame.image.load("TimeStopEffect.png").convert()
        self.images[Sprites.TIME_STOP_EFFECT].set_alpha(200)
        self.images[Sprites.TARGET_CURSOR] = pygame.image.load("TargetCursor.png").convert()
        self.images[Sprites.TARGET_CURSOR].set_colorkey((255, 255, 255))

    def getImage(self, image):
        return self.images[image]
