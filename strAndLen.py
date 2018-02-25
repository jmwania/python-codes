def add_length(str_):
  return map(lambda x: x +" "+str(len(x)),str_.split(" "))

  #Other means

  # def add_length(str_):
  #   return ["{} {}".format(i, len(i)) for i in str_.split(' ')]

print add_length('you will win')