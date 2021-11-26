#################################################
## Lists
#################################################

# A list is a value that contains multiple values
# It is a data structure
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

# changing list items

myFriends[3] = "this"


# adding lists

print(myFriends + myNumbers)

# shorthand updation
num = 0
num = num + 1

num += 1 # num = num + 1
num -= 1 # num = num - 1
num *= 3 # num = num * 3
num /= 5 # num = num / 5

# for loop in lists

for item in myFriends:
	print(item)

# Other way of doing the above thing
for i in range(0, len(myFriends), 1):
	print(myFriends[i])


string_var = "this"

for charachter in string_var:
	print(charachter)

# index()
# It searches for the argument in the given list and returns its index if found in the list
indexOfParth = myFriends.index("parth") 
print(indexOfParth)

# indexOf = myFriends.index("ram") -> Gives error as "ram" is not in the list
# print(indexOf)

# insert()
# It inserts given value inside the list
# It takes two arguments : First is the index before which the new item is to be inserted, and second is the item itself
myFriends.insert(4, "harsh") # Inserts "harsh" before index 4
print(myFriends)

# remove()
# It removes the given value from the list
myFriends.remove("harsh")
print(myFriends)

# myFriends.remove("new") -> this gives error as "new" is not in the list

# sort(), arranging in ascending order
myFriends.sort()
print(myFriends)

# Sorting in descdending order
# We use the reverse keyword
myFriends.sort(reverse = True)

# in and not in
# If we need to check that a specific item exists in the list then we use the in operator
a = "parth" in myFriends
print(a)

b = "parth" not in myFriends
print(b)

string_var = "tom"
a = "t" in string_var
print(a)



# mutable and immutable

# Mutable means can be changed
myFriends[4] = "ashmit"
# Lists are mutable

# Strings are immutable
string_var = "this"

#################################################
## Tuples
#################################################

# They are identical to lists
# Except for the fact that they are immutable
# lists start with [], tuples are enclosed in ()
myList = ['tom', 'marvolo', 'riddle']

myTuple = ('tom', 'marvolo', 'riddle')
# Indexed data structures are ordered
print(myTuple[0])