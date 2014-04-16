import pygame
from Enumerations import Images
from Map import Map

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
        self.screen = pygame.display.get_surface()

        self.images = dict()
        self.images[Images.HOMURA_STANDING] = pygame.image.load("HomuraStanding.png").convert()
        self.images[Images.MAMI_STANDING] = pygame.image.load("MamiStanding.png").convert()
        self.images[Images.FAMILIAR_STANDING] = pygame.image.load("FamiliarStanding.png").convert()
        self.images[Images.WITCH_STANDING] = pygame.image.load("WitchStanding.png").convert()
        self.images[Images.WALPURGISNACHT_STANDING] = pygame.image.load("WalpurgisnachtStanding.png").convert()
        self.images[Images.TARGET_CURSOR] = pygame.image.load("TargetCursor.png").convert()
        self.images[Images.TARGET_CURSOR].set_colorkey((255, 255, 255))

    def drawCharacter(self, character):
        character.rect.x = character.x * 16
        character.rect.y = character.y * 16
        self.screen.blit(character.image, character.rect)

    def drawPlayState(self, player):
        self.screen.fill((255, 255, 255))

        for column in Map.getInstance().grid:
            for cell in column:
                if len(cell.beings) != 0:
                    self.drawCharacter(cell.beings[-1])

        if player.targeting is not None:
            targetRect = pygame.Rect(player.targetX * 16, player.targetY * 16, 16, 16)
            self.screen.blit(self.images[Images.TARGET_CURSOR], targetRect)

        pygame.display.flip()

    def getImage(self, image):
        return self.images[image]
