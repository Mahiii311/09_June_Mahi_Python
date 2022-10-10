# Write a Python program to replace last value of tuples in a list.

lists = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]
print(lists)
print([tuples[:-1] + (500,) for tuples in lists])
