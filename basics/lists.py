#################################################
## Lists
#################################################

# A list is a value that contains multiple values
# Data Structure
myFriends = ["raman", "ashmit", "parth", "ashutosh", "devansh", "mayank"]
myNumbers = [1, 2, 3, 9, 5, 4]
randonList = ["string", 5.32, 6]

# The values in a list are also called items
# You can access items in a list with it's index

print(myFriends[2])

# The indexes start at 0

# Negative indexes
string_var = "this"
lastChar = string_var[-1]
print(lastChar) # -> i
firstItem = myFriends[-4]
print(firstItem)

# Slice function
newList = myFriends[1:4] # [1, 4)
print(newList)

newList = myFriends[:4]
print(newList)

newList = myFriends[1:]
print(newList)

print(string_var[::-1])

# len(), concatenation same as strings
lengthOfList = len(myFriends)
print(lengthOfList)

# list()

newList = list("this")
print(newList)

# Append
myFriends.append("raj")
print(myFriends)

students = []
for i in range(0, 50):
	new_student = input("Enter student name ")
	students.append(new_student)