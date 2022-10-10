# Write a Python script to merge two Python dictionaries
dict1= {'a': 100, 'b': 200, 'c': 300}
dict2= {'x': 400, 'y': 500, 'z': 500}

dict0= dict1.copy()
dict0.update(dict2)

print(dict1)
print(dict2)
print("Merge dictionary is ",dict0)
