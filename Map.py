import libtcodpy as libtcod
from Cell import Cell
from Constants import *
from Enumerations import *

gameScreen = libtcod.console_new(MAP_WIDTH, MAP_HEIGHT)
libtcod.console_set_default_background(gameScreen, libtcod.white)
libtcod.console_set_default_foreground(gameScreen, libtcod.black)

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
		for column in self.grid:
			for cell in column:
				cell.draw(gameScreen)
		libtcod.console_blit(gameScreen, 0, 0, MAP_WIDTH, MAP_HEIGHT, 0, 0, 0)
		libtcod.console_flush()
