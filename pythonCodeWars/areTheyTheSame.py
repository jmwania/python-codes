#https://www.codewars.com/kata/550498447451fbbd7600041c/train/python
def comp(array1, array2):

    squares = [i**2 for i in array1]
    
    if sorted(squares) == sorted(array2):
        return True
    else:
        return False


a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
print (comp(a,b))