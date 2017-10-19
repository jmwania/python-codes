def helloWorld(count):
	"""Simple function using recursion to print an output 10 times"""
	if count < 1:
		return
	print "Hello World"
	helloWorld(count - 1)

helloWorld(10)