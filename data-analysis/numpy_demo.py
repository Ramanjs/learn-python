# Arrays
# List of similar data types
# (1, 2, 4, 3, 8)
# Arrays are fast

import numpy

my_list = [5, 3, 8, 2] # this is python list

my_array = numpy.array(my_list) # convert list to array

second_item = my_array[1]

two_d_array = numpy.array([ [2, 3], [7, 9] ])
first_array = two_d_array[0]
print(first_array)

# Slice function
middle_array = my_array[1:3]
print(middle_array)

arr = numpy.array([1, 2, 3, 4, 5, 6])

new_arr = numpy.array_split(arr, 3) # arguments are the array which you want to split and the number of parts

# [1, 2], [3, 4], [5, 6]
# array_split() returns a 2d array

print(new_arr[0])

# where() function
# it returns index of matched values
# where() function checks the condition for every element in the array

x = numpy.where(arr == 3)

y = numpy.where(arr%2 == 1)
print(x)
print(y)

# sort()
# arranging 
# sort returns a new array which is oredered
# it first makes a copy of the original array and then sorts it
new_arr = numpy.array([5, 2, 9, 6, 1])

x = numpy.sort(new_arr)[::-1] # reversing the array

print(x)

# descending order

# slice [start:end:-1]


# filter
# if we need to extract some specific values from the array

filter_array = [True, False, True, True, False]

x = new_arr[filter_array]
# [5, 2, 9, 6, 1], [True, False, True, True, False]

idx = 0
for i in new_arr:
	if (i%2 == 0):
		filter_array[idx] = True
	else :
		filter_array[idx] = False
	idx = idx + 1

# filter_array = [False, True, False, True, False]
# idx = 3

x = new_arr[filter_array]
# [5, 2, 9, 6, 1], [False, True, False, True, False]

print(x)