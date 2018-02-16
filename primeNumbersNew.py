def is_prime(number):
	if number is 1:
		return False
		for value in range(2, int(number ** 0.5) + 1):
			if number % value is 0:
				return False
		return True
		
def collect_prime_numbers(number):
	prime_numbers = []
	for i in range(3, number + 1):
		if is_prime(i):
			prime_numbers.append(i)
	return prime_numbers
print(collect_prime_numbers(20))


