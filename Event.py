import pygame
from Enumerations import EventType

class Event():
    @classmethod
    def diedEvent(self, type):
        event = pygame.event.Event(EventType.DIED, {'beingType' : type})
        pygame.event.post(event)

    @classmethod
    def winEvent(self):
        event = pygame.event.Event(EventType.WIN)
        pygame.event.post(event)

    @classmethod
    def lossEvent(self):
        event = pygame.event.Event(EventType.LOSS)
        pygame.event.post(event)
