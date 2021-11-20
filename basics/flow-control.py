# Comparison Operators, only with int and float
# >, <, >=, <=, ==, !=
# They also return boolean value
print(4 < 5)
print(5 > 2)


# >= is called greater than or equal to
a = 9
b = 9
print(a >= b) # If left value is greater or equal to right value then it returns true

# <= is called less than equal to
print(a <= b)


# Not operator

# not operator inverts boolean values
print(not True)

# while loop (condition)
print(not False)

# not can be denoted by !
#print(True)
#print(False)

# Expressions vs Statements
# Expression is any python line that evaluates to any value.
(True and True) # This is an expression
# Statement is any python line that does not evaluate to any value.
print("Good day")
string_var = "new string"


##################################################
## Flow Control
##################################################

# Flow is the execution of the python program.
# Run or execute
# A program runs from top to bottom, line by line
# Flow control statements ; They can change the flow of the program.
# These statements can cause the interpreter to skip a block of code, or
# repeat some block of code a fixed number of time.

# Conditions
# comparision operators. If a certain condition is true or false, then we can use these statements to direct program flow.

# Blocks of Code or Clauses (Indentation)
print("Hello") # Block change
# Changing indentation creates a new block
# You can only create a new block with flow control statements, If, else if, else, while loop.
  # print("World")

# A block is a set of continuous lines of code in the same indentation
string_var = "this "
print(string_var)
print(len(string_var))

  # # New block
  # print("Hello")
  # other_var = "okay"
  # print(len(other_var))

# Flow Control Statements
# if, else, else if
age = 10
if (age > 10):
	# if (False):
	# new block of code has started
	print("My age is greater than 10 years")




# while loop
# break, continue