from Character import Character
import libtcodpy as libtcod
import sys
import random
from Constants import *
from Enumerations import *
from Map import Map

board = Map.getInstance()

class Enemy(Character):
	def __init__(self, being):
		self.hp = being.hp
		self.x = int(MAP_WIDTH / 2)
		self.y = int(MAP_HEIGHT / 2)
		self.strength = being.strength
		self.block = BlockStatus.BLOCK_ALL
		self.character = being.character
		self.being = being
		self.beingType = being.beingType
		self.being.controller = self
		
	def takeTurn(self):
		# For now, just move in a random direction unless the player is nearby
		if self.attack():
			return
		direction = random.choice([Movement.MOVE_UP, Movement.MOVE_DOWN, Movement.MOVE_LEFT, Movement.MOVE_RIGHT])
		self.move(direction)

	def attack(self):
		# For now, attack anything above, then right, then below, then left
		if self.y > 0 and len((board.grid[self.x][self.y-1]).beings) > 0:
			count = -1
			for being in (board.grid[self.x][self.y-1]).beings:
				if ((board.grid[self.x][self.y-1]).beings[count]).__class__.__name__ == "Enemy":
					continue
				((board.grid[self.x][self.y-1]).beings[count]).hp -= self.strength
				
				if ((board.grid[self.x][self.y-1]).beings[count]).hp <= 0:
					((board.grid[self.x][self.y-1]).beings[count]).die()
				return True
			
			# There is an enemy in that space, but no targets to attack
			return False
		elif self.x < (MAP_WIDTH - 1) and len((board.grid[self.x+1][self.y]).beings) > 0:
			count = -1
			for being in (board.grid[self.x+1][self.y]).beings:
				if ((board.grid[self.x+1][self.y]).beings[count]).__class__.__name__ == "Enemy":
					continue
			
				((board.grid[self.x+1][self.y]).beings[count]).hp -= self.strength
				if ((board.grid[self.x+1][self.y]).beings[count]).hp <= 0:
					((board.grid[self.x+1][self.y]).beings[count]).die()
				return True
				
			return False
		elif self.y < (MAP_HEIGHT - 1) and len((board.grid[self.x][self.y+1]).beings) > 0:
			count = -1
			for being in (board.grid[self.x][self.y+1]).beings:
				if ((board.grid[self.x][self.y+1]).beings[count]).__class__.__name__ == "Enemy":
					continue
				((board.grid[self.x][self.y+1]).beings[count]).hp -= self.strength
				if ((board.grid[self.x][self.y+1]).beings[count]).hp <= 0:
					((board.grid[self.x][self.y+1]).beings[count]).die()
				return True
			return False
		elif self.x > 0 and len((board.grid[self.x-1][self.y]).beings) > 0:
			count = -1
			for being in (board.grid[self.x-1][self.y]).beings:
				if ((board.grid[self.x-1][self.y]).beings[count]).__class__.__name__ == "Enemy":
					continue
				((board.grid[self.x-1][self.y]).beings[count]).hp -= self.strength
				if ((board.grid[self.x-1][self.y]).beings[count]).hp <= 0:
					((board.grid[self.x-1][self.y]).beings[count]).die()
				return True
			return False
			
		# There are no other characters surrounding the enemy
		return False

	def die(self):
		if self.hp <= 0:
			if self.beingType == BeingType.WALPURGISNACHT:
				libtcod.console_clear(0)
				libtcod.console_print(0, 0, int(MAP_HEIGHT / 2), "You win!")
				libtcod.console_flush()
				while (True):
					key = libtcod.Key()
					mouse = libtcod.Mouse()
					libtcod.sys_wait_for_event(libtcod.EVENT_KEY_PRESS, key, mouse, True)
					if key.vk == libtcod.KEY_ESCAPE:
						sys.exit(0)
			(board.grid[self.x][self.y]).removeBeing(self)
			self.x = -1
			self.y = -1
