import pygame
import random
from Cell import Cell
from Constants import *
from Enumerations import *

class Map:
    instance = None
    grid = []

    def __init__(self):
        # Nothing happens, don't create the value
        # Map is implemented as a Singleton
        return

    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = Map()
            (cls.instance).construct()
        return cls.instance

    def construct(self):
        for x in range(0, MAP_WIDTH):
            (self.grid).append([])
            for y in range(0, MAP_HEIGHT):
                (self.grid[x]).append(Cell(x, y))

    def addCharacter(self, character):
        while True:
            x = random.randint(0, MAP_WIDTH - 1)
            y = random.randint(0, MAP_HEIGHT - 1)
            if self.grid[x][y].addBeing(character):
                character.x = x
                character.y = y
                return
