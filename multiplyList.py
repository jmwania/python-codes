def product(myList):
	prod = 1
	count = len(myList)
	while count > 0:
		prod*= myList[count-1]
		count -=1
	return prod


if __name__ == '__main__':
	nums = [2,5,9,6]
	print product(nums)