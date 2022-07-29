#Write a Python program to check if a number is positive, negative or zero.
x=int(input("Enter a number to check="))
if x>0:
    print("{} is Positive".format(x))
elif x<0:
    print("{} is Negative".format(x))
else:
    print("{} is Zero".format(x))