def count(sequence,item):
  """A function that returns the number of occurrences of an item in a sequence"""
  count = 0
  for i in sequence:
    if i == item:
      count+=1
  return count