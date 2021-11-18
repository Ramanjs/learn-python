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
# TODO


# ==

# It returns (outpu# Equality operatorst) a boolean value
#print(2 == 3)
#print(4 == 4)

# != (inequality operator)
#print(2 != 3 )


# Logical operators

# and, or
# and - this returns (output) a boolean value as well
# True and True -> True
# True and False -> False
# False and False -> False

# or
# True or False -> True
# True or True -> True
# False or False -> False

print(1 and 0)
print(1 and 2)
# Any integer except zero is truthy, 1 is perfect True and every other number is truish



# Assignment operator
# Variables
# A variable is a container (bucket) in the memory of the computer
# It is a location in the memory where data of similar is kept stored
variableA = 5
floatingVariable = 6.3
stringVariable = "This is a string"
AnotherStringVar = 'This is another string'
myName = "Raman"
print("My name is " + myName)
# String concatenation
# Adds two strings
print(myName * 5)
# Formatted Strings
print(f"My name is {myName} and I am {14 + 5} years old")



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
secondLetter = myName[1]
print(secondLetter)

# len() function
# function is a block of code which performs a specific task
# len function returns (output) the length or the number of characters in a string

lenOfMyName = len(myName)
print(lenOfMyName)

thisInteger = 5
print(thisInteger)

# String in short are called str (read as "stirs")
thisString = str(thisInteger)

# Updating Variables
# Varaible naming convention
# input() function
# int(), float()
