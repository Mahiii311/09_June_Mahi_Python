# Write a Python program to unzip a list of tuples into individual lists.
list1 = [('This', 1), ('is', 2), ('Python', 3), ('in', 4), ('TOPS', 5)]
print ("Original list is : " + str(list1))

New_list = [[ i for i, j in list1 ],[ j for i, j in list1 ]]

print ("Modified list is : " + str(New_list))
