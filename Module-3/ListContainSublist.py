# Write a Python program to check whether a list contains a sub list

list1 = [9, 4, 5, 8, 10]
sublist = [10, 5, 4]

print("Original list : " + str(list1))
print("Sub list : " + str(sublist))

flag = 0
if(all(x in list1 for x in sublist)):
	flag = 1

if (flag):
	print("Yes, list is contain sub list")
else:
	print("No, list is not contain this sub list")
