from collections import Counter
def common(a,b,c):
	#Print the sum of common numbers in three lists
    return sum((Counter(a) & Counter(b) & Counter(c)).elements())

 
print (common([1,2,2,3],[5,3,2,2],[7,3,2,2]))





