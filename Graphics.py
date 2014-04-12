import pygame
from Enumerations import Images

class Graphics():
    instance = None

    def __init__(self):
        # Singleton
        pass

    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = Graphics()
            cls.instance.construct()
        return cls.instance

    def construct(self):
        self.images = dict()
        self.images[Images.MAMI_STANDING] = pygame.image.load("MamiStanding.png").convert()
        self.images[Images.FAMILIAR_STANDING] = pygame.image.load("FamiliarStanding.png").convert()
        self.images[Images.WITCH_STANDING] = pygame.image.load("WitchStanding.png").convert()
        self.images[Images.WALPURGISNACHT_STANDING] = pygame.image.load("WalpurgisnachtStanding.png").convert()

    def getImage(self, image):
        return self.images[image]
