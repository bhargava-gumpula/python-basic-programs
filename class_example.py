class Things:
	pass

class Inanimate(Things):
	pass

class Sidewalk(Inanimate):
	pass

class Animate(Things):
	pass

class Animals(Animate):
	def breathe(self):
		print("breathing")
	def move(self):
		print('moving')
	def eat_food(self):
		print("eating food")

class Mammals(Animals):
	def feed_young_with_milk(self):
		print("feeding young")

class Giraffes(Mammals):
	def eat_leaves_from_trees(self):
		print("eating leaves")


reginald = Giraffes()
reginald.move()
reginald.eat_leaves_from_trees()

harold = Giraffes()
harold.move()
