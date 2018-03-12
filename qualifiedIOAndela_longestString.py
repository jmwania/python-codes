def longest(string):
  """Function to return the longest word in a sentence"""
  word_lengths = []
  for word in string.split(" "):
    word_lengths.append(len(word))
    
  max_word_length = max(word_lengths)
  for word in string.split(" "):
    if len(word) == max_word_length:
      return word