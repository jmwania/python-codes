class Alphabet:
	#Class to demonstrate how to override / using the magic method __truediv__
	#Make sure to use python3
  def __init__(self,cont):
    self.cont = cont
    
  def __truediv__(self,other):
  	line = "="*len(other.cont)
  	return "\n".join([self.cont,line,other.cont])
    

foo = Alphabet("Spam")
bar = Alphabet("Hello World")
print(foo/bar)


# class SpecialString:
#   def __init__(self, cont):
#     self.cont = cont

#   def __truediv__(self, other):
#     line = "=" * len(other.cont)
#     return "\n".join([self.cont, line, other.cont])

# spam = SpecialString("spam")
# hello = SpecialString("Hello world!")
# print(spam / hello)