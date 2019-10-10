#!/usr/bin/env python3

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif (n % 2 == 0 or n % 3 == 0):
        return False
    elif ((n - 1) % 6 == 0 or (n + 1) % 6 == 0):
        return False
    else:
        return True


def print_factors(n):
    if n <= 1:
        print("n is less than or equal to one, therefore not prime.")
    else:
        factors = []
        for i in range(2, n):
            if (n % i == 0):
                factors.append(i)
        print("The factors of {} are:".format(n))
        print(factors)


def main():
    n = int(input("Enter an integer: "))
    if (is_prime(n)):
        print("{} is prime.".format(n))
    else:
        print("{} is not prime.".format(n))
        print_factors(n)

if __name__ == '__main__':
    main()
