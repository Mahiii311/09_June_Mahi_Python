# Write a Python script to check if a given key already exists in a dictionary.
dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def key_exist(x):
  if x in dict:
      print(f'Key {x} is present in this dictionary')
  else:
      print(f'Key {x} is not present in this dictionary')
      
print(dict)
key_exist(4)
key_exist(10)

