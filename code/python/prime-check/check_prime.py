#!/usr/bin/env python3
from fast_ex import compute_modular_exponent
import random

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def is_prime(m):
    r1 = random.randint(2, m * 10)
    maybe = 0
    if compute_modular_exponent(2, m - 1, m) == 1:
        maybe = 1
    if compute_modular_exponent(r1, m - 1, m) != 1:
        maybe = 0
    return maybe

def main():
    primes = [2]
    for i in range(1, 1000):
        if is_prime(i):
            primes.append(i)
    for row in chunks(primes, 20):
        print(row)

if __name__ == '__main__':
    main()
