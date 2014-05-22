from Enumerations import BlockStatus

class Being(object):
    def __init__(self):
        self.maxHP = 100
        self.hp = self.maxHP

        self.image = None
        self.rect = None

        self.beingType = None
        self.block = BlockStatus.BLOCK_ALL
        self.status = []
        self.vision = 3
        self.x = 0
        self.y = 0