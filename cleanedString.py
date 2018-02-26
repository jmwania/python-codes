def string_clean(s):
    return filter(lambda a: not a.isdigit(), s)
  
  
  


print string_clean("655kjk44")
