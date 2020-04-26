class Person:
	def __init__(self, height, mass, first_name, last_name):
		self.height = height
		self.mass = mass
		self.first_name = first_name
		self.last_name = last_name
		
	def full_name(self):
		return (self.first_name + self.last_name)

	def bmi(self):
		return (self.mass / (self.height)**2)


me = Person("1.76", "74", "Aidan", "Wisnia")

print(me.height)
