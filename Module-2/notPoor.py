#Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
# if 'not' follows the 'poor',
# replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
x=input("Enter a string: ")
xnot= x.find('not')  
xpoor= x.find('poor')  

if xnot==-1 or xpoor==-1:
    print("no change in string")
else:
    if xpoor > xnot:  
        x= x.replace(x[xnot:(xpoor+4)], 'good')  

print(f"resulting string is: {x}")