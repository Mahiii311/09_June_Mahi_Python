#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
#If the string length is less than 2, return instead of the empty string.
x=input("Enter a string: ")
if len(x)<2:
    print("Empty String")

else:
    print(x[0:2]+x[len(x)-2:len(x)])