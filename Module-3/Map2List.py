# Write a Python program to map two lists into a dictionary

keys = ["TOPS", "Python", "Practice"]
values = [1, 2, 3]

print("key list is : " + str(keys))
print("value list is : " + str(values))

x = dict(zip(keys,values))
print("Dictionary is : " + str(x))
