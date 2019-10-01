#!/usr/bin/env python3

from compute_inverse import *

def ChineseRemainderTheorem(n1, r1, n2, r2):
    # Are n1 and n2 coprime?

    x1 = r1*n2*compute_inverse(n2, n1)
    x2 = r2*n1*compute_inverse(n1, n2)
    x = x1 + x2
#    while (x > (n1 * n2)):
#        x -= n1 * n2
    return x % (n1 * n2)


def main():
    n1 = int(input("Enter n1: "))
    r1 = int(input("Enter r1: "))
    n2 = int(input("Enter n2: "))
    r2 = int(input("Enter r2: "))
    result = ChineseRemainderTheorem(n1, r1, n2, r2)
    print(result)

if __name__ == '__main__':
    main()
