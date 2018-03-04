def is_prime(num):
    if num < 2:
        return "Number is not prime"
    else:
        for n in range(2,num):
            if num % n == 0:
                return "{} multiplied by {} equals {}".format(n,(num/n),num)
        #Else statement here runs when the looks exits normally without encountering a break.
        else:
            return "Number is prime"


print is_prime(100)
