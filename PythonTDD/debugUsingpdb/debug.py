def funcA(first_val, second_val):
    result = (first_val*2) - (second_val/0)
    return result

def functionB(first_val=23, last_val=72):
    import pdb; pdb.set_trace()
    response = funcA(first_val, last_val)
    result = response * first_val / 7
    return result
    
functionB(33,88) # we are evaluating the function.