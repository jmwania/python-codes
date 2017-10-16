def median(lst):
	"""A function that returns the median of a list of numbers"""
	#Sort the list first
	lst = sorted(lst)

	#Find median based on whether the length of the list is odd or even
	if len(lst) % 2 == 0:
		return (lst[len(lst)/2] + lst[(len(lst)/2)-1]) / 2.0
	else:
		return lst[(len(lst)/2)]
		

if __name__ == '__main__':
	lst = [2,5,9,56,8,5]
	print median(lst)