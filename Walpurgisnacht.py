import pygame
import sys
from Witch import Witch
from Enumerations import *
from TurnManager import TurnManager
from Map import Map

board = Map.getInstance()
turnManager = TurnManager.getInstance()

class Walpurgisnacht(Witch):
	def __init__(self):
		self.hp = 150
		self.strength = 25
		self.image = pygame.image.load("WalpurgisnachtStanding.png").convert()
		self.rect = self.image.get_rect()
		self.beingType = BeingType.WALPURGISNACHT
		self.block = BlockStatus.BLOCK_ALL
		self.controller = 0
		for i in range(1, 4):
			self.spawnFamiliar(False)
		self.spawnFamiliar()
