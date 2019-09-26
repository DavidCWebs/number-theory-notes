---
title: Unique Factorization
---
Unique Factorization
====================

::: tip Theorem
Every integer _n_ > 1 can be represented as a product of one or more prime numbers.

Any such two representations of the same integer _n_ can differ only by the order of factors.
:::

::: tip Lemma
Integers _m_ and _m_ are called __coprime__ if gcd(_m_, _n_) = 1
:::

Computing GCD is much easier than prime factorization. The former can be computed with Euclid's algorithm, whereas there is no known efficient algorithm for the latter.

Least Common Multiple
---------------------
This is computed for _m_ and _n_ using Euclid's algorithm:

lcm(_m_, _n_) = (_mn_) / gcd(_m_, _n_)

::: tip Lemma
If two coprime numbers divide _n_, then their product also divides _n_.

If _a_ │ _n_, _b_ │ _n_ and gcd(_a_, _b_) = 1 then _ab_ │ _n_.
:::

Divisibility
------------
::: tip Lemma
If  all prime factors of number _a_ are among the prime factors of number _b_, and their degrees are equal or smaller, then _a_ │ _b_.
:::

For example:

105 = 3 ∙ 5 ∙ 7 divides 1260 = 2² ∙ 3² ∙ 5 ∙ 7


Coprime
-------
::: tip Lemma
Two numbers are coprime if their gcd is 1.

If two numbers share no prime factors, they are coprime.
:::

For example:

6 = 2 ∙ 3 and 35 = 5 ∙ 7. Because they do not share prime factors, they are coprime.

Easy criterion for divisibility given prime factorization - Coprime numbers don’t share prime factors

If two numbers are coprime and they divide _n_, their product also divides _n_.

Greatest Common Divisor
-----------------------
::: tip Lemma
The greatest common divisor of two numbers is the product of their common unique factors.
:::

For example:

The gcd(1980, 1848) is given by:

1980 = 2² ∙ 3² ∙ 5 ∙ 11
1848 = 2³ ∙ 3 ∙ 7 ∙ 11

gcd(1980, 1848) = 2² ∙ 3¹ ∙ 11¹

Note that in this case 2 and 3 are raised to the minimum of the power found in the unique factors:
common factor ^ min(power1, power1)

Least Common Multiple
---------------------
::: tip Lemma
The LCM of _a_ and _b_ is computed by: _ab_/gcd(_a_, _b_)
:::


