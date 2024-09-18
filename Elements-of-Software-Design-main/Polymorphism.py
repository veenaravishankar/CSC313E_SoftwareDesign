class Plant:
	def display(self):
		print("I'm a plant")
class Mint(Plant):
	def display(self):
		print("I'm a mint")
class Lavender(Mint):
	def display(self):
		print("I'm a lavender")

mint_1 = Mint()
mint_1.display()
lavender_1 = Lavender()
lavender_1.display()