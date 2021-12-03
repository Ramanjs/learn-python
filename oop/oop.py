# Object Oriented Programming
# Class -> group of similar kinds of things

# dog class, animal class, human class, furniture class

# Object -> member of a specific class

# class keyword
# Class definition
class dog:
	# Attributes or class variables
	# functions called methods
	name = 'rocky'
	breed = 'pug'

	def bark(self): # self refers to the object
		print('Bow bow')

	def eat(self):
		print("Chomp chomp")

	def hello(self, name):
		print("Hello " + name + " i am rocky")

# ended the class
# Object inherits all the properties from its class
dog_object = dog() #creating a dog object
# We access the properties using the dot operator
print(dog_object.name)
print(dog_object.breed)
dog_object.bark()
dog_object.eat()
dog_object.hello("Raman")


myList = [1, 2, 3, 4, 5]
# myList is an object of list class

# class list:
#    def append(item):
		# adds to the end of the list object

#	def insert()
