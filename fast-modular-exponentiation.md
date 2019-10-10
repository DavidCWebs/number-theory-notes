---
title: Fast Modular Exponentiation
---
Fast Modular Exponentiation
===========================
* Central operation in public key cryptography
* Required for fast encryption/decryption
* Easy in one direction, hard in reverse

Modular exponentiation is the operation of computing _b_ to the power _e_ (mod _m_).

_c_ ← _b_<sup>e</sup> (mod _m_)

To get the remainder, it is not necessary to compute _b_<sup>e</sup>, which is a potentially enormous number if _e_ is large.

Because multiplication (mod _m_) maintains congruence (mod _m_), the result modulo _m_ at each step can be multiplied together. In this way, much smaller numbers are multiplied, saving computational resources.

### Example: 3⁵ (mod 5)
3² = 3 ∙ 3  = 9	≡ 4 (mod 5)

3³ = 3² ∙ 3 = 4 ∙ 3 = 12 ≡ 2 (mod 5)

3⁴ = 3³ ∙ 3 = 2 ∙ 3 = 6	≡ 1 (mod 5)

3⁵ = 3⁴ ∙ 3 = 1 ∙ 3 = 3	≡ 3 (mod 5)

Note that 3 ∙ 3 ∙ 3 ∙ 3 ∙ 3 = 243 ≡ 3 (mod 5)

::: tip Naive Algorithm
For _c_ ← _b_<sup>e</sup> (mod _m_)

Start with 1, multiply by _b_, take the result mod(_m_), repeat _e_ times.

In other words:
1. Start with _c_ ← 1
2. Repeat _e_ times: _c_ ← _c_ ∙ _b_ mod _m_
:::

However, for an exponent _e_, _e_ multiplications are required. For sufficiently large values of _b_, _e_ and _m_, such as when each number consist of thousands of digits the computation is too inefficient.

Exponent is a Power of Two
--------------------------
If _c_ ← _b_<sup>e</sup> (mod _m_) and 

_e_ = 2<sup>k</sup>

We can compute _c_ using the "squares" method - this allows for fast computation of large positive integer powers of a number.

For example, a⁸, can be represented as ((a²)²)².

If you calculate a⁸ naively:

a⁸ = _a_ ∙ _a_ ∙ _a_ ∙ _a_ ∙ _a_ ∙ _a_ ∙ _a_ ∙ _a_

...7 multiplications are required (the exponent - 1).

Alternatively, computing `a⁸` as `((a²)²)²` requires three multiplications.

In this way, `aⁿ` requires no more than 2 log₂(_e_) multiplications, where _e_ is the exponent.

### Example Code: Exponent is a Power of 2
```python
#!/usr/bin/env python3

def exponent_power_of_2(a, e_power2, mod):
    count = 0
    for i in range (0, e_power2):
        a = (a * a) % mod
        count += 1
    return (a, count)

def main():
    print("Raise an integer to an exponent which is a power of 2.")
    a = int(input("Enter a: "))
    p2 = int(input("Enter power of 2: "))
    mod = int(input("Enter modulus: "))
    ans, count = exponent_power_of_2(a, p2, mod)
    print("{} ^ {} ≡ {} (mod {}). {} Iterations.".format(a, (2 ** p2), ans, mod, count))

if __name__ == '__main__':
    main()
```

### Example: Exponent Not Necessarily Power of 2
```python
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
```
Source: [Applied Cryptography, Udacity][2]

Resources
---------
* [Wikipedia, Exponentiation by Squaring][1]
* [Dave Evans, Applied Cryptography, Udacity][2]

[1]: https://en.wikipedia.org/wiki/Exponentiation_by_squaring
[2]: https://www.youtube.com/watch?v=vFkXvo-Y2DE


