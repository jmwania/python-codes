def array_madness(a,b):
  #Comparing the two item
  if sum(list(map(lambda x:x**2,a))) > sum(list(map(lambda x:x**3,b))):
  	return True

print array_madness([4, 5, 6], [1, 2, 3])