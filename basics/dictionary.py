#################################################
## Dictionary
#################################################

# Word: meaning
# Key: value 
# Data is stored in key-value pairs
# Dict does not have indeces
# Dicts are unordered
# Data can be in any random order
# To access our data we need its key

myDict = { 
	"mutable": "cannot be changed",
 	"tom M riddle": "Lord Voldemort",
 	452 : "four five two",
	"myList": ["one", "two", "three"]
}

value = myDict["mutable"]
print(value)
print(len(myDict))

print(myDict["myList"])

# Key-value pairs. Keys are like a list indexes

# Mutable
# one : 1
# Adding new item into the dictionary
myDict["one"] = 1

# print(myDict)

# Unordered -> no indexes, can exist in random order

# keys(), values(), items()

# keys()
# keys() is a internal function of dictionary
# to call internal functions we use dot operator
myKeys = myDict.keys()
print(myKeys)

# values()

myValues = myDict.values()
print(myValues)

# items()

myItems = myDict.items()
print(myItems)




# get()
#print(myDict["random"])
myValue = myDict.get("random")

a = "one" in myDict
print(a)

# updating dictionary
myDict["mutable"] = "un-changable" # assignment operator
myLetters = ['a', 'b', 'c', 'd', 'e']
myLetters.insert(3, 'f') # index at which we have to insert
print(myLetters)
myLetters = ['a', 'b', 'c', 'f', 'd', 'e']