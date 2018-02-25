def listsum(mylist):
	"""Function that returns the index in an array where the sum of values on the right side of the index is the same
	as the sum on the left side of the index"""
	for value in range(len(mylist)):
		if sum(mylist[:value]) == sum(mylist[value+1:]):
			return value
		return False
			

	
#Some test here.
list1 = [1,0]
print (listsum(list1))




