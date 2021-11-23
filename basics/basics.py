#print("Hello World!")

# Single line comments start with a hashtag

""" Multiline comments
    are often useful as 
    well
"""


#################################################
## Operators and Precedence
#################################################

(1 + 2)  # Paranthesis (1)
4 ** 5   # Exponentiation (1)
22 % 8   # Modulus (remainder) (2)
10 * 2   # Multiplication (2)
35 / 5   # Division (2)
35 // 5  # Integer division (2)
1 + 1    # Addition (3)
8 - 1    # Sutraction (3)

#print(6 * 5 // 6 % 4)


# Equality operator ( == ) 

# It returns (output) a boolean value
print(2 == 3) # -> False
print(4 == 4) # -> True

# != (inequality operator)
print(2 != 3 ) # -> True


# Logical operators (and, or)

# and -> this returns (output) a boolean value as well
# True and True -> True
# True and False -> False
# False and False -> False

# or
# True or False -> True
# True or True -> True
# False or False -> False

print(1 and 0) # -> False
print(1 and 2) # -> True
# Any integer except zero is truthy, 1 is perfect True and every other number is truish



# Assignment operator and Variables
# A variable is a container (bucket) in the memory of the computer
# It is a location in the memory where data of similar is kept stored
variableA = 5
floatingVariable = 6.3
stringVariable = "This is a string"
AnotherStringVar = 'This is another string'
myName = "Raman"

# String concatenation
# Adds two strings
print("My name is " + myName) # -> "My name is Raman"

# String multiplication
print(myName * 5) # -> "RamanRamanRamanRamanRaman"

# Formatted Strings
print(f"My name is {myName} and I am {14 + 5} years old") # -> "My name is Raman and I am 19 years old"



#################################################
## Data Types
#################################################

# Integers (int)
1, 2, 3, -5, -9
# Floating point numbers (float)
floatVar = 5.7
# Boolean true or false

# Strings
# String is a sequence of characters
"This"
# String is implemented as a list of characters
0, 'T'; 1, 'h'; 2, 'i'; 3, 's'

# Accessing characters of a string
myName = "Raman"
secondLetter = myName[1]
print(secondLetter) # -> "a"

# len() function
# function is a block of code which performs a specific task
# len function returns/outputs the length or the number of characters in a string

lenOfMyName = len(myName)
print(lenOfMyName) # -> 5

thisInteger = 5
# String in short are called str (read as "stirs")
thisString = str(thisInteger) # -> "5"


# Updating Variables
a = 5
a = 82
a = "This"
# Python is a dynamically typed language
# This means that variables can be assigned different data types
# In static typed languages (c++, java) you cannot change the data type 
# of the variable.

a = 2 * 5 + (4 - 9)
#print(a)

a = a + 5
#print(a)
a = a - 10
#print(a)
a = a * 9
#print(a)


# Varaible naming convention
# Cannot start with a number
# Cannot contain any special character (like $)
# Cannot contain hyphen (-)
# We can use undercscore (_)
# Cannot use reserved words

# variable_name = 56

# Camel Case
# variableName = 56


# int() function

b = int(5.74)
# Rounds it down to nearest integer
print(b) # -> 5

b = int("392")
print(b) # -> 392

#b = int("85ghd") # Cannot do this


# float()

b = float(42)
print(b) # -> 42.0

b = float("73.15")
print(b) # -> 73.15

# input() -> If we have to take input from the user, then we use this function
# A program to take input the users name and print the number of letters in it

myAge = input("Enter your age")
# input function always returns a string
myAge = int(myAge)
print(type(myAge))
