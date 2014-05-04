from Character import Character
import sys
import random
from CombatUtils import *
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
            self.turnsHuntingTarget = 0

        def takeTurn(self):
            self.turnsHuntingTarget += 1
            if self.immobilized():
                return True

            # If a target has been found, stay focused on following and attacking them
            # For at least two turns, until a new character attacks this enemy
            if self.target is None or CombatUtils.distance(self.x, self.y, self.target.x, self.target.y) > self.vision:
                # Search around the enemy for a new target to focus on
                # Starting with the closest spaces, and expanding outward
                self.target = None
                self.turnsHuntingTarget = 0
                for interval in range(1, self.vision + 1):
                    for x in range(self.x - interval, self.x + interval + 1):
                        if x < 0 or x >= MAP_WIDTH:
                            continue

                        y = self.y - interval + abs(self.x - x)
                        if y > 0 and y < MAP_HEIGHT and board.grid[x][y].beings:
                            if board.grid[x][y].beings[-1].__class__.__name__ != "Enemy":
                                self.target = board.grid[x][y].beings[-1]
                                break

                        y = self.y + interval - abs(self.x - x)
                        if y > 0 and y < MAP_HEIGHT and board.grid[x][y].beings:
                            if board.grid[x][y].beings[-1].__class__.__name__ != "Enemy":
                                self.target = board.grid[x][y].beings[-1]
                                break
                    if self.target is not None:
                        break

            if self.target is not None:
                if CombatUtils.distance(self.x, self.y, self.target.x, self.target.y) <= self.range:
                    board.grid[self.target.x][self.target.y].beings[-1].takeDamage(self, self.strength)
                    return True
            self.move()
            return True

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

        def move(self):
            directions = []
            if self.target is None:
                directions = [Movement.MOVE_UP, Movement.MOVE_DOWN, Movement.MOVE_LEFT, Movement.MOVE_RIGHT]
                random.shuffle(directions)
            else:
                # Determine which directions will most likely lead toward the targt
                # This isn't technically an algorithm :(
                # But mostly works practically speaking
                # Mostly
                xDistance = abs(self.x - self.target.x)
                yDistance = abs(self.y - self.target.y)
                if xDistance < yDistance:
                    if self.y < self.target.y:
                        directions.append(Movement.MOVE_DOWN)
                    else:
                        directions.append(Movement.MOVE_UP)
                    if self.x < self.target.x:
                        directions.append(Movement.MOVE_RIGHT)
                        directions.append(Movement.MOVE_LEFT)
                    else:
                        directions.append(Movement.MOVE_LEFT)
                        directions.append(Movement.MOVE_RIGHT)

                else:
                    if self.x < self.target.x:
                        directions.append(Movement.MOVE_RIGHT)
                    else:
                        directions.append(Movement.MOVE_LEFT)
                    if self.y < self.target.y:
                        directions.append(Movement.MOVE_DOWN)
                        directions.append(Movement.MOVE_UP)
                    else:
                        directions.append(Movement.MOVE_UP)
                        directions.append(Movement.MOVE_DOWN)

            # Now the directions list has been sorted
            for direction in directions:
                if super(Enemy, self).move(direction):
                    return
            return

        def takeDamage(self, attacker, damage):
            self.hp -= damage
            if self.turnsHuntingTarget > 2:
                self.target = attacker
            if self.hp <= 0:
                self.die()

    return Enemy()
