#!/usr/bin/env python3

def square(x): return x * x
def mod_exp(x, n, mod):
    if n == 0: return 1
    if (n % 2 == 0):
        return square(mod_exp(x, n / 2, mod)) % mod
    else:
        return (x * mod_exp(x, n - 1, mod)) % mod

def main():
    print("Raise an integer to an exponent.")
    a = int(input("Enter a: "))
    e = int(input("Enter exponent: "))
    mod = int(input("Enter modulus: "))
    ans = mod_exp(a, e, mod)
    print("{} ^ {} ≡ {} (mod {}).".format(a, e, ans, mod))

if __name__ == '__main__':
    main()
