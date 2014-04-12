import pygame
import random
from Familiar import Familiar
from Enemy import Enemy
from Enumerations import *
from Constants import *
from Graphics import Graphics
from Map import Map
from TurnManager import TurnManager

board = Map.getInstance()
turnManager = TurnManager.getInstance()

class Witch(Familiar):
    def __init__(self):
        self.hp = 75
        self.strength = 20
        self.image = Graphics.getInstance().getImage(Images.WITCH_STANDING)
        self.rect = self.image.get_rect()
        self.beingType = BeingType.WITCH
        self.block = BlockStatus.BLOCK_ALL
        self.controller = 0
