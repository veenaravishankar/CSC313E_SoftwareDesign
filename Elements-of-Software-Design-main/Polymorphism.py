class Plant:
	def display(self):
		print("I'm a plant")
class Mint(Plant):
	def display(self):
		print("I'm a mint")
class Lavender(Mint):
	def display(self):
		print("I'm a lavender")

leaf = Mint()
leaf.display()
leaf = Lavender()
leaf.display()
