# Write a Python program to reverse a tuple.
def Reverse(tuples):
	newtuple = tuples[::-1]
	return newtuple

tuples=('T','O','P','S',' ','P','Y','T','H','O','N',9)
print(tuples)
print(Reverse(tuples))
