import pygame
from Being import Being
from Event import Event
from Enumerations import *
from Images import Images

class Familiar(Being):
    def __init__(self):
        super(Familiar, self).__init__()
        self.maxHP = 25
        self.hp = self.maxHP

        self.image = Images.getInstance().getImage(Sprites.FAMILIAR_STANDING)
        self.rect = self.image.get_rect()

        self.beingType = BeingType.FAMILIAR
        self.block = BlockStatus.BLOCK_ALL
        self.range = 1
        self.strength = 10
        self.vision = 3

    def die(self):
        if self.hp <= 0:
            Event.diedEvent(BeingType.FAMILIAR)