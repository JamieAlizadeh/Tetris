class Tile:
	def __init__(self, name="", shape=list()):
		self.name = name
		self.shape = shape
	def spinRight(self):
		newArr = self.shape[:]
		for x in range (1, 17):
			if (x == 1 or x == 2 or x == 3 or x == 4):
				self.shape[x] = newArr[-4*x+17]
			if (x == 5 or x == 6 or x == 7 or x == 8):
				self.shape[x] = newArr[-4*x+34]
			if (x == 9 or x == 10 or x == 11 or x == 12):
				self.shape[x] = newArr[-4*x+51]
			if (x == 13 or x == 14 or x == 15 or x == 16):
				self.shape[x] = newArr[-4*x+68]
	def spinLeft(self):
		newArr = self.shape[:]
		for x in range (1, 17):
			if (x == 1 or x == 2 or x == 3 or x == 4):
				self.shape[-4*x+17] = newArr[x]
			if (x == 5 or x == 6 or x == 7 or x == 8):
				self.shape[-4*x+34] = newArr[x]
			if (x == 9 or x == 10 or x == 11 or x == 12):
				self.shape[-4*x+51] = newArr[x]
			if (x == 13 or x == 14 or x == 15 or x == 16):
				self.shape[-4*x+68] = newArr[x]


tileOne = Tile("O", [None, False, False, True, True, False, False, True,
						 True, False, False, False, False, False, False, False, False])
tileTwo = Tile("I", [None, False, False, True, False, False, False, True,
						False, False, False, True, False, False, False, True, False])
tileThree = Tile("T", [None, False, True, True, True, False, False, True,
						False, False, False, False, False, False, False, False, False])
tileFour = Tile("J", [None, False, True, True, True, False, False, False,
						  True, False, False, False, False, False, False, False, False])
tileFive = Tile("L", [None, False, True, True, True, False, True, False,
						  False, False, False, False, False, False, False, False, False])
tileSix = Tile("S", [None, False, False, True, True, False, True, True,
						  False, False, False, False, False, False, False, False, False])
tileSeven = Tile("Z" , [None, False, True, True, False, False, False, True,
						  True, False, False, False, False, False, False, False, False])
