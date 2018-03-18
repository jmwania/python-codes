# https://www.codewars.com/kata/sum-of-multiples/train/python
def sum_mul(n, m):
    total = 0
    count = n
    if n <= 0 or m <= 0:
        return 'INVALID'
    else:
        while n < m:
            total += n
            n += count
    return total

print sum_mul(0,0)
