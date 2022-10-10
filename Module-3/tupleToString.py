# Write a Python program to convert a tuple to a string.
def convert(x):
	str=''
	for i in x:
		str=str+i
	return str

tuple=('T','O','P','S')
str=convert(tuple)
print(tuple)
print(str)
