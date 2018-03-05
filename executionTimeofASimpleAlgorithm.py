#Using the time module
import time

def sumOfN2(n):
    start = time.time()

    sum = 0
    for i in range(1,n+1):
        sum += i

    stop = time.time()

    return sum, stop-start


for i in range(5):
    print ("Sum is %d required %10.7f seconds" % sumOfN2(1000000))
print("\n")


#Taking advantage of a closed equation instead of looping.
def sumOfN3(n):
    start = time.time()
    sum = (n*(n+1))/2
    stop = time.time()
    return sum, stop-start

for i in range(5):
    print ("Sum is %d required %10.7f seconds" % sumOfN3(1000000))


