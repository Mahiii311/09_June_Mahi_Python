# Write a Python function that checks whether a passed string is palindrome or not

def isPalindrome(s):
	return s == s[::-1]

s = input("Enter your string ")
ans = isPalindrome(s)

if ans:
	print(f"Given string {s} is palindrome")
else:
	print(f"Given string {s} is not palindrome")
