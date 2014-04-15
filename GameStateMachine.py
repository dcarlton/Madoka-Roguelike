import pygame
from Enumerations import EventType
from Event import Event
from PlayState import PlayState

class GameStateMachine():
    def __init__(self):
        self.playState = PlayState()

        self.previousState = False
        self.currentState = self.playState

    def run(self):
        # Add mouse support after the initial prototype is finished
        pygame.event.set_blocked(pygame.MOUSEMOTION)
        pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
        pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
        pygame.event.set_blocked(pygame.KEYUP)
        while True:
            self.currentState.draw()
            event = pygame.event.wait()
            self.currentState.eventHandle(event)
