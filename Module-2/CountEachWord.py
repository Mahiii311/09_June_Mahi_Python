#Write a Python program to count the occurrences of each word in a given sentence
x="this is Python language and this is Tops"
list=x.split(" ")
print(list)
for i in list:
    print(f"{i}= ",list.count(i))
