import pygame
from Being import Being
from Enumerations import *
from Event import Event
from Images import Images

class Walpurgisnacht(Being):
    def __init__(self):
        super(Walpurgisnacht, self).__init__()
        self.maxHP = 150
        self.hp = self.maxHP

        self.image = Images.getInstance().getImage(Sprites.WALPURGISNACHT_STANDING)
        self.rect = self.image.get_rect()

        self.beingType = BeingType.WALPURGISNACHT
        self.block = BlockStatus.BLOCK_ALL
        self.range = 1
        self.strength = 25
        self.vision = 3

    def die(self):
        if self.hp <= 0:
            Event.diedEvent(BeingType.WALPURGISNACHT)
            Event.winEvent()
