def reverse(text):
  reversed_string = ""
  count = len(text)
  while (count > 0):
    reversed_string += text[count-1]
    count -= 1
  return reversed_string