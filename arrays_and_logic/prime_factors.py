from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    divisors = [i for i in range(2, int(sqrt(n))+1) if n % i == 0]
    return not divisors

def factors(value):
    if value < 2:
        return []
    divisors = []
    while not is_prime(value):
        for i in range(2, value):
            if value % i == 0:
                divisors += [i]
                value = int(value/i)
                break
    divisors += [value]
    return divisors
