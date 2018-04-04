class Calculator(object):
    """Calculator class for four basic mathematical operations"""
    number_types = (int, long, float, complex)

    #add
    def add(self,x,y):
        if isinstance(x, Calculator.number_types) and isinstance(y, Calculator.number_types):
            return x+y    
        else:
            raise ValueError
    #subtract
    def subtract(self,x,y):
        if isinstance(x, Calculator.number_types) and isinstance(y, Calculator.number_types):
            return x-y
        else:
            raise ValueError

    #Divide
    def divide(self,x,y):
        if isinstance(x, Calculator.number_types) and isinstance(y, Calculator.number_types):
            if y == 0:
                raise ZeroDivisionError
            return x//y
        else:
            raise ValueError
    #Multiply
    def multiply(self,x,y):
        if isinstance(x, Calculator.number_types) and isinstance(y, Calculator.number_types):
            return x*y
        else:
            raise ValueError


