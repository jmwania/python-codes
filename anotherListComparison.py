def find_difference(a, b):
  return abs(reduce(lambda x,y: x*y,a) - reduce(lambda x,y:x*y,b))

print find_difference([3, 2, 5], [1, 4, 4])