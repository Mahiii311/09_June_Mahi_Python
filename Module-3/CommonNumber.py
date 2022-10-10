# Write a Python function that takes two lists and returns true if they have at least one common member.
def Find_common(list1, list2):
	result = False
	for x in list1:
		for y in list2:
			if x == y:
				result = True
				return result
	return result

a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(Find_common(a, b))

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
print(Find_common(a, b))