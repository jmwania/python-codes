 def purify(numbers):
  """A function that takes a list of numbers and removes all odd numbers from that list"""
  new_list = []
  for item in numbers:
    if item % 2 == 0 and item > 1:
      new_list.append(item)
  return new_list