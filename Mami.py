import pygame
from Constants import *
from Enumerations import *
from Graphics import Graphics
from MagicalGirl import MagicalGirl
from Map import Map
from TurnManager import TurnManager

MUSKET_SLAM_DAMAGE = 10
MUSKET_SLAM_MAGIC = 5

board = Map.getInstance()
turnManager = TurnManager.getInstance()

class Mami(MagicalGirl):
    def __init__(self):
        self.maxHP = 1000
        self.hp = 1000
        self.magic = 100
        self.x = 0
        self.y = 0
        self.regenerationRate = 5
        self.block = BlockStatus.BLOCK_ALL
        self.image = Graphics.getInstance().getImage(Images.MAMI_STANDING)
        self.rect = self.image.get_rect()
        self.beingType = BeingType.MAGICAL_GIRL
        self.score = 0
        turnManager.delayFunction(self.regenerate, self.regenerationRate)

    def abilityOne(self, x, y):
        if not (-1 < x and x < MAP_WIDTH and -1 < y and y < MAP_HEIGHT):
            return 0
        if len((board.grid[x][y]).beings) > 0:
            ((board.grid[x][y]).beings[-1]).hp -= MUSKET_SLAM_DAMAGE
            if ((board.grid[x][y]).beings[-1]).hp <= 0:
                dead = (board.grid[x][y]).beings[-1]
                if dead.beingType == BeingType.FAMILIAR:
                    self.score += 100
                elif dead.beingType == BeingType.WITCH:
                    self.score += 100
                    self.magic += 200
                ((board.grid[x][y]).beings[-1]).die()
            return MUSKET_SLAM_MAGIC
        return 0

    def regenerate(self):
        if self.hp < self.maxHP:
            self.hp += 1
        turnManager.delayFunction(self.regenerate, self.regenerationRate)
