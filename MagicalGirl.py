from Being import Being
from Constants import *
from Enumerations import BeingType
from Map import Map
from TurnManager import TurnManager

board = Map.getInstance()
turnManager = TurnManager.getInstance()

class MagicalGirl(Being):
    # All of the MagicalGirl subclasses are basically used as structs
    # They maintain the player/allies initial stats and abilities
    def __init__(self):
        pass

    def abilityOne(self, x, y):
        if not (-1 < x and x < MAP_WIDTH and -1 < y and y < MAP_HEIGHT):
            return 0
        if self.distance(self.x, self.y, x, y) > self.abilityOneRange:
            return 0
        if len((board.grid[x][y]).beings) > 0:
            if board.grid[x][y].beings[-1] == self:
                return 0
            ((board.grid[x][y]).beings[-1]).hp -= self.abilityOneDamage
            if ((board.grid[x][y]).beings[-1]).hp <= 0:
                dead = (board.grid[x][y]).beings[-1]
                if dead.beingType == BeingType.FAMILIAR:
                    self.score += 100
                elif dead.beingType == BeingType.WITCH:
                    self.score += 100
                    self.magic += 200
                ((board.grid[x][y]).beings[-1]).die()
            return self.abilityOneMagic
        return 0

    def abilityTwo(self, x, y):
        if not (-1 < x and x < MAP_WIDTH and -1 < y and y < MAP_HEIGHT):
            return 0
        if self.distance(self.x, self.y, x, y) > self.abilityTwoRange:
            return 0
        if len((board.grid[x][y]).beings) > 0:
            if board.grid[x][y].beings[-1] == self:
                return 0
            ((board.grid[x][y]).beings[-1]).hp -= self.abilityTwoDamage
            if ((board.grid[x][y]).beings[-1]).hp <= 0:
                dead = (board.grid[x][y]).beings[-1]
                if dead.beingType == BeingType.FAMILIAR:
                    self.score += 100
                elif dead.beingType == BeingType.WITCH:
                    self.score += 100
                    self.magic += 200
                ((board.grid[x][y]).beings[-1]).die()
            return self.abilityTwoMagic
        return 0

    def abilityThree(self, x, y):
        if not (-1 < x and x < MAP_WIDTH and -1 < y and y < MAP_HEIGHT):
            return 0
        if self.distance(self.x, self.y, x, y) > self.abilityThreeRange:
            return 0
        if len((board.grid[x][y]).beings) > 0:
            if board.grid[x][y].beings[-1] == self:
                return 0
            ((board.grid[x][y]).beings[-1]).hp -= self.abilityThreeDamage
            if ((board.grid[x][y]).beings[-1]).hp <= 0:
                dead = (board.grid[x][y]).beings[-1]
                if dead.beingType == BeingType.FAMILIAR:
                    self.score += 100
                elif dead.beingType == BeingType.WITCH:
                    self.score += 100
                    self.magic += 200
                ((board.grid[x][y]).beings[-1]).die()
            return self.abilityThreeMagic
        return 0

    def getRange(self, ability):
        if ability == 1:
            return self.abilityOneRange
        elif ability == 2:
            return self.abilityTwoRange
        elif ability == 3:
            return self.abilityThreeRange
        elif ability == 4:
            return self.abilityFourRange
        return False

    def regenerate(self):
        if self.hp < self.maxHP:
            self.hp += 1
        turnManager.delayFunction(self.regenerate, self.regenerationRate)
