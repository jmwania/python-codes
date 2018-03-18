# https://www.codewars.com/kata/hex-to-decimal/train/python
def hex_to_dec(s):
    counter = len(s)-1
    decimal_num = 0

    while counter >= 0:
        for char in s:
            if char == "a":
                char = 10
            elif char == "b":
                char = 11
            elif char == "c":
                char = 12
            elif char == "d":
                char = 13
            elif char == "e":
                char = 14
            elif char == "f":
                char = 15
            decimal_num += int(char) * 16**counter
            counter -= 1
    return decimal_num

print hex_to_dec('13f')