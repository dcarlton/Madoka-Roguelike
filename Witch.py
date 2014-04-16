from Being import Being
from Enumerations import *
from Images import Images

class Witch(Being):
    def __init__(self):
        super(Witch, self).__init__()
        self.maxHP = 75
        self.hp = self.maxHP
        self.strength = 20
        self.x = 0
        self.y = 0
        self.image = Images.getInstance().getImage(Sprites.WITCH_STANDING)
        self.rect = self.image.get_rect()
        self.beingType = BeingType.WITCH
        self.block = BlockStatus.BLOCK_ALL
