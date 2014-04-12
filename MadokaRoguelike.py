import pygame
from GameStateMachine import GameStateMachine

pygame.init()
screen = pygame.display.set_mode((144, 144))
GameStateMachine().run()
