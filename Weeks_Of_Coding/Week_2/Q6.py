# Ques 6. Write a python program to create multiple instances of a class.

class person:
	
	def __init__(self, name):
		self.name = name

	def introduce(self):
		print("Hello My Name is ",self.name)

a = person("Prakhar")
b = person("Prakhar II")
c = person("Prakhar III")
d = person("Prakhar IV")

a.introduce()
b.introduce()
c.introduce()
d.introduce()