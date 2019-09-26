---
title: Prime Numbers
---
Prime Numbers
=============

Definition
----------
> A positive integer _n_ > 1 is called __prime__ if it has no positive divisors other than 1 and _n_.

Examples: `{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, ...}`

Composite Numbers
-----------------
If a number is not prime, it is known as a composite number.

Composite numbers can always be factorized into a product of two other integers which are greater than 1.

Examples:

```
4  = 2 × 2
6  = 2 × 3
8  = 2 × 4
10 = 2 × 5
etc.
```
Check if a Number is Composite/Prime
-------------------------------------
If the number _n_ is low enough, assume _a_ < _b_ and _a_ < √ _n_.

Check numbers between 2 and √ _n_ divide _n_.

```python
#!/usr/bin/env python3

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif (n % 2 == 0 or n % 3 == 0):
        return False
    elif ((n - 1) % 6 == 0 or (n + 1) % 6 == 0):
        return False
    else:
        return True

def print_factors(n):
    if n <= 1:
        print("n is less than or equal to one, therefore not prime.")
    else:
        factors = []
        for i in range(2, n):
            if (n % i == 0):
                factors.append(i)
        print("The factors of {} are:".format(n))
        print(factors)

def main():
    n = int(input("Enter an integer: "))
    if (is_prime(n)):
        print("{} is prime.".format(n))
    else:
        print("{} is not prime.".format(n))
        print_factors(n)

if __name__ == '__main__':
    main()
```


Special Cases: 1, 0
-------------------
Neither prime nor composite, 1 is considered as a special case.

From one point of view, it's only divisors are itself and one, but it is not considered prime.

Zero is also a special case: any number divides zero, because zero multiplied by any number _a_ is zero - so by definition, _a_ is a divisor of _a_, which means that zero has an infinite number of divisors. Despite this, zero is not considered either prime or composite.

Integers as Products of Primes
------------------------------
By definition, a composite number can be represented as a product of two smaller integers.

For example:
```
1001 = 7 ∙ 143
```
If one of the factors is not prime, then it can in turn be represented as a product of two even smaller integers:

```
1001 = 7 ∙ 143 = 7 ∙ 11 ∙ 13
```

The process of representing an integer as a product of smaller and smaller integers is called __Integer Factorization__.

In the above example, 7, 11 and 13 are prime numbers, so factorization of 1001 is complete at this stage.

We could start with a different representation of 1001:

```
1001 = 11 ∙ 91
91 is not prime so factoring further:
1001 = 11 ∙ 7 ∙ 13
```
Represented as a tree:

```
        1001                    1001
        /  \                    /  \
       7   143                11    91
          /   \                    /  \
        11    13                  7    13
```
Integers in the leaves give a representation of 1001 as a product of primes.

The two final representations differ only by the order of these primes. Different branches/paths, same effective result. The prime factors are the same in each case, only their orders differ.

::: tip Theorem
Every integer _n_ > 1 can be represented as a product of one or more prime numbers.
:::

Proof:

* If _n_ is prime, the theorem is satisfied
* Otherwise, _n_ = _ab_, 1 < _a_,_b_ < _n_
* If _a_ and _b_ are prime, the theorem is satisfied
* Otherwise, at least one of _a_ and _b_ is composite so can be factored:
_a_ = _a₁a₂_, 1 < _a₁_, _a₂_ < _n_
* Continue factorization while it is possible.
* It must stop as factors get smaller.

Stops when all factors are prime - if a factor is not prime, the process could continue.

Uniqueness
----------
Is the representation of numbers as prime factors unique?



