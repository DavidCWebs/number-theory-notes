#!/usr/bin/env python3

def fastModularExp(b, k, m):
    for i in range(0, k):
        b = (b * b) % m
    return b

def fastGen(b, e, m):
    b = b % m
    r = 1
    while e > 0:
        if (e % 2 == 1):
            r = (r * b) % m
        e >>= 1
        b = (b * b) % m
    return r

def main():
    b = int(input("Enter b: "))
    k = int(input("Enter k: "))
    e = int(input("Enter e: "))
    m = int(input("Enter m: "))

    print(fastModularExp(b, k, m))
    print(fastGen(b, e, m))

if __name__ == '__main__':
    main()
