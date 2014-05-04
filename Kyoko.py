import pygame
from CombatUtils import CombatUtils
from Constants import *
from Enumerations import *
from Event import Event
from Images import Images
from MagicalGirl import MagicalGirl
from Map import Map
from TurnManager import TurnManager

board = Map.getInstance()
turnManager = TurnManager.getInstance()

class Kyoko(MagicalGirl):
    def __init__(self):
        super(Kyoko, self).__init__()
        self.maxHP = 100
        self.hp = 100
        self.magic = 100
        self.x = 0
        self.y = 0
        self.regenerationRate = 5
        self.block = BlockStatus.BLOCK_ALL
        self.image = Images.getInstance().getImage(Sprites.KYOKO_STANDING)
        self.rect = self.image.get_rect()
        self.beingType = BeingType.MAGICAL_GIRL
        self.score = 0

        self.abilityOneName = "Spear Thrust"
        self.abilityOneDamage = 15
        self.abilityOneMagic = 5
        self.abilityOneRange = 2
        self.abilityOneStatus = None
        self.abilityOneTargeted = True
        self.abilityOneTargets = Victims.NON_PLAYER_AND_HUMAN

        self.abilityTwoName = "Spear Spin"
        self.abilityTwoDamage = 15
        self.abilityTwoMagic = 0 # Using this so extra Magic won't be used up for each character hit by the spin
        self.abilityTwoRange = 2
        self.abilityTwoStatus = None
        self.abilityTwoTargeted = False
        self.abilityTwoTargets = Victims.NON_PLAYER_AND_HUMAN
        self.spinMagicCost =15

        self.abilityThreeName = "Spear Slam"
        self.abilityThreeDamage = 10
        self.abilityThreeMagic = 10
        self.abilityThreeRange = 2
        self.abilityThreeStatus = Status.STUN
        self.abilityThreeTargeted = True
        self.abilityThreeTargets = Victims.NON_PLAYER_AND_HUMAN
        self.stunDuration = 5

        self.abilityFourName = "Barrier"
        self.abilityFourDamage = 0
        self.abilityFourMagic = 5
        self.abilityFourRange = float('inf')
        self.abilityFourStatus = None
        self.abilityFourTargeted = True
        self.abilityFourTargets = Victims.EVERYTHING
        self.barrierDuration = 5

        self.barriers = []
        self.stunVictims = []

        turnManager.delayFunction(self.regenerate, self.regenerationRate)

    def abilityTwo(self, x, y):
        for xIndex in range(self.x - self.abilityTwoRange, self.x + self.abilityTwoRange + 1):
            for yIndex in range(self.y - self.abilityTwoRange, self.y + self.abilityTwoRange + 1):
                if xIndex < 0 or xIndex >= MAP_WIDTH or yIndex < 0 or yIndex >= MAP_HEIGHT:
                    continue
                if CombatUtils.distance(self.x, self.y, xIndex, yIndex) > self.abilityTwoRange:
                    continue
                if self.x == xIndex and self.y == yIndex:
                    continue
                super(Kyoko, self).abilityTwo(xIndex, yIndex)
        return self.spinMagicCost

    def abilityThree(self, x, y):
        magicLoss = super(Kyoko, self).abilityThree(x, y)
        if magicLoss is not None:
            self.stunVictims.append(board.grid[x][y].beings[-1])
            turnManager.delayFunction(self.cureStun, self.stunDuration)
        return magicLoss

    def abilityFour(self, x, y):
        if not board.grid[x][y].beings:
            board.grid[x][y].barrier = True
            turnManager.delayFunction(self.removeBarrier, self.barrierDuration)
            self.barriers.append((x, y))

            self.magic -= self.abilityFourMagic
            if self.magic <= 0:
                self.die()
        return None

    def cureStun(self):
        victim = self.stunVictims.pop(0)
        if victim is not None:
            try:
                victim.status.remove(Status.STUN)
            except:
                # WHY DOES PYTHON THROW AN EXCEPTION FOR THIS AAAARGGSEOTNHU
                pass

    def die(self):
        pass

    def endTurn(self, success):
        return success

    def removeBarrier(self):
        barrier = self.barriers.pop(0)
        board.grid[barrier[0]][barrier[1]].barrier = False
