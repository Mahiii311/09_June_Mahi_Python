# Write a Python function to get the largest number, smallest num and sum of all from a list.
x = []
# number of elements as input
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input())
    x.append(ele)
print("List is: ",x)      
print("Largest number of list is ",max(x))
print("Smallest number of list is ",min(x))
print(sum(x))
