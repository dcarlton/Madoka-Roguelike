import pygame

class BlockStatus:
    # Lower number means the space is more restricted
    BLOCK_ALL = 1
    BLOCK_NON_PLAYABLE_CHARACTER = 2
    BLOCK_NON_MAGICAL_GIRL = 3
    BLOCK_NONE = 4

class Movement:
    MOVE_UP = 1
    MOVE_DOWN = 2
    MOVE_RIGHT = 3
    MOVE_LEFT = 4

class BeingType:
    MAGICAL_GIRL = 1
    FUTURE_MAGICAL_GIRL = 2
    BUNNYCAT = 3
    HUMAN = 4
    FAMILIAR = 5
    WITCH = 6
    WALPURGISNACHT = 7

class EventType:
    WIN = pygame.USEREVENT
    LOSS = pygame.USEREVENT + 1

class Sprites:
    MAMI_STANDING = 0
    HOMURA_STANDING = 1000
    FAMILIAR_STANDING = 6000
    WITCH_STANDING = 7000
    WALPURGISNACHT_STANDING = 8000
    TARGET_CURSOR = 9000

class Status:
    STUN = 1

class Victims:
    ALL = 1
    NON_PLAYER_AND_HUMAN = 2
    NON_ENEMY = 3
    NON_PLAYER = 4
    NONE = 5
    EVERYTHING = 6
