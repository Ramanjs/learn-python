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