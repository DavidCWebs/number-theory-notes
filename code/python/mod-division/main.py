#!/usr/bin/env python3
#
# Given three integers a, b, and n, such that gcd⁡(a,n) = 1 and n >1
# The algorithm should return an integer x such that
#
# 0 ≤ x ≤ n −1, and
#
# b/a = x(mod n) in other words b = ax(modn).
#============================================================================================================

def gcd(a, b):
    assert a >= 0 and b >= 0 and a + b > 0

    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return max(a, b)


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

def divide(a, b, n):
    assert n > 1 and a > 0 and gcd(n, a) == 1
    p = a if a > n else n
    q = n if a > n else a
    d, s, t = extended_gcd(p, q)
    inv = s if a > n else t
    x = b * (inv % n)
    # return the number x s.t. x = b / a (mod n) and 0 <= x <= n-1.
    return x % n

def main():
    print(divide(2, 7, 9))

if __name__ == '__main__':
    main()
