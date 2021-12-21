import pandas

a = [5, 4, 9]

my_series = pandas.Series(a)

print(my_series)

my_series = pandas.Series(a, index = ["a", "b", "c"])

print(my_series)
print(my_series["b"])