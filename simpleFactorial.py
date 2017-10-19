def factorial(n):
	product = 1
	for n in range(1,n+1):
		product *=n
	return product

print factorial(5)