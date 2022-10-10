# Write a Python program to find the second smallest number in a list.
def second_smallest(list1):
	list1.sort()
	print("Second Smallest element is:", list1[1])

list1=[2,51,24,30,5,0,65,25,44,3,8,4,]
second_smallest(list1)
