#!/usr/bin/env python3

def fast_ex(b, e, m):
    e2 = 1
    while 1:
        e2 *= 2
        if e2 > e: break
        b = (b * b) % m
    return b, e2 / 2

def compute_modular_exponent(b, e, m):
    r, e2 = fast_ex(b, e, m)
    while 1:
        if e2 >= e: break
        s, t = fast_ex(b, e - e2, m)
        r *= s
        e2 += t
    return r % m

def main():
    b = int(input("Enter b: "))
    e = int(input("Enter e: "))
    m = int(input("Enter m: "))
    
    print(compute_modular_exponent(b, e, m))


if __name__ == '__main__':
    main()
