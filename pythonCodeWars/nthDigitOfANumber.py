
#The function findDigit takes two numbers as input, num and nth. It outputs the nth digit of num 
#(counting from right to left).

# #Note

# If num is negative, ignore its sign and treat it as a positive value.
# If nth is not positive, return -1.
# Keep in mind that 42 = 00042. This means that findDigit(42, 5) would return 0.
# #Examples

# findDigit(5673, 4)     returns 5
# findDigit(129, 2)      returns 2
# findDigit(-2825, 3)    returns 8
def find_digit(num, nth):
    num = str(abs(num))
    if nth < 1:
        return -1
    elif len(num) < nth:
        return 0
    else:
        return int(num[-nth])

print find_digit(5673, 5)