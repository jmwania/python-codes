# Create a function that returns the CSV representation of a two-dimensional numeric array.
def csv(array):
   return '\n'.join(','.join(map(str,line)) for line in array)



print csv([[ 0, 1, 2, 3, 45 ],[ 10,11,12,13,14 ], [20,21,22,23,24 ],[ 30,31,32,33,34 ]] )
