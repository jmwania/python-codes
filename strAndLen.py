def add_length(str_):
  return map(lambda x: x +" "+str(len(x)),str_.split(" "))

print add_length('you will win')