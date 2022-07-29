#Write a Python program to get a single string from two given strings,
#separated by a space and swap the first two characters of each string.
s="Tops Python"
s=s.split(" ")
#print(s[0][0:2])
s1=s[0][0:2]+s[1][2:]
s2=s[1][0:2]+s[0][2:]
print(s1)
print(s2)