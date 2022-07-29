#Write a python program to sum of the first n positive integers
n=int(input("Enter the value of n= "))
sum=0
for i in range(n+1):
    sum+=i
print(f"sum of first {n} positive number is {sum}")