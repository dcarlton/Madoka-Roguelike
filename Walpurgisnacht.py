from Being import Being
from Enumerations import *
from Event import Event
from Graphics import Graphics
from Map import Map

board = Map.getInstance()

class Walpurgisnacht(Being):
    def __init__(self):
        super(Walpurgisnacht, self).__init__()
        self.hp = 150
        self.strength = 25
        self.image = Graphics.getInstance().getImage(Images.WALPURGISNACHT_STANDING)
        self.rect = self.image.get_rect()
        self.beingType = BeingType.WALPURGISNACHT
        self.block = BlockStatus.BLOCK_ALL

    def die(self):
        if self.hp <= 0:
            (board.grid[self.x][self.y]).removeBeing(self)
            self.x = -1
            self.y = -1
            Event.winEvent()
