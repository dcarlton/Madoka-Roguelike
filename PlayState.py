import pygame
import sys
from Enemy import makeEnemy
from Enumerations import *
from Event import Event
from Familiar import Familiar
from Graphics import Graphics
from Homura import Homura
from Kyoko import Kyoko
from Mami import Mami
from Map import Map
from Mixer import Mixer
from Player import makePlayer
from Sayaka import Sayaka
from State import State
from TurnManager import TurnManager
from Walpurgisnacht import Walpurgisnacht
from Witch import Witch

board = Map.getInstance()
mixer = Mixer.getInstance()
turnManager = TurnManager.getInstance()

class PlayState(State):
    def addFamiliar(self):
        familiar = makeEnemy(Familiar)
        board.addCharacter(familiar)
        self.familiars.append(familiar)

    def addWitch(self):
        witch = makeEnemy(Witch)
        board.addCharacter(witch)
        self.witches.append(witch)

        for i in range(0, 2):
            self.addFamiliar()
        turnManager.delayFunction(self.addWitch, 25)

    def addWalpurgisnacht(self):
        self.walpurgisnacht = makeEnemy(Walpurgisnacht)
        board.addCharacter(self.walpurgisnacht)
        for i in range(0, 4):
            self.addFamiliar()

    def __init__(self):
        self.player = makePlayer(Kyoko)
        board.addCharacter(self.player)

        self.familiars = []
        self.witches = []
        self.walpurgisnacht = False
        self.addWitch()
        self.addWitch()
        turnManager.delayFunction(self.addWalpurgisnacht, 100)

        mixer.playSong("Magia.wav")

    def eventHandle(self, event):
        if event == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            sys.exit(0)
        elif event.type == EventType.WIN:
            print("You win!")
            pygame.event.wait()
            sys.exit(0)
        elif event.type == EventType.LOSS:
            print("Game over")
            pygame.event.wait()
            sys.exit(0)
        if self.player.takeTurn(event):
            self.npcTurn()
            turnManager.endTurn()
        print("HP: " + str(self.player.hp))
        print("Magic: " + str(self.player.magic))
        print("Score: " + str(self.player.score))

    def draw(self):
        Graphics.getInstance().drawPlayState(self.player)

    def npcTurn(self):
        if self.walpurgisnacht:
                self.walpurgisnacht.takeTurn()
        for witch in self.witches:
            witch.takeTurn()
        for familiar in self.familiars:
            familiar.takeTurn()
