#!/usr/bin/env python3

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def compute_inverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def brute_compute_inverse(a, m):
    inv = 0
    for i in range(1, m):
        if ((i * a) % m == 1):
            inv = i
            break
    return inv


def main():
    a = int(input("Enter value: "))
    m = int(input("Enter modulo: "))
    print("The inverse of {} (mod {}) is {}".format(a, m, compute_inverse(a, m)))

if __name__ == '__main__':
    main()
