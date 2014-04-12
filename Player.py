from Character import Character
import pygame
import sys
from Constants import *
from Enumerations import *
from Event import Event
from Map import Map
from TurnManager import TurnManager

board = Map.getInstance()
turnManager = TurnManager.getInstance()

class Player(Character):
    def __init__(self, being):
        self.maxHP = being.hp
        self.hp = being.hp
        self.magic = being.magic
        self.regenerationRate = being.regenerationRate
        self.block = BlockStatus.BLOCK_ALL
        self.x = int(MAP_WIDTH / 2)
        self.y = int(MAP_HEIGHT / 2)
        self.image = being.image
        self.rect = being.rect
        self.being = being
        self.beingType = being.beingType
        self.being.controller = self
        self.score = 0
        turnManager.delayFunction(self.regenerate, self.regenerationRate)

    def die(self):
        if self.hp <= 0:
            (board.grid[self.x][self.y]).removeBeing(self)
            self.x = -1
            self.y = -1
        Event.lossEvent()

    def killedFamiliar(self):
        self.score += 100

    def killedWitch(self):
        self.score += 100
        self.magic += 200

    def regenerate(self):
        if self.hp < self.maxHP:
            self.hp += 1
        turnManager.delayFunction(self.regenerate, self.regenerationRate)

    def takeTurn(self, event):
        magicLoss = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            magicLoss = self.being.abilityOne(self.x, self.y-1)
            if magicLoss != 0:
                self.magic -= magicLoss
                return True
            return self.move(Movement.MOVE_UP)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            magicLoss = self.being.abilityOne(self.x, self.y+1)
            if magicLoss != 0:
                self.magic -= magicLoss
                return True
            return self.move(Movement.MOVE_DOWN)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            magicLoss = self.being.abilityOne(self.x-1, self.y)
            if magicLoss != 0:
                self.magic -= magicLoss
                return True
            return self.move(Movement.MOVE_LEFT)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            magicLoss = self.being.abilityOne(self.x+1, self.y)
            if magicLoss != 0:
                self.magic -= magicLoss
                return True
            return self.move(Movement.MOVE_RIGHT)
        return False
