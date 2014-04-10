from Character import Character
import libtcodpy as libtcod
import sys
from Constants import *
from Enumerations import *
from Map import Map
from TurnManager import TurnManager

board = Map.getInstance()
turnManager = TurnManager.getInstance()

class Player(Character):
	def __init__(self, being):
		self.maxHP = being.hp
		self.hp = being.hp
		self.magic = being.magic
		self.regenerationRate = being.regenerationRate
		self.block = BlockStatus.BLOCK_ALL
		self.x = int(MAP_WIDTH / 2)
		self.y = int(MAP_HEIGHT / 2)
		self.character = being.character
		self.being = being
		self.beingType = being.beingType
		self.being.controller = self
		self.score = 0
		turnManager.delayFunction(self.regenerate, self.regenerationRate)
	
	def takeTurn(self):
		key = libtcod.Key()
		mouse = libtcod.Mouse()
		libtcod.sys_wait_for_event(libtcod.EVENT_KEY_PRESS, key, mouse, True)
	
		if key.vk == libtcod.KEY_ENTER and key.lalt:
			libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
		elif key.vk == libtcod.KEY_ESCAPE:
			sys.exit(0)
			
		magicLoss = 0
		if libtcod.console_is_key_pressed(libtcod.KEY_UP):
			magicLoss = self.being.abilityOne(self.x, self.y-1)
			if magicLoss != 0:
				self.magic -= magicLoss
				return True
			return self.move(Movement.MOVE_UP)
		elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
			magicLoss = self.being.abilityOne(self.x, self.y+1)
			if magicLoss != 0:
				self.magic -= magicLoss
				return True
			return self.move(Movement.MOVE_DOWN)
		elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
			magicLoss = self.being.abilityOne(self.x-1, self.y)
			if magicLoss != 0:
				self.magic -= magicLoss
				return True
			return self.move(Movement.MOVE_LEFT)
		elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
			magicLoss = self.being.abilityOne(self.x+1, self.y)
			if magicLoss != 0:
				self.magic -= magicLoss
				return True
			return self.move(Movement.MOVE_RIGHT)
		return False
		
	def killedFamiliar(self):
		self.score += 100
		
	def killedWitch(self):
		self.score += 100
		self.magic += 200

	def regenerate(self):
		if self.hp < self.maxHP:
			self.hp += 1
		turnManager.delayFunction(self.regenerate, self.regenerationRate)
