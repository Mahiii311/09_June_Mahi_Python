# Write a Python script to sort (ascending and descending) a dictionary by value.

dict1 = {'c': 3, 'a': 1, 'd': 4, 'b': 2}
print(dict1)

sorted_dict = sorted([(value, key)
for (key, value) in dict1.items()])

print("Sorted dictionary is :")
print(sorted_dict)
