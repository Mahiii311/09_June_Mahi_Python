#Write a Python function to reverses a string if its length is a multiple of 4.
x=input("Enter your string: ")
if len(x)%4==0:
    x=x[::-1]

    
print("string is :",x)