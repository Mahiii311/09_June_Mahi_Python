# Write a Python program to returns sum of all divisors of a number
def div(n):
    divisors = [1]
    for i in range(2, n):
        if (n % i)==0:
            divisors.append(i)
    return sum(divisors)

print(div(8))
print(div(12))
