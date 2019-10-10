#!/usr/bin/env python3

def fastEx(b, e, m):
    e2 = 1
    while 1:
        e2 *= 2
        if e2 > e: break
        b = (b * b) % m
        print("b: {}, e2: {}".format(b, e2))
    return b, e2 / 2

def main():
    b = int(input("Enter b: "))
    e = int(input("Enter e: "))
    m = int(input("Enter m: "))
    
    r, e2 = fastEx(b, e, m)
    while 1:
        if e2 >= e: break
        s, t = fastEx(b, e - e2, m)
        r *= s
        e2 += t
    r %= m
    print(r)


if __name__ == '__main__':
    main()
