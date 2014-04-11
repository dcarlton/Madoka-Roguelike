import pygame
from Enumerations import *
from Constants import *
from Map import Map
from MagicalGirl import MagicalGirl

MUSKET_SLAM_DAMAGE = 10
MUSKET_SLAM_MAGIC = 5

board = Map.getInstance()

class Mami(MagicalGirl):
	def __init__(self):
		self.hp = 100000
		self.magic = 100
		self.regenerationRate = 5
		self.image = pygame.image.load("MamiStanding.png").convert()
		self.rect = self.image.get_rect()
		self.controller = 0
		self.beingType = BeingType.MAGICAL_GIRL
		
	def abilityOne(self, x, y):
		if not (-1 < x and x < MAP_WIDTH and -1 < y and y < MAP_HEIGHT):
			return 0
		if len((board.grid[x][y]).beings) > 0:
			((board.grid[x][y]).beings[-1]).hp -= MUSKET_SLAM_DAMAGE
			if ((board.grid[x][y]).beings[-1]).hp <= 0:
				if self.controller:
					dead = (board.grid[x][y]).beings[-1]
					if dead.beingType == BeingType.FAMILIAR:
						(self.controller).killedFamiliar()
					elif dead.beingType == BeingType.WITCH:
						(self.controller).killedWitch()
				((board.grid[x][y]).beings[-1]).die()
			return MUSKET_SLAM_MAGIC
		return 0
