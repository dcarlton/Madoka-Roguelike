import math
import sys
from Constants import *
from Enumerations import *
from Map import Map

board = Map.getInstance()

class Character:
    def __eq__(self, other):
        # Works as long as two characters of the same type
        # Cannot stand in the same space
        if self.beingType == other.beingType and self.x == other.x and self.y == other.y:
            return True
        return False

    def die(self):
        if self.hp <= 0:
            (board.grid[self.x][self.y]).removeBeing(self)
            self.x = -1
            self.y = -1

    def immobilized(self):
        for status in self.status:
            if status == Status.STUN:
                return True
        return False

    def move(self, direction):
        if direction == Movement.MOVE_DOWN and self.y > -1 and self.y < (MAP_HEIGHT - 1):
            if (board.grid[self.x][self.y+1]).canMove(self):
                (board.grid[self.x][self.y]).removeBeing(self)
                self.y += 1
                (board.grid[self.x][self.y]).addBeing(self)
                return True
            return False
        elif direction == Movement.MOVE_UP and self.y > 0 and self.y < MAP_HEIGHT:
            if (board.grid[self.x][self.y-1]).canMove(self):
                (board.grid[self.x][self.y]).removeBeing(self)
                self.y -= 1
                (board.grid[self.x][self.y]).addBeing(self)
                return True
            return False
        elif direction == Movement.MOVE_LEFT and self.x > 0 and self.x < MAP_WIDTH:
            if (board.grid[self.x-1][self.y]).canMove(self):
                (board.grid[self.x][self.y]).removeBeing(self)
                self.x -= 1
                (board.grid[self.x][self.y]).addBeing(self)
                return True
            return False
        elif direction == Movement.MOVE_RIGHT and self.x > -1 and self.x < (MAP_WIDTH - 1):
            if (board.grid[self.x+1][self.y]).canMove(self):
                (board.grid[self.x][self.y]).removeBeing(self)
                self.x += 1
                (board.grid[self.x][self.y]).addBeing(self)
                return True
            return False
        return False

    def takeDamage(self, attacker, damage):
            self.hp -= damage
            if self.hp <= 0:
                self.die()

    def teleport(self, x, y):
        if x < 0 or x >= MAP_WIDTH or y < 0 or y >= MAP_HEIGHT:
            return False
        if board.grid[x][y].canMove(self):
            board.grid[self.x][self.y].removeBeing(self)
            board.grid[x][y].addBeing(self)
            self.x = x
            self.y = y
            return True
        return False