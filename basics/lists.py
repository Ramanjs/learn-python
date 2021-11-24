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

print(myFriends[2]) # -> "parth"

# The indexes start at 0

# Negative indexes start from the end
string_var = "this"
lastChar = string_var[-1] 
print(lastChar) # -> "s"
firstItem = myFriends[-4] 
print(firstItem) # -> "parth"

# Slice function
newList = myFriends[1:4] # [1, 4)
print(newList) # -> ["ashmit", "parth", "ashutosh"]

newList = myFriends[:4]
print(newList) # -> ["raman", "ashmit", "parth", "ashutosh"]

newList = myFriends[1:]
print(newList) # -> ["ashmit", "parth", "ashutosh", "devansh", "mayank"]

string_var = "raman"
print(string_var[::-1]) # -> "namar"

# len()
lengthOfList = len(myFriends)
print(lengthOfList) # -> 6


# list()

newList = list("this")
print(newList) # -> ['t', 'h', 'i', 's']

# Append -> adds a new item to the end of the list
myFriends.append("raj")
print(myFriends)

students = []
for i in range(0, 50):
	new_student = input("Enter student name ")
	students.append(new_student)
