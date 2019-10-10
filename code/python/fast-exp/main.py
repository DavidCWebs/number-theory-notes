#!/usr/bin/env python3

def exponent_power_of_2(a, e_power2, mod):
    count = 0
    for i in range (0, e_power2):
        a = (a * a) % mod
        count += 1
    return (a, count)

def rec(x, n, mod):
    if n < 0:
        return rec(1 / x, -n, mod)
    if n == 0:
        return 1
    if n == 1:
        return x
    if ((n & 1) == 0):
        return rec(x * x, n / 2, mod)
    else:
        return x * rec(x * x, (n - 1) / 2, mod)

def main():
    print("Raise an integer to an exponent which is a power of 2.")
    a = int(input("Enter a: "))
    p2 = int(input("Enter power of 2: "))
    mod = int(input("Enter modulus: "))
    ans, count = exponent_power_of_2(a, p2, mod)
    print("{} ^ {} ≡ {} (mod {}). {} Iterations.".format(a, (2 ** p2), ans, mod, count))

if __name__ == '__main__':
    main()
