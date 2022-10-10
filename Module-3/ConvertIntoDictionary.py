# Write a Python program to convert a list of tuples into a dictionary

def Convert(tup, di):
	for a, b in tup:
		di.setdefault(a, []).append(b)
	return di
		
tuples = [('This', 1), ('is', 2), ('Python', 3), ('in', 4), ('TOPS', 5)]

dictionary = {}
print (Convert(tuples, dictionary))
