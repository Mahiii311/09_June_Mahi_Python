# Write a Python program to print all unique values in a dictionary.
list1 = [{'abc' : 1, 'xyz' : 2}, {'lmn' : 1, 'ghi' : 3}, {'python' : 2}]

print("The original list : " + str(list1))
x = list(set(val for dict1 in list1 for val in dict1.values()))
print("The unique values in list are : " + str(x))
