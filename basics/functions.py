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

def add(num1, num2):
	return 0 # return is kind of a break statement of functions
	sum_var = num1 + num2
	print(sum_var)
	return sum_var

return_value = add(4, 8)
print(return_value)

def modulo(num1, num2):
	print(num1 % num2)


modulo(4, 5)

# To store the argument we pass in the function call, there should be 
# a corresponding variable to store the argument

# Function is used to reduce repetion of code

#print("hello world") # i am calling the print function

# return values and return statement

# When a function ends, it always returns a value
# to return a value we can use the return statement
# If we do not use the return statement then default value is None
# None value


# Call Stack
# Local and global scope