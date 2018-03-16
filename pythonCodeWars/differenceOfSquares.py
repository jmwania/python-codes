# https://www.codewars.com/kata/difference-of-squares/train/python

def difference_of_squares(n):
    sum_total = 0
    square_total = 0
    for num in range(1,n+1):
        sum_total+=num
        square_total+=num**2

    return square_total - sum_total


