import random
#game of sticks using probability basic idea of AI


class Player():
	def __init__(self, sticks):
		self.array = None
		self.name = None
		self.sticks = sticks
	def pickSticks(self, pick):
		self.sticks -= pick

class Ai(Player):
	def __init__(self, sticks):
		super(Ai, self).__init__(sticks)
		self.name = ' '.join([chr(random.randrange(100)) for x in range(4)])
		self.array = [0] * sticks


class GameofSticks():
	def __init__(self):
		self.numSticks = 20
		self.name = input(str("Enter in your name: "))
		print("Hello", self.name)
		self.welcome()
		self.chooseOption()

	def welcome(self):
		chose = "Rules: pick between 1-3 sticks, the player pick last stick loses the game\n"
		chose1 = "1. Choose simple player vs player\n2. Choose to train Ai and play against Ai\n3. Exit the game\n"
		while True:
			try:
				self.option = int(input(chose+chose1))
				if(self.option > 3 or self.option < 1):
					continue
				break
			except ValueError as e:
				print("please enter valid int..")
	def chooseOption(self):
		if self.option == 1:
			self.pvp()
		elif self.option == 2:
			self.train()
		else:
			exit()
	def winner(self, players):
		pass

	def pvp(self):
		player1 = Player(self.numSticks)
		player2 = Player(self.numSticks)
		player1.name = str(input("what is player 1 name? "))
		player2.name = str(input("what is player 2 name? "))
		players = [player1, player2]
		players = random.shuffle(players)
		print(players[0].name + "is going first")





if __name__ == "__main__":
	newgame = GameofSticks()
