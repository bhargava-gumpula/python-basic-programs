import random

class Employee:
	def __init__(self, name, age, position):
		self.name = name
		self.age = age
		self.position = position
		self.id = None

	def set_name(self, name):
		self.name = name
	def set_age(self, age):
		self.age = age
		self.show()
	def set_position(self, position):
		self.position = position	
	def generate_ID(self):
		alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
		nums = [1,2,3,4,5,6,7,8,9]
		self.id = " "
		self.id  = self.id + str(random.choice(nums))
		for x in range(0,3):
			rand_letter = random.choice(alphabet)
			self.id = self.id + rand_letter.upper()
		for x in range(0,3):
			rand_int = str(random.choice(nums))
			self.id = self.id + rand_int	
	def __str__(self):
        	return self.name + " " + str(self.age) + " " + str(self.id)
manager = Employee("foo", 30, "Manager")
director = Employee("bar", 50, "Director")

manager.generate_ID()
director.generate_ID()
print(manager)
print(director)

