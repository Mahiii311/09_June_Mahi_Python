#Write a Python program to get the Factorial number of given number.
x=int(input("Enter number="))
ans=1
for i in range(1,x+1):
    ans=i*ans
print(f"factorial of {x} is {ans}")