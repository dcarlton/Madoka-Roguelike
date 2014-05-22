from Being import Being
from Event import Event
from Enumerations import *
from Images import Images

class Witch(Being):
    def __init__(self):
        super(Witch, self).__init__()
        self.maxHP = 75
        self.hp = self.maxHP

        self.image = Images.getInstance().getImage(Sprites.WITCH_STANDING)
        self.rect = self.image.get_rect()

        self.beingType = BeingType.WITCH
        self.block = BlockStatus.BLOCK_ALL
        self.range = 1
        self.strength = 20
        self.vision = 3

    def die(self):
        if self.hp <= 0:
            Event.diedEvent(BeingType.WITCH)