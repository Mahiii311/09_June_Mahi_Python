#Write python program that swap two number with temp variable and without temp variable.
a=5
b=9
print(f"before swap a={a} and b={b}")
#using temp
temp=a
a=b
b=temp
print(f"after swap using temp veriable a={a} and b={b}")

#without using temp
a=a+b
b=a-b
a=a-b
print(f"after swap without using temp veriable a={a} and b={b}")

