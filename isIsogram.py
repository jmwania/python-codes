def is_isogram(word):
  """A function to test if a word is an isogram"""
  word_set = set(word)
  
  if word.strip() == "":
    return (word, False)
  elif type(word)!= str:
    return (word, False)
  elif len(word) == len(word_set):
    return (word, True)
  else:
    return (word, False)