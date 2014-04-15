class TurnManager():
    instance = None

    def __init__(self):
        # Singleton
        return

    @classmethod
    def getInstance(cls):
        if cls.instance is None:
            cls.instance = TurnManager()
            (cls.instance).construct()
        return cls.instance

    def construct(self):
        self.toBeCalled = dict()
        self.turnCount = 1

    def callDelayedFunctions(self):
        if self.toBeCalled.has_key(self.turnCount):
            for function in self.toBeCalled[self.turnCount]:
                function()

    def delayFunction(self, function, delay):
        if (self.toBeCalled).has_key(self.turnCount + delay):
            self.toBeCalled[(self.turnCount + delay)].append(function)
        else:
            self.toBeCalled[self.turnCount + delay] = [function]

    def endTurn(self):
        self.turnCount += 1
        self.callDelayedFunctions()

    def removeDelayedFunction(self, function, delay=1000):
        for turn in range(self.turnCount, self.turnCount + delay):
            if (self.toBeCalled).has_key(turn):
                result = False
                # For some reason, lists throw an error if they try to remove an item they don't have <_<
                try:
                    result = self.toBeCalled[turn].remove(function)
                except:
                    pass
                if result:
                    return True
        return False
