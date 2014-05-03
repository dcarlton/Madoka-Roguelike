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
        if len((board.grid[x][y]).beings) > 0:
            ((board.grid[x][y]).beings[-1]).takeDamage(self, self.abilityOneDamage)
            if self.abilityOneStatus is not None:
                ((board.grid[x][y]).beings[-1]).status.append(self.abilityOneStatus)
            return self.abilityOneMagic
        return None

    def abilityTwo(self, x, y):
        if not (-1 < x and x < MAP_WIDTH and -1 < y and y < MAP_HEIGHT):
            return None
        if len((board.grid[x][y]).beings) > 0:
            ((board.grid[x][y]).beings[-1]).takeDamage(self, self.abilityTwoDamage)
            if self.abilityTwoStatus is not None:
                ((board.grid[x][y]).beings[-1]).status.append(self.abilityTwoStatus)
            return self.abilityTwoMagic
        return None

    def abilityThree(self, x, y):
        if not (-1 < x and x < MAP_WIDTH and -1 < y and y < MAP_HEIGHT):
            return None
        if len((board.grid[x][y]).beings) > 0:
            ((board.grid[x][y]).beings[-1]).takeDamage(self, self.abilityThreeDamage)
            if self.abilityThreeStatus is not None:
                ((board.grid[x][y]).beings[-1]).status.append(self.abilityThreeStatus)
            return self.abilityThreeMagic
        return None

    def abilityFour(self, x, y):
        if not (-1 < x and x < MAP_WIDTH and -1 < y and y < MAP_HEIGHT):
            return None
        if len((board.grid[x][y]).beings) > 0:
            ((board.grid[x][y]).beings[-1]).takeDamage(self, self.abilityFourDamage)
            if self.abilityFourStatus is not None:
                ((board.grid[x][y]).beings[-1]).status.append(self.abilityFourStatus)
            return self.abilityFourMagic
        return None

    def endTurn(self, success):
        # Each magical girl can overwrite this class to do end-of-turn effects, mainly Time Stop hijinks
        # Currently only called if success might be true; turns which were not taken are ignored
        return success

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
