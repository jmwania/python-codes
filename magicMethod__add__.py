class Vector:
	#Class to demonstrate how to override + using the magic method __add__
  def __init__(self,x,y):
    self.x = x
    self.y = y
    
  def __add__(self,other):
    return Vector(self.x+other.x,self.y+other.y)
    

first = Vector(2,2)
second = Vector(3,3)
third = first + second
print ('{},{}'.format(third.x,third.y))
