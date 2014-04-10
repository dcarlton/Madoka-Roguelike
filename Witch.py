import random
from Familiar import Familiar
from Enemy import Enemy
from Enumerations import *
from Constants import *
from Map import Map
from TurnManager import TurnManager

board = Map.getInstance()
turnManager = TurnManager.getInstance()

class Witch(Familiar):
	def spawnFamiliar(self, delay = True):
		if self.controller:
			if (self.controller).hp <= 0:
				return
		familiar = Enemy(Familiar())
		while (True):
			x = random.randint(0, MAP_WIDTH - 1)
			y = random.randint(0, MAP_HEIGHT - 1)
			if board.grid[x][y].addBeing(familiar):
				familiar.x = x
				familiar.y = y
				break
		if delay:
			turnManager.delayFunction(self.spawnFamiliar, 10)
			
	def __init__(self):
		self.hp = 75
		self.strength = 20
		self.character = 'W'
		self.beingType = BeingType.WITCH
		self.block = BlockStatus.BLOCK_ALL
		self.controller = 0
		self.spawnFamiliar(False)
		self.spawnFamiliar()
