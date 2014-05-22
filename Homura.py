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

class Homura(MagicalGirl):
    def __init__(self):
        super(Homura, self).__init__()
        self.image = Images.getInstance().getImage(Sprites.HOMURA_STANDING)
        self.rect = self.image.get_rect()

        self.bombs = []
        self.timeStopped = False

        self.abilityOneName = "Golf Club"
        self.abilityOneDamage = 10
        self.abilityOneMagic = 5
        self.abilityOneRange = 1
        self.abilityOneStatus = None
        self.abilityOneTargeted = True
        self.abilityOneTargets = Victims.NON_PLAYER_AND_HUMAN

        self.abilityTwoName = "Pistol"
        self.abilityTwoDamage = 15
        self.abilityTwoMagic = 10
        self.abilityTwoRange = 3
        self.abilityTwoStatus = None
        self.abilityTwoTargeted = True
        self.abilityTwoTargets = Victims.NON_PLAYER_AND_HUMAN

        self.abilityThreeName = "Bomb"
        self.abilityThreeDamage = 25
        self.abilityThreeMagic = 0 # Using this so extra Magic won't be used up for each character hit by the explosion
        self.abilityThreeRange = 1
        self.abilityThreeStatus = None
        self.abilityThreeTargeted = True
        self.abilityThreeTargets = Victims.EVERYTHING
        self.bombMagicCost = 10
        self.bombTimer = 0
        self.bombBlastZone = 2

        self.abilityFourName = "Time Stop"
        self.abilityFourDamage = 0
        self.abilityFourMagic = 2
        self.abilityFourRange = float('inf')
        self.abilityFourStatus = None
        self.abilityFourTargeted = False
        self.abilityFourTargets = Victims.EVERYTHING

        turnManager.delayFunction(self.regenerate, self.regenerationRate)

    # Letting the MagicalGirl class handle abilities 1 and 2
    def abilityThree(self, x, y):
        self.bombs.append((x, y))
        turnManager.delayFunction(self.detonate, self.bombTimer)
        return self.bombMagicCost

    def abilityFour(self, x, y):
        if self.timeStopped:
            self.timeStopped = False
            return 0 # Magic is only used up at the end of the turn
        self.timeStopped = True
        self.magic -= self.abilityFourMagic
        return None

    def detonate(self):
        bomb = self.bombs.pop(0)
        # Remember to account for range starting at the first parameter, and stopping before the second parameter
        # Which is really stupid <_< Why do that??? It's just confusing IMO
        for x in range(bomb[0] - self.bombBlastZone, bomb[0] + self.bombBlastZone + 1):
            for y in range(bomb[1] - self.bombBlastZone, bomb[1] + self.bombBlastZone + 1):
                # This is REALLY inefficient, the loops make a square where there should be a diamond of explosions
                if x < 0 or x >= MAP_WIDTH or y < 0 or y >= MAP_HEIGHT:
                    continue
                if CombatUtils.distance(x, y, bomb[0], bomb[1]) > self.bombBlastZone:
                    continue
                super(Homura, self).abilityThree(x, y)

        # Normally, enemy deaths are checked at the end of the player's turn
        # But bombs don't work that way
        for event in pygame.event.get(EventType.DIED):
            if event.beingType == BeingType.FAMILIAR:
                self.killedFamiliar()
            elif event.beingType == BeingType.WITCH:
                self.killedWitch()
            elif event.beingType == BeingType.WALPURGISNACHT:
                self.killedWalpurgisnacht()

    def die(self):
        self.timeStopped = False

    def endTurn(self, success):
        if success == False or not self.timeStopped:
            return success
        self.magic -= self.abilityFourMagic
        if self.magic <= 0:
            self.die()
        return False
