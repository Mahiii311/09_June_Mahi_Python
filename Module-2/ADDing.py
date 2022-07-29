#Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
#If the given string already ends with 'ing' then add 'ly'
#instead if the string length of the given string is less than 3, leave it unchanged.
x=input("Enter a string: ")
if(len(x)>=3):
    if x.endswith("ing"):
        x=x+"ly"
        print(x)
    else:
        x=x+"ing"
        print(x)
else:
    print(f"Length of string '{x}' is less then 3. So no change in string")