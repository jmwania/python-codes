def string_clean(s):
    # return filter(lambda a: not a.isdigit(), s)
    new_str = ""
    for c in s:
        for i in "0123456789":
            if c == i:
                c = ""
            else:
                c = c
        new_str+=c
    return new_str
  
  


print string_clean("655kjk44")
