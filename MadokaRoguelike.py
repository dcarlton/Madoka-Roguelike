import libtcodpy as libtcod
import random
import sys
from PlayState import PlayState
from Player import Player
from Enemy import Enemy
from Mami import Mami
from Witch import Witch
from Walpurgisnacht import Walpurgisnacht
from Familiar import Familiar
from Map import Map
from TurnManager import TurnManager
from Constants import *
from Enumerations import *


libtcod.console_set_custom_font('arial24x24.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(MAP_WIDTH, MAP_HEIGHT, 'Madoka Roguelike', False)

player = Player(Mami())
player.x = 4
player.y = 4
witches = [Enemy(Witch())]

board = Map.getInstance()
(board.grid[4][4]).addBeing(player)
for witch in witches:	
	while (True):
		x = random.randint(0, MAP_WIDTH - 1)
		y = random.randint(0, MAP_HEIGHT - 1)
		if board.grid[x][y].addBeing(witch):
			witch.x = x
			witch.y = y
			break
			
turnManager = TurnManager.getInstance()
			
def npcTurn():
	beings = []
	for column in board.grid:
		for cell in column:
			for being in cell.beings:
				if being.__class__.__name__ != "Player":
					beings.append(being)
	for being in beings:
		being.takeTurn()
			
def addWitch():
	witch = Enemy(Witch())
	while (True):
		x = random.randint(0, MAP_WIDTH - 1)
		y = random.randint(0, MAP_HEIGHT - 1)
		if board.grid[x][y].addBeing(witch):
			witch.x = x
			witch.y = y
			break
	witches.append(witch)
	turnManager.delayFunction(addWitch, 25)
	
def addWalpurgisnacht():
	walpurgisnacht = Enemy(Walpurgisnacht())
	while (True):
		x = random.randint(0, MAP_WIDTH - 1)
		y = random.randint(0, MAP_HEIGHT - 1)
		if board.grid[x][y].addBeing(walpurgisnacht):
			walpurgisnacht.x = x
			walpurgisnacht.y = y
			break
	witches.insert(0, walpurgisnacht)
		
def win():
	# Would be nice if there was a way to check if Walpurgisnaght had been slain
	libtcod.console_clear(0)
	libtcod.console_print(0, 0, int(MAP_HEIGHT / 2), "You win!")
	libtcod.console_flush()
	while (True):
		key = libtcod.Key()
		mouse = libtcod.Mouse()
		libtcod.sys_wait_for_event(libtcod.EVENT_KEY_PRESS, key, mouse, True)
		if key.vk == libtcod.KEY_ESCAPE:
			sys.exit(0)
			
def loss():
	if player.hp <= 0 or player.magic <= 0:
		result = "Game over"
	else:
		return False
	libtcod.console_clear(0)
	libtcod.console_print(0, 0, int(MAP_HEIGHT / 2), result)
	libtcod.console_flush()
	while (True):
		key = libtcod.Key()
		mouse = libtcod.Mouse()
		libtcod.sys_wait_for_event(libtcod.EVENT_KEY_PRESS, key, mouse, True)
		if key.vk == libtcod.KEY_ESCAPE:
			sys.exit(0)

turnManager.delayFunction(addWitch, 25)
turnManager.delayFunction(addWalpurgisnacht, 50)

while not libtcod.console_is_window_closed():
	board.draw()
	while (not player.takeTurn()):
		pass
	npcTurn()
	if player.hp <= 0 or player.magic <= 0:
		loss()
	turnManager.turnCount += 1
	turnManager.callDelayedFunctions()
	print("HP: " + str(player.hp))
	print("Magic: " + str(player.magic))
	print("Score: " + str(player.score))
