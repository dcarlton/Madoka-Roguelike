import pygame
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
				
	def draw(self):
		screen = pygame.display.get_surface()
		screen.fill((255, 255, 255))
		for column in self.grid:
			for cell in column:
				cell.draw()
		pygame.display.flip()
