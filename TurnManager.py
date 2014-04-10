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
		
	def delayFunction(self, function, delay):
		if (self.toBeCalled).has_key(self.turnCount + delay):
			self.toBeCalled[(self.turnCount + delay)].append(function)
		else:
			self.toBeCalled[self.turnCount + delay] = [function]
			
	def removeDelayedFunction(self, function, delay):
		for turn in range(self.turnCount, self.turnCount + delay):
			if (self.toBeCalled).has_key(turn):
				result = self.toBeCalled[turn].remove(function)
				if result:
					return True
		return False

	def callDelayedFunctions(self):
		if self.toBeCalled.has_key(self.turnCount):
			for function in self.toBeCalled[self.turnCount]:
				function()
