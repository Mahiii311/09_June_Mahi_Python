#Write a Python function to insert a string in the middle of a string
x=input("Enter a string: ")
y=input("insert in middle of string: ")

print(x[0:len(x)//2]+y+x[len(x)//2:])
