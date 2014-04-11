import sys
from Constants import *
from Enumerations import *
from Map import Map

board = Map.getInstance()

class Character:
	def __init__(self):
		# All values are set to the default for an unknown character
		self.hp = 100
		self.block = BLOCK_ALL
		self.x = 0
		self.y = 0
		self.character = '?'
		
	def __eq__(self, other):
		# Works as long as two characters of the same type
		# Cannot stand in the same space
		if self.beingType == other.beingType and self.x == other.x and self.y == other.y:
			return True
		return False

	def move(self, direction):
		if direction == Movement.MOVE_DOWN and self.y > -1 and self.y < (MAP_HEIGHT - 1):
			if (board.grid[self.x][self.y+1]).canMove(self):
				(board.grid[self.x][self.y]).removeBeing(self)
				self.y += 1
				(board.grid[self.x][self.y]).addBeing(self)
				self.rect.move(0, 16)
				return True
			return False
		elif direction == Movement.MOVE_UP and self.y > 0 and self.y < MAP_HEIGHT:
			if (board.grid[self.x][self.y-1]).canMove(self):
				(board.grid[self.x][self.y]).removeBeing(self)
				self.y -= 1
				(board.grid[self.x][self.y]).addBeing(self)
				self.rect.move(0, -16)
				return True
			return False
		elif direction == Movement.MOVE_LEFT and self.x > 0 and self.x < MAP_WIDTH:
			if (board.grid[self.x-1][self.y]).canMove(self):
				(board.grid[self.x][self.y]).removeBeing(self)
				self.x -= 1
				(board.grid[self.x][self.y]).addBeing(self)
				self.rect.move(-16, 0)
				return True
			return False
		elif direction == Movement.MOVE_RIGHT and self.x > -1 and self.x < (MAP_WIDTH - 1):
			if (board.grid[self.x+1][self.y]).canMove(self):
				(board.grid[self.x][self.y]).removeBeing(self)
				self.x += 1
				(board.grid[self.x][self.y]).addBeing(self)
				self.rect.move(16, 0)
				return True
			return False
		return False

	def die(self):
		if self.hp <= 0:
			(board.grid[self.x][self.y]).removeBeing(self)
			self.x = -1
			self.y = -1

	def abilityOne(self, x, y):
		# Let the Magical Girl's return value decide if the space is valid or not
		# Unrelated note, need to rename Being to Character, and Character to...something
		# Maybe
		return (self.being).abilityOne(x, y)
