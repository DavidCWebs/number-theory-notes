---
title: Division with Remainders
---
{{$page.title}}
===============
Division over integers is not always possible.

::: tip Definition
Suppose _b_ is a positive integer. The result of the division of _a_ by _b_ with a remainder is a pair of integers, **quotient** _q_ and **remainder** _r_ such that:

_a_ = _q_ × _b_ + _r_

and 0 ≤ _r_ < _b_
::: 

If _r_ = 0, then _b_ divides _a_.

::: tip Lemma
Integers _a₁_ and _a₂_ have the same remainder when divided by _b_ iff _a₁_ - _a₂_ is divisible by _b_
:::

Division By 10
--------------
::: tip Lemma
Suppose we divide _a_ by 10 with a remainder. The remainder is the last digit of _a_ and the quotient is the number formed by all digits of _a_ except the last one.
:::

::: tip Corollary
An integer _a_ is divisible by 10 iff it's last digit is 0.
:::

* 10 │ _a_ iff the remainder is 0
* The remainder is the last digit

Divisibility by 5
-----------------
::: tip Lemma
An integer _a_ is divisible by 5 iff it's last digit is 0 or 5
:::

Divisibility by 2
-----------------
::: tip Lemma
An integer _a_ is divisible by 2 iff it's last digit is 0, 2, 4, 6 or 8
:::

Divisibility by 3
-----------------
::: tip Lemma
An integer is divisible by 3 if the sum of the digits is divisible by 3.
:::

Divisibility by 6
-----------------
::: tip Lemma
The prime factors of 6 are 2 and 3, so a number that is divisible by 6 must be divisible by two (it must be even) and three:

A number is divisible by 6 if:

* It's last digit is 0, 2, 4, 6 or 8 AND
* The sum of digits is divisible by 3
:::
