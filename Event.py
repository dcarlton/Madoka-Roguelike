import pygame
from Enumerations import EventType

class Event():
    @classmethod
    def winEvent(self):
        event = pygame.event.Event(EventType.WIN)
        pygame.event.post(event)

    @classmethod
    def lossEvent(self):
        event = pygame.event.Event(EventType.LOSS)
        pygame.event.post(event)
