def remove_duplicates(string):
  """A function to remove duplicates from a string"""
  count = 0
  result = []
  for char in string:
    if char not in result:
      result.append(char)
      count += 1
  return ("".join(sorted(result)),len(string)- count)