#Square each number in a list
def maps(a):
    return list(map((lambda x:x**2),a))

    #Using list comprehension
    # return [x**2 for x in a]

print maps([6,4])