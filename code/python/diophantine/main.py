#!/usr/bin/env python3
#
# Use extended Euclid's algorithm to solve Diophantine equations efficiently.
#
# Given three numbers a>0, b>0, and c, the algorithm should return some x and y such that
#
# ax+by=c
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
        # The deepest level - the algorithm has finished.
        # The current a is the gcd. (1, 0) are the starting 
        # values for x and y respectively.
        d, x, y = a, 1, 0
    else:
        # Run another iteration - the new a is the old b,
        # the new b is the old remainder (i.e. a % b).
        # Because this is a recursive function call, we 
        # continue to call extended_gcd() from within until
        # b == 0
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y
    return (d, x, y)

def diophantine(a, b, c):
    assert c % gcd(a, b) == 0
    d, x, y = extended_gcd(a, b)
    q = c/d
    x *= q
    y *= q
    
    
    # return (x, y) such that a * x + b * y = c
    # Solve a * x0 + b * y0 = d
    # Where d = gcd(a,b)
#    (x, y, d) = extended_euclid(a, b)
#    print((x, y, d))

    return (x, y)


def main():
#    (x, y) = diophantine(391, 299, -69)
    (x, y) = diophantine(10, 6, 14)
    print(x, y)

if __name__ == '__main__':
    main()
