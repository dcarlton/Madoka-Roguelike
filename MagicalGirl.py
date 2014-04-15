from Being import Being
from Constants import *
from Enumerations import BeingType
from Map import Map
from TurnManager import TurnManager

board = Map.getInstance()
turnManager = TurnManager.getInstance()

class MagicalGirl(Being):
    def __init__(self):
        super(MagicalGirl, self).__init__()

    def abilityOne(self, x, y):
        if not (-1 < x and x < MAP_WIDTH and -1 < y and y < MAP_HEIGHT):
            return None
        if self.distance(self.x, self.y, x, y) > self.abilityOneRange:
            return None
        if len((board.grid[x][y]).beings) > 0:
            if board.grid[x][y].beings[-1] == self:
                return None
            ((board.grid[x][y]).beings[-1]).hp -= self.abilityOneDamage
            if self.abilityOneStatus is not None:
                ((board.grid[x][y]).beings[-1]).status.append(self.abilityOneStatus)
            if ((board.grid[x][y]).beings[-1]).hp <= 0:
                dead = (board.grid[x][y]).beings[-1]
                if dead.beingType == BeingType.FAMILIAR:
                    self.score += 100
                elif dead.beingType == BeingType.WITCH:
                    self.score += 100
                    self.magic += 200
                ((board.grid[x][y]).beings[-1]).die()
            return self.abilityOneMagic
        return None

    def abilityTwo(self, x, y):
        if not (-1 < x and x < MAP_WIDTH and -1 < y and y < MAP_HEIGHT):
            return None
        if self.distance(self.x, self.y, x, y) > self.abilityTwoRange:
            return None
        if len((board.grid[x][y]).beings) > 0:
            if board.grid[x][y].beings[-1] == self:
                return None
            ((board.grid[x][y]).beings[-1]).hp -= self.abilityTwoDamage
            if self.abilityTwoStatus is not None:
                ((board.grid[x][y]).beings[-1]).status.append(self.abilityTwoStatus)
            if ((board.grid[x][y]).beings[-1]).hp <= 0:
                dead = (board.grid[x][y]).beings[-1]
                if dead.beingType == BeingType.FAMILIAR:
                    self.score += 100
                elif dead.beingType == BeingType.WITCH:
                    self.score += 100
                    self.magic += 200
                ((board.grid[x][y]).beings[-1]).die()
            return self.abilityTwoMagic
        return None

    def abilityThree(self, x, y):
        if not (-1 < x and x < MAP_WIDTH and -1 < y and y < MAP_HEIGHT):
            return None
        if self.distance(self.x, self.y, x, y) > self.abilityThreeRange:
            return None
        if len((board.grid[x][y]).beings) > 0:
            if board.grid[x][y].beings[-1] == self:
                return None
            ((board.grid[x][y]).beings[-1]).hp -= self.abilityThreeDamage
            if self.abilityThreeStatus is not None:
                ((board.grid[x][y]).beings[-1]).status.append(self.abilityThreeStatus)
            if ((board.grid[x][y]).beings[-1]).hp <= 0:
                dead = (board.grid[x][y]).beings[-1]
                if dead.beingType == BeingType.FAMILIAR:
                    self.score += 100
                elif dead.beingType == BeingType.WITCH:
                    self.score += 100
                    self.magic += 200
                ((board.grid[x][y]).beings[-1]).die()
            return self.abilityThreeMagic
        return None

    def abilityFour(self, x, y):
        if not (-1 < x and x < MAP_WIDTH and -1 < y and y < MAP_HEIGHT):
            return None
        if self.distance(self.x, self.y, x, y) > self.abilityFourRange:
            return None
        if len((board.grid[x][y]).beings) > 0:
            if board.grid[x][y].beings[-1] == self:
                return None
            ((board.grid[x][y]).beings[-1]).hp -= self.abilityFourDamage
            if self.abilityFourStatus is not None:
                ((board.grid[x][y]).beings[-1]).status.append(self.abilityFourStatus)
            if ((board.grid[x][y]).beings[-1]).hp <= 0:
                dead = (board.grid[x][y]).beings[-1]
                if dead.beingType == BeingType.FAMILIAR:
                    self.score += 100
                elif dead.beingType == BeingType.WITCH:
                    self.score += 100
                    self.magic += 200
                ((board.grid[x][y]).beings[-1]).die()
            return self.abilityFourMagic
        return None

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
