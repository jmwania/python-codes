def factorial(n):
	"""Simple factorial using recursion"""
	if n == 1:
		return n
	elif n == 0:
		return 1
	elif n < 0:
		return "Invalid Input"
	else:
		return n*factorial(n-1)


print factorial(5)
