#!/usr/bin/env python3

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def squares(n, m):
    d = gcd(n, m)
    return (n / d) * (m / d)


def main():
    n = int(input("Enter Length: "))
    m = int(input("Enter Width: "))
    print(squares(n, m))

if __name__ == '__main__':
    main()
