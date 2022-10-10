# Write a Python program to count the number of strings 
# where the string length is 2 or more and 
# the first and last character are same from a given list of strings.
def match_words(words):
  x=0
  for i in words:
    if len(i)>1 and i[0]==i[-1]:
      x+=1
  return x

print(match_words(['abcd', 'xyz', 'abht', '1516','dajcn']))
