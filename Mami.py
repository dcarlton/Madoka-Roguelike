import pygame
from Constants import *
from Enumerations import *
from Graphics import Graphics
from MagicalGirl import MagicalGirl
from Map import Map
from TurnManager import TurnManager

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

        self.abilityOneName = "Musket Slam"
        self.abilityOneDamage = 10
        self.abilityOneMagic = 5
        self.abilityOneRange = 1
        self.abilityOneStatus = None

        self.abilityTwoName = "Musket Shot"
        self.abilityTwoDamage = 15
        self.abilityTwoMagic = 10
        self.abilityTwoRange = 3
        self.abilityTwoStatus = None

        self.abilityThreeName = "Trio Finale"
        self.abilityThreeDamage = 45
        self.abilityThreeMagic = 25
        self.abilityThreeRange = 3
        self.abilityThreeStatus = None

        turnManager.delayFunction(self.regenerate, self.regenerationRate)

    # Using the default MagicalGirl class for abilities 1-3
