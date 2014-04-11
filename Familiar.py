import pygame
from Being import Being
from Enumerations import *

class Familiar(Being):
	def __init__(self):
		self.hp = 25
		self.strength = 10
		self.image = pygame.image.load("FamiliarStanding.png").convert()
		self.rect = self.image.get_rect()
		self.beingType = BeingType.FAMILIAR
		self.block = BlockStatus.BLOCK_ALL
		self.controller = 0
