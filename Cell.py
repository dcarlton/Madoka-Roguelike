import libtcodpy as libtcod
from Enumerations import *

class Cell:
	def __init__(self, x, y):
		self.beings = []
		self.block = BlockStatus.BLOCK_NONE
		self.x = x
		self.y = y
		
	def draw(self, console):
		libtcod.console_set_char_background(console, self.x, self.y, libtcod.white)
		if len(self.beings) == 0:
			libtcod.console_put_char(console, self.x, self.y, ' ')
			return
		libtcod.console_put_char(console, self.x, self.y, (self.beings[-1]).character)
		
	def addBeing(self, being):
		if self.canMove(being):
			(self.beings).append(being)
			if being.block < self.block:
				# If the new being is more restrictive 
				# e.g. Magical girl moving into a human's space
				# Then update the new status
				self.block = being.block
			return True
		return False
		
	def removeBeing(self, being):
		(self.beings).remove(being)
		if being.block <= self.block:
			self.checkBlockStatus()
			return True
		return False
		
	def canMove(self, being):
		# Temporary, should use the BlockStatus to determine if it can move there
		if len(self.beings) == 0:
			return True
		return False
		
	def checkBlockStatus(self):
		# Calling this function means that the cell does not know
		# What should and shouldn't be kept out of the cell
		block = BlockStatus.BLOCK_NONE
		if len(self.beings) == 0:
			return
		
		for being in self.beings:
			if being.block < self.block:
				self.block = being.block
