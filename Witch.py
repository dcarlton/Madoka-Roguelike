from Familiar import Familiar
from Enumerations import *
from Graphics import Graphics
from TurnManager import TurnManager

class Witch(Familiar):
    def __init__(self):
        self.maxHP = 75
        self.hp = self.maxHP
        self.strength = 20
        self.x = 0
        self.y = 0
        self.image = Graphics.getInstance().getImage(Images.WITCH_STANDING)
        self.rect = self.image.get_rect()
        self.beingType = BeingType.WITCH
        self.block = BlockStatus.BLOCK_ALL
