#Write a Python function that takes a list of words and returns the length of the longest one.
list1=['mahi','python','tops','project']
finalList = []
     
for word in list1:
        finalList.append((len(word), word))
     
finalList.sort()
print("The word with the longest length is:", finalList[-1][1]," and length is ", len(finalList[-1][1]))