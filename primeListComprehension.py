def is_prime(num):
	"""A function to get list of prime numbers using list comprehension(Sieve of Eratosthenes).
	First build a list of non-prime numbers, using a single list comprehension,
	then use another list comprehension to get the "inverse" of the list, which are prime numbers."""
	
	noprimes = [j for i in range(2,8) for j in range(i*2,num,i)]
	primes = [x for x in range(2,num) if x not in noprimes]
	print primes


if __name__ == '__main__':
	is_prime(15)
