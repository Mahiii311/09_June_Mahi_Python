#Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.
x=int(input("Enter a number to check="))
if x%2==0:
    print(f"{x} is even number")
else:
    print(f"{x} is odd number")