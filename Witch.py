import pygame
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
				familiar.rect.x = x * 16
				familiar.y = y
				familiar.rect.y = y * 16
				break
		if delay:
			turnManager.delayFunction(self.spawnFamiliar, 10)
			
	def __init__(self):
		self.hp = 75
		self.strength = 20
		self.image = pygame.image.load("WitchStanding.png").convert()
		self.rect = self.image.get_rect()
		self.beingType = BeingType.WITCH
		self.block = BlockStatus.BLOCK_ALL
		self.controller = 0
		self.spawnFamiliar(False)
		self.spawnFamiliar()
