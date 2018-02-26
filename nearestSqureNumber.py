#Find the closest square number
def nearest_sq(n):
    a = int(n**0.5) ** 2
    b = (int(n**0.5) + 1) ** 2
    if abs(a - n) < abs(b - n):
        return a
    return b

print nearest_sq(10)