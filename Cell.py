import pygame
from Enumerations import *

class Cell:
    def __init__(self, x, y):
        self.barrier = False
        self.beings = []
        self.block = BlockStatus.BLOCK_NONE
        self.x = x
        self.y = y

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
        if len(self.beings) == 0 and self.barrier is False:
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
