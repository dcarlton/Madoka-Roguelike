import pygame
from Enumerations import Sprites
from Images import Images
from Homura import Homura
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
                if cell.barrier:
                    self.screen.blit(Images.getInstance().getImage(Sprites.KYOKO_BARRIER), pygame.Rect(cell.x * 16, cell.y * 16, 16, 16))

        if isinstance(player, Homura):
            if player.timeStopped:
                self.screen.blit(Images.getInstance().getImage(Sprites.TIME_STOP_EFFECT), pygame.Rect(0, 0, 144, 144))
                player.image.set_colorkey((255, 255, 255))
                self.drawCharacter(player)

        if player.targeting is not None:
            targetRect = pygame.Rect(player.targetX * 16, player.targetY * 16, 16, 16)
            self.screen.blit(Images.getInstance().getImage(Sprites.TARGET_CURSOR), targetRect)

        pygame.display.flip()
