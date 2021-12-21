import matplotlib.pyplot as plt
import numpy

# point is represented as x-cord, y-cord
# (4, 5), (3, 1)
# list of x cordinates
# (4, 3)
# (5, 1)
x_cord = numpy.array([4, 3])
y_cord = numpy.array([5, 1])

# plot() accepts two arguments, x_cord and y_cord
# plt.plot(x_cord, y_cord, 'o') # plots the points
# plt.show() # displays the graph

# # marker:line:color
# plt.plot(x_cord, y_cord, 'o:r')
# plt.show()

x = numpy.random.normal(10, 50, 5) # x is a histogram

# hist()
plt.hist(x)
plt.show()