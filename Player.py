import pygame
import sys
from Character import Character
from Constants import *
from Enumerations import *
from Event import Event
from Map import Map
from TurnManager import TurnManager

ABILITY_ONE = 1
ABILITY_TWO = 2
ABILITY_THREE = 3
ABILITY_FOUR = 4

board = Map.getInstance()
turnManager = TurnManager.getInstance()

def makePlayer(being):
    class Player(being, Character):
        def __init__(self):
            being.__init__(self)

            # Ugh, poor naming...can be equal to ABILITY_ONE, ABILITY_TWO, etc. or None if not targeting
            self.targeting = None
            self.targetX = 0
            self.targetY = 0

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
            if self.targeting is not None:
                return self.takeTurnTargeting(event)

            # If the user uses an ability button, begin targeting
            # TO BE IMPLEMENTED

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

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_QUOTE:
                self.targeting = ABILITY_ONE
                # Setting targetX and targetY to a nearby enemy or the closest enemy would be awesome :)
                self.targetX = self.x
                self.targetY = self.y
                return False

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_COMMA:
                self.targeting = ABILITY_TWO
                # Setting targetX and targetY to a nearby enemy or the closest enemy would be awesome :)
                self.targetX = self.x
                self.targetY = self.y
                return False

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_PERIOD:
                self.targeting = ABILITY_THREE
                # Setting targetX and targetY to a nearby enemy or the closest enemy would be awesome :)
                self.targetX = self.x
                self.targetY = self.y
                return False

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                self.targeting = ABILITY_FOUR
                self.targetX = self.x
                self.targetY = self.y
                return False

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                return True
            return False

        def takeTurnTargeting(self, event):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if self.targetY > 0 and self.distance(self.x, self.y, self.targetX, self.targetY - 1) <= self.abilityOneRange:
                        self.targetY -= 1
                    return False

                elif event.key == pygame.K_DOWN:
                    if self.targetY < (MAP_HEIGHT - 1) and self.distance(self.x, self.y, self.targetX, self.targetY + 1) <= self.abilityOneRange:
                        self.targetY += 1
                    return False

                elif event.key == pygame.K_LEFT:
                    if self.targetX > 0 and self.distance(self.x, self.y, self.targetX - 1, self.targetY) <= self.abilityOneRange:
                        self.targetX -= 1
                    return False

                elif event.key == pygame.K_RIGHT:
                    if self.targetX < (MAP_WIDTH - 1) and self.distance(self.x, self.y, self.targetX + 1, self.targetY) <= self.abilityOneRange:
                        self.targetX += 1
                    return False

                elif event.key == pygame.K_QUOTE and self.targeting == ABILITY_ONE:
                    self.targeting = None
                    magicLoss = self.abilityOne(self.targetX, self.targetY)
                    if magicLoss == 0:
                        return False
                    self.magic -= magicLoss
                    if self.magic <= 0:
                        Event.lossEvent()
                    return True

                elif event.key == pygame.K_COMMA and self.targeting == ABILITY_TWO:
                    self.targeting = None
                    magicLoss = self.abilityTwo(self.targetX, self.targetY)
                    if magicLoss == 0:
                        return False
                    self.magic -= magicLoss
                    if self.magic <= 0:
                        Event.lossEvent()
                    return True

                elif event.key == pygame.K_PERIOD and self.targeting == ABILITY_THREE:
                    self.targeting = None
                    magicLoss = self.abilityThree(self.targetX, self.targetY)
                    if magicLoss == 0:
                        return False
                    self.magic -= magicLoss
                    if self.magic <= 0:
                        Event.lossEvent()
                    return True

                elif event.key == pygame.K_p and self.targeting == ABILITY_FOUR:
                    self.targeting = None
                    magicLoss = self.abilityFour(self.targetX, self.targetY)
                    if magicLoss == 0:
                        return False
                    self.magic -= magicLoss
                    if self.magic <= 0:
                        Event.lossEvent()
                    return True

                self.targeting = None
                return False

            # Mouse support to be implemented later
            return False

    return Player()
