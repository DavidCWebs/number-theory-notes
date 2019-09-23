#!/usr/bin/env python3

def extended_gcd(a, b):
    assert a >= b and b >= 0 and a + b > 0

    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y
    return (d, x, y)

def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(extended_gcd(a, b))

if __name__ == '__main__':
    main()

