class Four_Wheeler:
	def print(self):
		print("Hello")
	wheels = 4

class Car(Four_Wheeler):
	def __init__(self, brand, color, price, numSeats):
		self.brand = brand
		self.color = color
		self.price = price
		self.numSeats = numSeats

	def set_price(self, price):
		self.price = price
	
	def set_color(self, color):
		self.color = color

	def __str__(self):
		return "Brand : %s\nColor : %s\nPrice : %s\nSeats : %s\nWheels : %s\n" % (self.brand,self.color,self.price,self.numSeats,self.wheels)


Egod = Car("Tesla", "Red", 80000, 5)
Egod.set_color("Blue")

Toyota = Car("Toyota", "Red", 15000, 5)
print(Egod)
print("\n")
print(Toyota)

Egod.print()
