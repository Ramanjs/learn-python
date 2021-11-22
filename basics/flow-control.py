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

# Flow is the execution of the python program
# Run or execute a program through command prompt
# A program runs from top to bottom, line by line
# Flow control statements ; They can change the flow of the program
# These statements can cause the interpreter to skip a block of code, or
# repeat some block of code a fixed number of time.

# Conditions
# comparision operators. If a certain condition is true or false, then we can use these statements to direct program flow.

# Blocks of Code or Clauses (Indentation)
print("Hello")
# Block change
# Changing indentation creates a new block
# You can only create a new block with flow control statements, If, else if, else, while loop, etc.
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

# If the statement inside the if conditions is true then run next block, otherwise skip it.

# else if -> elif
age = 8 
if (age > 10):
  print("my age is greater than 10 years")
else:
  print("my age is less than 10 years")



# else -> if all the above conditions are false, then the else block of code is run


# while loop
# it is used to repeat a block of code some fixed number of times, or even infinitely

# marks = 45
# while (marks > 40):
#   print("fail")
#   marks = marks + 1

# while loop; Components
# 1. Starting point. We can store the starting point in variable.
# 2. While condition. End point.
# 3. Updation of variable. if we need to go forwards, then num = num + 1, or num = num - 1 for backwards

# break, continue

# Break statement
# it is used to break the while loop
# num = 1 # dry run 
# while (num <= 10):
#   if (num == 5):
#     break
#   print(num)
#   num = num + 1
# after the break statement is met, the rest of the while loop block is skipped and the loop is broken


# continue statement

# num = 1 # dry run
# while (num <= 10):
#   if (num == 5):
#     num = num + 1
#     continue
#   print(num)
#   num = num + 1

# after the continue statement is met, the rest of the while loop is skipped and program starts again from the
# beginning of the while loop


# truthy and falsey values
# all numbers except 0 are truish, truthy
bool(3) # True
bool(0) # False
# 0 False, 1 True

# num = 5
# while (num):
#   print(num)
#   num = num - 1

# falsey values are 0, 0.0, string ka false ""
"this", "raman" # are true

# range() function

# In range function, we pass three values
# range(start, end, step)
# [3, 5) -> 3, 4
# [start, end)

# num = 1
# while (num <= 10):
#    num = num + 1

for num in range(11, 0, -1): # num in the range [1, 11)
  print(num)
