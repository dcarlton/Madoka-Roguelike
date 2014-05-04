import pygame
from Being import Being
from Enumerations import *
from Event import Event
from Images import Images
from Map import Map

board = Map.getInstance()

class Walpurgisnacht(Being):
    def __init__(self):
        super(Walpurgisnacht, self).__init__()
        self.hp = 150
        self.strength = 25
        self.range = 1
        self.vision = 3
        self.x = 0
        self.y = 0
        self.image = Images.getInstance().getImage(Sprites.WALPURGISNACHT_STANDING)
        self.rect = self.image.get_rect()
        self.beingType = BeingType.WALPURGISNACHT
        self.block = BlockStatus.BLOCK_ALL

    def die(self):
        if self.hp <= 0:
            Event.diedEvent(BeingType.WALPURGISNACHT)
            Event.winEvent()
