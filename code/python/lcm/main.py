#!/usr/bin/env python3

# Brute force the lcm by iterating over a range from 1 to
# the multiple of a and b (which is defintely a multiple).
# Check at each iteration if the target is divisible by both
# a and b.
def naive_lcm(a, b):
    assert a > 0 and b > 0

    for d in range(1, a * b + 1):
        if d % a == 0 and d % b == 0:
            return d

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        gcd(b, a % b)

def lcm(a, b):
    assert a > 0 and b > 0
    return (a * b) // gcd(a, b)

def main():
    a = int(input("Input a: "))
    b = int(input("Input b: "))
    print("Naive lcm of {} and {} is {}".format(a, b, naive_lcm(a, b)))
    print("Efficient lcm of {} and {} is {}".format(a, b, lcm(a, b)))

if __name__ == '__main__':
    main()
