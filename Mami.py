import pygame
from Constants import *
from Enumerations import *
from Images import Images
from MagicalGirl import MagicalGirl
from Map import Map
from TurnManager import TurnManager

board = Map.getInstance()
turnManager = TurnManager.getInstance()

class Mami(MagicalGirl):
    def __init__(self):
        super(Mami, self).__init__()
        self.maxHP = 100
        self.hp = 100
        self.magic = 100
        self.x = 0
        self.y = 0
        self.regenerationRate = 5
        self.block = BlockStatus.BLOCK_ALL
        self.image = Images.getInstance().getImage(Sprites.MAMI_STANDING)
        self.rect = self.image.get_rect()
        self.beingType = BeingType.MAGICAL_GIRL
        self.score = 0
        self.ribbonVictim = None

        self.abilityOneName = "Musket Slam"
        self.abilityOneDamage = 10
        self.abilityOneMagic = 3
        self.abilityOneRange = 1
        self.abilityOneStatus = None
        self.abilityOneTargeted = True
        self.abilityOneTargets = Victims.NON_PLAYER_AND_HUMAN

        self.abilityTwoName = "Musket Shot"
        self.abilityTwoDamage = 15
        self.abilityTwoMagic = 5
        self.abilityTwoRange = 3
        self.abilityTwoStatus = None
        self.abilityTwoTargeted = True
        self.abilityTwoTargets = Victims.NON_PLAYER_AND_HUMAN

        self.abilityThreeName = "Trio Finale"
        self.abilityThreeDamage = 45
        self.abilityThreeMagic = 25
        self.abilityThreeRange = 3
        self.abilityThreeStatus = None
        self.abilityThreeTargeted = True
        self.abilityThreeTargets = Victims.NON_PLAYER_AND_HUMAN

        self.abilityFourName = "Ribbon Tie"
        self.abilityFourDamage = 0
        self.abilityFourMagic = 15
        self.abilityFourRange = float('inf')
        self.abilityFourStatus = Status.STUN
        self.abilityFourTargeted = True
        self.abilityFourTargets = Victims.NON_PLAYER

        turnManager.delayFunction(self.regenerate, self.regenerationRate)

    # Using the default MagicalGirl class for abilities 1-3
    def abilityFour(self, x=-1, y=-1):
        if self.ribbonVictim is not None:
            self.untie()
            turnManager.removeDelayedFunction(self.untie, 10)
            return 0
        magicLoss = super(Mami, self).abilityFour(x, y)
        if magicLoss is not None:
            # Something has been tied up. Next time this ability is used, it should be released
            self.ribbonVictim = board.grid[x][y].beings[-1]
            self.abilityFourTargeted = False
            turnManager.delayFunction(self.untie, 10)
            return magicLoss
        return None

    def die(self):
        if self.ribbonVictim is not None:
            self.untie()
            turnManager.removeDelayedFunction(self.untie, 10)

    def untie(self):
        if self.ribbonVictim is not None:
            self.ribbonVictim.status.remove(Status.STUN)
            self.ribbonVictim = None
            self.abilityFourTargeted = True
