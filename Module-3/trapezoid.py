# Write a Python program to calculate the area of a trapezoid

def Area(b1, b2, h):
	return ((b1 + b2) / 2) * h

base1 = 8; 
base2 = 10; 
height = 6
area = Area(base1, base2, height)
print("Area is:", area)
