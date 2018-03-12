def my_sort(numbers):
  """Function to sort a list into odd and even numbers respectively"""
  odd_list = []
  even_list = []
  
  for num in numbers:
    if num%2 == 0:
      even_list.append(num)
    else:
      odd_list.append(num)
  
  return sorted(odd_list) + sorted(even_list)