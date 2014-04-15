import pygame
from Being import Being
from Enumerations import *
from Graphics import Graphics

class Familiar(Being):
    def __init__(self):
        super(Familiar, self).__init__()
        self.maxHP = 25
        self.hp = self.maxHP
        self.x = 0
        self.y = 0
        self.strength = 10
        self.image = Graphics.getInstance().getImage(Images.FAMILIAR_STANDING)
        self.rect = self.image.get_rect()
        self.beingType = BeingType.FAMILIAR
        self.block = BlockStatus.BLOCK_ALL
