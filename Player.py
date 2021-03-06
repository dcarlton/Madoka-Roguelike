import pygame
import sys
from Character import Character
from CombatUtils import CombatUtils
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
            self.score = 0

            # Ugh, poor naming...can be equal to ABILITY_ONE, ABILITY_TWO, etc. or None if not targeting
            self.targeting = None
            self.targetPath = []
            self.targetX = 0
            self.targetY = 0

        def die(self):
            if self.hp <= 0:
                super(Player, self).die()
                Event.diedEvent(BeingType.MAGICAL_GIRL)
                Event.lossEvent()

        def endTurn(self, success):
            for event in pygame.event.get(EventType.DIED):
                if event.beingType == BeingType.FAMILIAR:
                    self.killedFamiliar()
                elif event.beingType == BeingType.WITCH:
                    self.killedWitch()
                elif event.beingType == BeingType.WALPURGISNACHT:
                    self.killedWalpurgisnacht()
            return super(Player, self).endTurn(success)

        def killedFamiliar(self):
            self.score += FAMILIAR_SCORE

        def killedWitch(self):
            self.score += WITCH_SCORE
            self.magic += SOUL_GEM_MAGIC

        def killedWalpurgisnacht(self):
            self.score += WALPURGISNACHT_SCORE

        def takeTurn(self, event):
            if self.immobilized():
                return True

            if self.targeting is not None:
                success = self.takeTurnTargeting(event)
                return self.endTurn(success)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                magicLoss = self.abilityOne(self.x, self.y-1)
                if magicLoss is not None:
                    self.magic -= magicLoss
                    if self.magic <= 0:
                        Event.lossEvent()
                    return self.endTurn(True)
                success = self.move(Movement.MOVE_UP)
                return self.endTurn(success)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                magicLoss = self.abilityOne(self.x, self.y+1)
                if magicLoss is not None:
                    self.magic -= magicLoss
                    if self.magic <= 0:
                        Event.lossEvent()
                    return self.endTurn(True)
                success = self.move(Movement.MOVE_DOWN)
                return self.endTurn(success)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                magicLoss = self.abilityOne(self.x-1, self.y)
                if magicLoss is not None:
                    self.magic -= magicLoss
                    if self.magic <= 0:
                        Event.lossEvent()
                    return self.endTurn(True)
                success = self.move(Movement.MOVE_LEFT)
                return self.endTurn(success)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                magicLoss = self.abilityOne(self.x+1, self.y)
                if magicLoss is not None:
                    self.magic -= magicLoss
                    if self.magic <= 0:
                        Event.lossEvent()
                    return self.endTurn(True)
                success = self.move(Movement.MOVE_RIGHT)
                return self.endTurn(success)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_QUOTE:
                if self.abilityOneTargeted:
                    self.targeting = ABILITY_ONE
                    self.targetPath.append((self.x, self.y))
                    self.targetX = self.x
                    self.targetY = self.y
                    return False
                magicLoss = self.abilityOne(self,x, self.y)
                if magicLoss is None:
                    return False
                self.magic -= magicLoss
                if self.magic <= 0:
                    Event.lossEvent()
                return self.endTurn(True)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_COMMA:
                if self.abilityTwoTargeted:
                    self.targeting = ABILITY_TWO
                    self.targetPath.append((self.x, self.y))
                    self.targetX = self.x
                    self.targetY = self.y
                    return False
                magicLoss = self.abilityTwo(self.x, self.y)
                if magicLoss is None:
                    return False
                self.magic -= magicLoss
                if self.magic <= 0:
                    Event.lossEvent()
                return self.endTurn(True)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_PERIOD:
                if self.abilityThreeTargeted:
                    self.targeting = ABILITY_THREE
                    self.targetPath.append((self.x, self.y))
                    self.targetX = self.x
                    self.targetY = self.y
                    return False
                magicLoss = self.abilityThree(self.x, self.y)
                if magicLoss is None:
                    return False
                self.magic -= magicLoss
                if self.magic <= 0:
                    Event.lossEvent()
                return self.endTurn(True)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                if self.abilityFourTargeted:
                    self.targeting = ABILITY_FOUR
                    self.targetPath.append((self.x, self.y))
                    self.targetX = self.x
                    self.targetY = self.y
                    return False
                magicLoss = self.abilityFour(self.x, self.y)
                if magicLoss is None:
                    return False
                self.magic -= magicLoss
                if self.magic <= 0:
                    Event.lossEvent()
                return self.endTurn(True)

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                return self.endTurn(True)
            return False

        def takeTurnTargeting(self, event):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if self.targetY > 0 and CombatUtils.distance(self.x, self.y, self.targetX, self.targetY - 1) <= self.getRange(self.targeting):
                        self.targetY -= 1
                        self.targetPath.append((self.targetX, self.targetY))
                    return False

                elif event.key == pygame.K_DOWN:
                    if self.targetY < (MAP_HEIGHT - 1) and CombatUtils.distance(self.x, self.y, self.targetX, self.targetY + 1) <= self.getRange(self.targeting):
                        self.targetY += 1
                        self.targetPath.append((self.targetX, self.targetY))
                    return False

                elif event.key == pygame.K_LEFT:
                    if self.targetX > 0 and CombatUtils.distance(self.x, self.y, self.targetX - 1, self.targetY) <= self.getRange(self.targeting):
                        self.targetX -= 1
                        self.targetPath.append((self.targetX, self.targetY))
                    return False

                elif event.key == pygame.K_RIGHT:
                    if self.targetX < (MAP_WIDTH - 1) and CombatUtils.distance(self.x, self.y, self.targetX + 1, self.targetY) <= self.getRange(self.targeting):
                        self.targetX += 1
                        self.targetPath.append((self.targetX, self.targetY))
                    return False

                elif event.key == pygame.K_QUOTE and self.targeting == ABILITY_ONE:
                    self.targeting = None
                    if not board.grid[self.targetX][self.targetY].beings:
                        target = None
                    else:
                        target = board.grid[self.targetX][self.targetY].beings[-1]
                    if not CombatUtils.canTarget(target, self.abilityOneTargets):
                        self.targetPath = []
                        return False
                    magicLoss = self.abilityOne(self.targetX, self.targetY)
                    self.targetPath = []
                    if magicLoss is None:
                        return False
                    self.magic -= magicLoss
                    if self.magic <= 0:
                        Event.lossEvent()
                    return True

                elif event.key == pygame.K_COMMA and self.targeting == ABILITY_TWO:
                    self.targeting = None
                    if not board.grid[self.targetX][self.targetY].beings:
                        target = None
                    else:
                        target = board.grid[self.targetX][self.targetY].beings[-1]
                    if not CombatUtils.canTarget(target, self.abilityTwoTargets):
                        self.targetPath = []
                        return False
                    magicLoss = self.abilityTwo(self.targetX, self.targetY)
                    self.targetPath = []
                    if magicLoss is None:
                        return False
                    self.magic -= magicLoss
                    if self.magic <= 0:
                        Event.lossEvent()
                    return True

                elif event.key == pygame.K_PERIOD and self.targeting == ABILITY_THREE:
                    self.targeting = None
                    if not board.grid[self.targetX][self.targetY].beings:
                        target = None
                    else:
                        target = board.grid[self.targetX][self.targetY].beings[-1]
                    if not CombatUtils.canTarget(target, self.abilityThreeTargets):
                        self.targetPath = []
                        return False
                    magicLoss = self.abilityThree(self.targetX, self.targetY)
                    self.targetPath = []
                    if magicLoss is None:
                        return False
                    self.magic -= magicLoss
                    if self.magic <= 0:
                        Event.lossEvent()
                    return True

                elif event.key == pygame.K_p and self.targeting == ABILITY_FOUR:
                    self.targeting = None
                    if not board.grid[self.targetX][self.targetY].beings:
                        target = None
                    else:
                        target = board.grid[self.targetX][self.targetY].beings[-1]
                    if not CombatUtils.canTarget(target, self.abilityFourTargets):
                        self.targetPath = []
                        return False
                    magicLoss = self.abilityFour(self.targetX, self.targetY)
                    self.targetPath = []
                    if magicLoss is None:
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
