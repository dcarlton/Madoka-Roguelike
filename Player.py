import pygame
import sys
from Character import Character
from Constants import *
from Enumerations import *
from Event import Event
from Map import Map
from TurnManager import TurnManager

board = Map.getInstance()
turnManager = TurnManager.getInstance()

def makePlayer(being):
    class Player(being, Character):
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

        def takeTurn(self, event):
            magicLoss = 0
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                magicLoss = self.abilityOne(self.x, self.y-1)
                if magicLoss != 0:
                    self.magic -= magicLoss
                    if self.magic <= 0:
                        Event.lossEvent()
                    return True
                return self.move(Movement.MOVE_UP)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                magicLoss = self.abilityOne(self.x, self.y+1)
                if magicLoss != 0:
                    self.magic -= magicLoss
                    if self.magic <= 0:
                        Event.lossEvent()
                    return True
                return self.move(Movement.MOVE_DOWN)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                magicLoss = self.abilityOne(self.x-1, self.y)
                if magicLoss != 0:
                    self.magic -= magicLoss
                    if self.magic <= 0:
                        Event.lossEvent()
                    return True
                return self.move(Movement.MOVE_LEFT)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                magicLoss = self.abilityOne(self.x+1, self.y)
                if magicLoss != 0:
                    self.magic -= magicLoss
                    if self.magic <= 0:
                        Event.lossEvent()
                    return True
                return self.move(Movement.MOVE_RIGHT)

            return False

    return Player()
