def remove_duplicates(inputlist):
	"""A function that takes in a list and returns unique values in form of a list"""
    if inputlist == []:
        return []
    
# Sort the input list from low to high    
    inputlist = sorted(inputlist)
# Initialize the output list, and give it the first value of the now-sorted input list
    outputlist = [inputlist[0]]

# Go through the values of the sorted list and append to the output list
# ...any values that are greater than the last value of the output list
    for i in inputlist:
        if i > outputlist[-1]:
            outputlist.append(i)
        
    return outputlist


	


if __name__ == '__main__':
	lst = [1,1,2,2,4]
	print remove_duplicates(lst)


