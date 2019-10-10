---
title: Extended Euclidean Algorithm
---
Extended Euclidean Algorithm
============================
If _a_ and _b_ are positive integers, they ca n be expressed as:

```
a = (q ∙ b) + r
```
...where q is the quotient and the remainder _r_ satisfies 0 ≤ _r_ < _b_. This is known as __the division algorithm__.

In other words, you can subtract increasing multiples of _b_ from _a_ until you're left with a non-negative integer that is less than _b_.

The Euclidean algorithm determines the greatest common divisor (_gcd_) of _a_ and _b_ by iteratively using the divison algorithm to divide the largest number by the smaller, substituting the original smaller number as the larger and the remainder as the smaller at each step. When the remainder is zero, the last remainder is the _gcd_(a, b).

::: tip Euclid's Algorithm
a = bq₁ + r₁,		0 < r₁ < b,

b = r₁q₂ + r₂,		0 < r₂ < r₁,

r₁ = r₂q₃ + r₃,		0 < r₃ < r₂,

...

r<sub>j - 2</sub> = r<sub>j - 1</sub>q<sub>j</sub> + r<sub>j</sub>,		0 < r<sub>j</sub> < r<sub>j - 1</sub>

r<sub>j - 1</sub> = r<sub>j</sub>q<sub>j + 1</sub>
:::

The _gcd_(a, b) of _a_ and _b_ is r<sub>j</sub>, the last nonzero remainder in the division algorithm.

Why Does the Euclidean Algorithm Work?
--------------------------------------
We can determine the _gcd_ of two integers _a_ and _b_ by looking at the _gcd_s of subsequent remainders because:

Since the _gcd_ divides _a_ and _b_, it must divide r₁.

In the next equation, since the gcd divides _b_ and r₁, it must also divide r₂. In this way, the _gcd_ divides all the remainders, up to the last non-sero remainder r<sub>j</sub>.

Working back to the top, r<sub>j</sub> divides all remainders, and so must be the _gcd_.

::: tip Lemma
If a = (q ∙ b) + r, then

_gcd_(a, b) = _gcd_(b, r)
:::

Algorithm
----------
@TODO FINISH THIS



Given r₀, r₁

```
gcd(r₀, r₁) = s ∙ r₀ + t ∙ r₁
```

The extended Euclidean Algorithm computes the GCD as well as the linear combination of r₀ and r₁ - in particular the coefficients _s_ and _t_.

The basic idea is to compute the Euclidean Algorithm:

```
gcd(r₀, r₁) r₀ = q₁r₁ + r₂
```

Take the new remainder, and express as a multiple of r (i - 2)

Extended Euclidean Algorithm & Multiplicative Inverse
-----------------------------------------------------
The EEA can be used to determine the multiplicative inverse of a number a modulo b when the _gcd_(a, b) is 1 - in other words when Bézout's identity equals 1:

ax + by = 1

a ∙ x = 1 ± b ∙ y ≡ 1 (mod b)

This means that x is the multiplicative inverse of a (mod b). Or:

a ∙ x ≡ 1 (mod b)

This property is particularly useful, because the EEA can be used to efficiently compute the bézout coefficients for a and b.



Resources
---------
* [Article on extended Euclidean][1], Carnegie Mellon, with worked example
* [Christoph Paar video][2]
* [Worked examples, PDF][3]
* [Maths with Jay: Computing Multiplicative Inverse][4]

[1]: https://www.math.cmu.edu/~bkell/21110-2010s/extended-euclidean.html
[2]: https://www.youtube.com/watch?v=fq6SXByItUI
[3]: https://www.math.utah.edu/~fguevara/ACCESS2013/Euclid.pdf
[4]: https://www.youtube.com/watch?v=_feEMKq_Uik
