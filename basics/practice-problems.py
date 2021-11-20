#################################################
## Practice Problems
#################################################

# 1 #

a = 2
a = a * 2
x = 4 + a
print(x)
# Write answer below 


# 2 #

a = 9 * 4 // 12 - (7 % 5 + 3)
# a = 9 * 4 // 12 - (5)
# a = 36 // 12 - (5)
# a = 3 - 5
# a = -2
print(a)
# Write answer below


# 3 #

b = (True and True) or (True and False)
# b = (True) or (True and False)
# b = (True) or (False)
# b = True
c = (True or False) and (True or True)
c = True
d = (b == c)
print(b)
print(c)
print(d)	
# Write ans below




# 4 #

some_string = "Wow!, programming is way easier than I thought."
other_string = "So far."
final_string = some_string + " " + other_string
print(final_string)
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
print(final_string + last_character)
# Write answer below


# 6 #

""" Write a program to take input user's first name and user's last name.
    Then print full name of the user with a space between first and last names.
"""

# 7 #

""" Write a program to take input a string. Print the first, last and middle character of the
string in separate lines."""

# 8 # 

# The following lines of code have some error in them. Correct it.
new_string = "saturday"
final_string = new_string + "6"
print(final_string)

# 9 # 

a = (5 > 3)
b = (231 < 94)
c = (52 >= 52)
d = (77 <= 813)
answer = (a and d) or (b and c)
print(answer)
# Write answer below


# 10 #
a = 42
b = 79
print("The value of a is: " + str(a))
print(f"The value of b is: {b}")
b = a + b
a = b - a
b = b - a
print("The new value of a is: " + str(a))
print(f"The new value of b is: {b}")
# Write answer below. Also, observe the output and see if you find anything special.