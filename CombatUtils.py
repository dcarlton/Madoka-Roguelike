from Enumerations import Victims

targets = dict()
targets[Victims.ALL] = ["Player", "Ally", "Human", "Enemy"]
targets[Victims.NON_PLAYER_AND_HUMAN] = ["Ally", "Enemy"]
targets[Victims.NON_PLAYER] = ["Ally", "Human", "Enemy"]
targets[Victims.NON_ENEMY] = ["Player", "Ally", "Human"]
targets[Victims.EVERYTHING] = ["Player", "Ally", "Human", "Enemy", ""]
targets[Victims.NONE] = [""]


class CombatUtils():
    @classmethod
    def canTarget(cls, character, victims):
        if character is None:
            for target in targets[victims]:
                if target == "":
                    return True
        else:
            for target in targets[victims]:
                if character.__class__.__name__ == target:
                    return True
        return False

    @classmethod
    def distance(cls, x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)
