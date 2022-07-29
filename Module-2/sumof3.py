#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
x=int(input("x= "))
y=int(input("y= "))
z=int(input("z= "))
if x==y or y==z or x==z:
    sum=0
    print("Here two or three values are equal so")
else:
    sum=x+y+z
print(f"Addition of three number is {sum}")