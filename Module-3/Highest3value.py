# Write a Python program to find the highest 3 values in a dictionary
my_dict = {'A': 22, 'B': 16, 'C': 64, 'D': 70, 'E': 59, 'F': 69}

print("Initial Dictionary:",my_dict)
print("Dictionary with 3 highest values:")
print("Keys: Values")

x=list(my_dict.values())
x.sort(reverse=True)
x=x[:3]

for i in x:
	for j in my_dict.keys():
		if(my_dict[j]==i):
			print(str(j)+" : "+str(my_dict[j]))
