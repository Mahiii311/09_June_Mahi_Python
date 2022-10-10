# Write a Python program to remove an empty tuple(s) from a list of tuples.
def Remove(tuples):
	tuples = [t for t in tuples if t]
	return tuples

tuples = [(), ('33','15','8'), (), ('ram','laxman', 'sita'),
		('krishna', 'radha', '100'), ('',''),()]
print(tuples)
print(Remove(tuples))
