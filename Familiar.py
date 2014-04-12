import pygame
from Being import Being
from Enumerations import *
from Graphics import Graphics

class Familiar(Being):
    def __init__(self):
        self.hp = 25
        self.strength = 10
        self.image = Graphics.getInstance().getImage(Images.FAMILIAR_STANDING)
        self.rect = self.image.get_rect()
        self.beingType = BeingType.FAMILIAR
        self.block = BlockStatus.BLOCK_ALL
        self.controller = 0
