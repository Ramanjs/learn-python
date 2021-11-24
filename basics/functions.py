# Functions

# range(), input(), print(), len(), str(), int(), float() are functions
# Function is like a mini-program inside a program
# Each function is a block of code that performs a specific task

# Arguments
# Arguments are the values which we pass to the function
# print("Hello world") # hello world is the argument

# Python has some pre written functions which we can use
# We can also write some functions to our need

# first of all we define the function
def myFunction(myVariable): # Parameter
	# funciton body/ block
	print("Hello, " + myVariable)
# ended the function

# a function runs when it is called
myFunction("Raman") # calling the function
myFunction("Rishi") # calling the function with different argument

# To store the argument we pass in the function call, there should be 
# a corresponding variable (parameter) to store the argument

def add(num1, num2):
	sum_var = num1 + num2
	# return is kind of a break statement of functions
	return sum_var


return_value = add(4, 8)
print(return_value) # -> 12

def modulo(num1, num2):
	print(num1 % num2)

modulo(4, 5)


def reverse_string(string_variable):
	n = len(string_variable) 
	index = n - 1
	reverse_result = ''
	while (index >= 0):
		reverse_result = reverse_result + string_variable[index] 
		index = index - 1
	return reverse_result


reverse1 = reverse_string("raman")
reverse2 = reverse_string("rishi")
reverse3 = reverse_string("parth")
print(reverse1) # -> "namar"
print(reverse2) # -> "ihsir"
print(reverse3) # -> "htrap"
# We can use the same function with different arguments to produce different results

# Function is used to reduce repetion of code

# return values and return statement
# When a function ends, it always returns a value
# to return a value we can use the return statement
# If we do not use the return statement then default value is None


# Local and global scope
# A variable defined inside a function has local scope. It means that it cannot be accessed outside that function
# A global variable can be accessed anywhere
myName = "raman" # myName is a global variable
def add(num1, num2):
	sum_var = num1 + num2 # sum_var is a local variable
	print(myName)
	return sum_var

result = add(2, 3)
# print(sum_var) # cannot access sum_var outside add function


# Modules
# We can import functions from other files
from module import divide # We need to tell python the file name from which we are importing
result = divide(5, 6)
print(result)

import random # random is a built-in module

random_integer = random.randint(1, 5)
print(random_integer)
