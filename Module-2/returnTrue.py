#Write a Python program that will return true if the two given 
#integer values are equal or their sum or difference is 5.
print("Enter any two integer values")
x=int(input("Enter value of x: "))
y=int(input("Enter value of y: "))

def func(x,y):
    if x==y or x+y==5 or x/y==5:
        return True
    else:
        return False
print("Given integer values are equal or their sum or difference is 5 is ",func(x,y))
