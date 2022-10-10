# Write a Python program to convert a list of characters into a string.
def convert(s):
	str = ""
	for x in s:
		str+=x
	return str

s = ['T','O','P','S',' ','P','Y','T','H','O','N']
print(convert(s))
