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

class Sayaka(MagicalGirl):
    def __init__(self):
        super(Sayaka, self).__init__()
        self.maxHP = 100
        self.hp = 100
        self.magic = 100
        self.x = 0
        self.y = 0
        self.regenerationRate = 5
        self.block = BlockStatus.BLOCK_ALL
        self.image = Images.getInstance().getImage(Sprites.SAYAKA_STANDING)
        self.rect = self.image.get_rect()
        self.beingType = BeingType.MAGICAL_GIRL
        self.score = 0

        self.abilityOneName = "Sword Slash"
        self.abilityOneDamage = 15
        self.abilityOneMagic = 5
        self.abilityOneRange = 1
        self.abilityOneStatus = None
        self.abilityOneTargeted = True
        self.abilityOneTargets = Victims.NON_PLAYER_AND_HUMAN

        self.abilityTwoName = "Sword Toss"
        self.abilityTwoDamage = 10
        self.abilityTwoMagic = 15
        self.abilityTwoRange = 3
        self.abilityTwoStatus = None
        self.abilityTwoTargeted = True
        self.abilityTwoTargets = Victims.NON_PLAYER_AND_HUMAN

        self.abilityThreeName = "Aqua Jet"
        self.abilityThreeDamage = 10
        self.abilityThreeMagic = 0 # Using this so extra Magic won't be used up for each character hit by the jet
        self.abilityThreeRange = float('inf')
        self.abilityThreeStatus = None
        self.abilityThreeTargeted = True
        self.abilityThreeTargets = Victims.EVERYTHING
        self.jetMagicCost = 5

        self.abilityFourName = "Heal"
        self.abilityFourDamage = -50
        self.abilityFourMagic = 10
        self.abilityFourRange = float('inf')
        self.abilityFourStatus = None
        self.abilityFourTargeted = False
        self.abilityFourTargets = Victims.NON_ENEMY

        turnManager.delayFunction(self.regenerate, self.regenerationRate)

    # Letting the MagicalGirl class handle abilities 1 and 2
    def abilityThree(self, x, y):
        targets = []
        firstSpace = self.targetPath.pop(0)
        prevSpace = firstSpace
        if not self.targetPath:
            return None

        for space in self.targetPath:
            if board.grid[space[0]][space[1]].beings:
                target = board.grid[space[0]][space[1]].beings[-1]
                if target not in targets:
                    targets.append(target)
                if (space[0] - prevSpace[0]) == 1:
                    target.move(Movement.MOVE_RIGHT)
                elif (space[0] - prevSpace[0]) == -1:
                    target.move(Movement.MOVE_LEFT)
                elif (space[1] - prevSpace[1]) == 1:
                    target.move(Movement.MOVE_DOWN)
                elif (space[1] - prevSpace[1]) == -1:
                    target.move(Movement.MOVE_UP)
            prevSpace = space
        self.targetPath.insert(0, firstSpace)

        for space in reversed(self.targetPath):
            success = self.teleport(space[0], space[1])
            if success:
                break

        for target in targets:
            super(Sayaka, self).abilityThree(target.x, target.y)
        return self.jetMagicCost * len(self.targetPath)

    def abilityFour(self, x, y):
        if self.hp >= self.maxHP:
            return None
        self.hp -= self.abilityFourDamage
        if self.hp > self.maxHP:
            self.hp = self.maxHP
        self.magic -= self.abilityFourMagic
        return self.abilityFourMagic

    def die(self):
        pass

    def endTurn(self, success):
        return success
