from Character import Character
import sys
import random
from Constants import *
from Enumerations import *
from Event import Event
from Map import Map

board = Map.getInstance()

def makeEnemy(being):
    class Enemy(being, Character):
        def __init__(self):
            super(Enemy, self).__init__()
            self.target = None

        def takeTurn(self):
            # For now, just move in a random direction unless the player is nearby
            if self.immobilized():
                return True

            if self.attack():
                return
            direction = random.choice([Movement.MOVE_UP, Movement.MOVE_DOWN, Movement.MOVE_LEFT, Movement.MOVE_RIGHT])
            self.move(direction)

        def attack(self):
            # For now, attack anything above, then right, then below, then left
            being = None
            if self.y > 0 and len((board.grid[self.x][self.y-1]).beings) > 0:
                being = (board.grid[self.x][self.y-1]).beings[-1]
                if being is not None and being.__class__.__name__ != "Enemy":
                    being.takeDamage(self, self.strength)
                    return True

            if self.x < (MAP_WIDTH - 1) and len((board.grid[self.x+1][self.y]).beings) > 0:
                being = (board.grid[self.x+1][self.y]).beings[-1]
                if being is not None and being.__class__.__name__ != "Enemy":
                    being.takeDamage(self, self.strength)
                    return True

            if self.y < (MAP_HEIGHT - 1) and len((board.grid[self.x][self.y+1]).beings) > 0:
                being = (board.grid[self.x][self.y+1]).beings[-1]
                if being is not None and being.__class__.__name__ != "Enemy":
                    being.takeDamage(self, self.strength)
                    return True

            if self.x > 0 and len((board.grid[self.x-1][self.y]).beings) > 0:
                being = (board.grid[self.x-1][self.y]).beings[-1]
                if being is not None and being.__class__.__name__ != "Enemy":
                    being.takeDamage(self, self.strength)
                    return True

            return False

        def die(self):
            if self.hp <= 0:
                super(Enemy, self).die()
                board.removeBeing(self)
                self.x = -1
                self.y = -1

        def takeDamage(self, attacker, damage):
            self.hp -= damage
            self.target = attacker
            if self.hp <= 0:
                self.die()

    return Enemy()
