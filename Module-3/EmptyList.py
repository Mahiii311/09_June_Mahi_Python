# Write a Python program to check a list is empty or not.
def Empty_List(lists):
	if len(lists) == 0:
		return 0
	else:
		return 1

lists = []
if Empty_List(lists):
	print("The list is not empty!!")
else:
	print("Empty List..")
