# http://www.codewars.com/kata/bin-to-decimal/train/python

def binary_to_decimal(binary):
    counter = len(binary)-1
    decimal_num = 0

    while counter >= 0:
        for char in binary:
            decimal_num += int(char) * 2**counter
            counter -= 1
    return decimal_num

print binary_to_decimal('1001001')


