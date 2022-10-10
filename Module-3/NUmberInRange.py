# Write a Python function to check whether a number is in a given range
def func(n):
    if n in range(0,9):
        print( f" {n} is in the range")
    else :
        print(f"{n} is outside the given range.")

func(5)
func(10)
