#################################################
## Practice Problems
#################################################

# 1 #

a = 2
a = a * 2
x = 4 + a
# print(x)
# Write answer below 


# 2 #

a = 9 * 4 // 12 - (7 % 5 + 3)
# a = 9 * 4 // 12 - (5)
# a = 36 // 12 - (5)
# a = 3 - 5
# a = -2
# print(a)
# Write answer below


# 3 #

b = (True and True) or (True and False)
# b = (True) or (True and False)
# b = (True) or (False)
# b = True
c = (True or False) and (True or True)
c = True
d = (b == c)
# print(b)
# print(c)
# print(d)	
# Write ans below




# 4 #

some_string = "Wow!, programming is way easier than I thought."
other_string = "So far."
final_string = some_string + " " + other_string
# print(final_string)
# Write answer below



# 5 #

new_string = "what a day"
other_string = "maybe"
final_string = other_string[2] + other_string[1]
#last_character = new_string[len(new_string) - 1]
# last_character = new_string[10 - 1]
# last_character = new_string[9]
# last_character = "y"
# if we need the last character of a string. Then the index of the last character is length of string - 1.
# If in general case, the length of a string is n, then indexing is from 0 to n - 1.
# 1 to n is n numbers. similarly 0 to n - 1 is also n numbers.
# 1 "w", index = 0
# 2 "h", index = 1
# 3 "a", index = 2
last_character = new_string[-1] # Python specific
# print(final_string + last_character)
# Write answer below


# 6 #

""" Write a program to take input user's first name and user's last name.
    Then print full name of the user with a space between first and last names.
"""

# 7 #

""" Write a program to take input a string. Print the first, last and middle character of the
string in separate lines."""

abcd = "vision"
midindex = len(abcd) // 2
# midindex = 3
# print(midindex) # it is the index of the middle character
# to print the middle char we have to first access it.
# print(abcd[midindex]) # accesing the character
# resolve into simpler line
# print(abcd[3])
# print("s")
abcd[midindex]
abcd[len(abcd) - 1]

# 8 # 

# The following lines of code have some error in them. Correct it.
new_string = "saturday"
# final_string = new_string + 6
# print(final_string)

# 9 # 

a = (5 > 3)
b = (231 < 94)
c = (52 >= 52)
d = (77 <= 813)
answer = (a and d) or (b and c)
# print(answer)
# Write answer below


# 10 #
a = 42
b = 79
# print("The value of a is: " + str(a))
# print(f"The value of b is: {b}")
b = a + b
a = b - a
b = b - a
# print("The new value of a is: " + str(a))
# print(f"The new value of b is: {b}")
# Write answer below. Also, observe the output and see if you find anything special.


# In any expression if we write a variable, then the expression is evaluated by
# replacing the variable by its value.
ab = 42
c = ab + 9
# c = 42 + 9


# 11 #

num = 55
if (num % 5 == 0):
    print("Num is divisible by 5")
else:
    print("Num is NOT divisible by 5")
# Write answer below


# 12 #

num = 21
if (num % 2 == 0):
    print("Num is even")
else:
    print("Num is odd")
# Write answer below


# 13 #

age = 32

if (age >= 65):
    print("You are a senior citizen")
elif (age >= 18 and age < 65):
    print("You are an adult")
else:
    print("You are a minor")
# Write answer below


# 14 #

marks = 47
grade = "" # "" is an empty string
if (marks >= 90):
    grade = "A1"
elif (marks >= 80 and marks < 90):
    grade = "A2"
elif (marks >= 70 and marks < 80):
    grade = "B"
elif (marks >= 60 and marks < 70):
    grade = "C"
elif (marks >= 50 and marks < 60):
    grade = "D"
elif (marks >= 40 and marks < 50):
    grade = "E"
else: 
    grade = "F"
print(grade)
# Write answer below


# 15 #

""" Write a program to take input a number from the user.
Print whether the number is negative, positive or zero."""


# 16 #

""" Write a program to take input two numbers from the user.
Print the larger of the two numbers """


# 17 # 

""" Write a program to input two names from the user.
Print the lexicographically smaller name """


# 18 #

#### HARD ####
""" Take input of age of 3 people by user and determine oldest among them """


# 19 #

""" Write a program to print first 10 natural number in reverse order using while loop """

num = 5
while (num):
    print(num)
    num = num - 1

for num in range(1, 11, 1): # [1, 11) closed is square and open is paranthesis
    print(num)

for num in range(10, 0, -1): # [10, 0) num decreases by 1
    print(num)



# if we need to go forward, then we generally use (num = num + 1, <= )
# in reverse order, num > 0, num = num - 1


# 20 # 

""" Write a program to print sum of first 10 Natural numbers """
sum_var = 0
num = 1
while (num <= 5):
    sum_var =  sum_var + num       # sum_var = 1 + 2 + 3 + 4 + 5
    num = num + 1
print(sum_var)

#
sum_var = 0
for num in range(1, 11, 1):
    sum_var = sum_var + num
print(sum_var)


# 21 # 

#### HARD ####
""" Write a program to take input a string from the user 
and print each character of the string separately on a new line """

string_var = input("Enter a string") # default value is string
n = len(string_var)
index = 0
while (index <= n - 1):
    print(string_var[index])
    index = index + 1

string_var = "jupiter"
n = len(string_var)

for index in range(0, n, 1):
    print(string_var[index]) # iteration



# 22 #

# Write a program to input a string from the user and print the reverse string.

index = len(string_var) - 1
while (index >= 0):
    print(string_var[index])
    index = index - 1



n = len(string_var)

for index in range(n - 1, -1, -1): # [n - 1, -1)
    print(string_var[index])


# 23 # 

my_name = "Tom Marvolo Riddle"
random_index = 7 % 3
print(my_name[random_index])
# Write answer below


# 24 #

num = 1
while (num <= 10):
    if (num % 2): # if (1)
        print(num)
    num = num + 1

# Write answer below
1
3
5
7
9


# 25 #

some_string = "Jupiter"
reverse_string = "" # empty string
index = len(some_string) - 1 # index = 6
while (index >= 0):
    reverse_string = reverse_string + some_string[index] # reverse_string = "retipuJ"
    index = index - 1
print(reverse_string)

# Write answer below
retipuJ

# 26 #

num = 21
while (num):
    if (num < 17):
        print("Ending the loop")
        break
    print(num)
    num = num - 2

# Write answer below
21
19
17
Ending the loop


# Modulo or remainder
