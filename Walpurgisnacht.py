import pygame
import sys
from Witch import Witch
from Enumerations import *
from Event import Event
from Graphics import Graphics
from TurnManager import TurnManager
from Map import Map

board = Map.getInstance()
turnManager = TurnManager.getInstance()

class Walpurgisnacht(Witch):
    def __init__(self):
        self.hp = 150
        self.strength = 25
        self.image = Graphics.getInstance().getImage(Images.WALPURGISNACHT_STANDING)
        self.rect = self.image.get_rect()
        self.beingType = BeingType.WALPURGISNACHT
        self.block = BlockStatus.BLOCK_ALL
        self.controller = 0

    def die(self):
        print("Game over!")
        if self.hp <= 0:
            (board.grid[self.x][self.y]).removeBeing(self)
            self.x = -1
            self.y = -1
        Event.winEvent()
