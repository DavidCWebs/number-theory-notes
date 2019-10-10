---
title: Modular Division
---
Modular Division
================

Modular Inverse
---------------
A number multiplied by it's inverse equals 1. For example, The inverse of 5 is 1/5 because 5 ∙ (1 / 5) = 1

All real numbers other than zero have an inverse.

Multiplying a number by the inverse of A is equivalent to dividing by A.

In modular arithmetic, there is no division operation. There are, however, modular inverses.

The modular inverse of a number N (mod m) is the number which when multiplied by N results in 1 (mod m).

Only numbers coprime to the modulus have a modular inverse in that modulus.

Naive Solution
--------------
To find the modular inverse of _a_ (mod _m_):

1. Calculate _a_ ∙ _b_ (mod _m_) for _b_ values in the range [0, _m_).
2. The modular inverse of _a_ mod _m_ is the number such that _a_ ∙ _b_ ≡ 1

Example:
Find the modular inverse of 5 (mod 7):

| b in range [0, m)	| 0	| 1	| 2	| 3	| 4	| 5	| 6	|
| ---			| ---	| ---	| ---	| ---	| ---	| ---	| ---	|
| b ∙ 5 (mod 7)		| 0	| 5	| 3	| 1	| 6	| 4	| 2	|

This shows that 3 ∙ 5 ≡ 1 (mod 7).

This means that 3 is the multiplicative inverse of 5 (mod 7)			

References & Resources
----------------------

* [Khan Academy on Modular Inverses][1]

[1]: https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/modular-inverses

