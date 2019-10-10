---
title: Chinese Remainder Theorem
---
Chinese Remainder Theorem
=========================

::: tip Theorem
If gcd(_a_, _x_) = 1, then for any remainder rₐ modulo a and any remainder rₓ modulo x there exists integer n such that n ≡ rₐ (mod a) and n ≡ rₓ (mod x). if n₁ and n₂ are two such integers, then n₁ ≡ n₂ (mod ab)
:::

In other words:

Consider all _ab_ remainders modulo _ab_:

0, 1, 2, ... ab - 1

Every such remainder _r_ corresponds to a pair of remainders (_ra_, _rb_):

_r_ ≡ _ra_ mod _a_, r ≡ _rb_ mod _b_

Claim: if we consider pairs corresponding to each _r_, then each of the possible _ab_ pairs (_ra_, _rb_) appears exactly once.

Algorithm
---------



Intuition
---------
Many congruence problems can be reduced in such a way that the Chinese Remainder Theorem can be used.

### System of Linear Congruences

Consider any linear congruence _ax_ ≡ _b_ (mod _N_)

In general:

* Let _N_ be factored into _p_, _q_, _r_ ..., all relatively prime.
* _ax_ ≡ _b_ (mod _N_) can then be reduced to a system of simultaneous congruences mod _p_, _q_, _r_ ....
* These can be solved with Chinese remainder problem algorithm.

### Example
Find a sysyem of simultaneous congruences whose solutions also solve 3x ≡ 7 (mod 40).

1. Convert the congruence to an equation:

3x ≡ 7 (mod 40) → 3x = 40k + 7

2. Look for factors of 40 which are coprime - in this case 5 and 8. This leads to:

3x = 5 ∙ (8 ∙ k) + 7 → 3x ≡ 7 ≡ 2 (mod 5)

and:

3x = 8 ∙ (5 ∙ k) + 7 → 3x ≡ 7 (mod 8)

3. We now have a set of simultaneous congruences:

3x ≡ 2 (mod 5)

and

3x ≡ 7 (mod 8)

4. Use multiplicative inverse in the relevant modulus to solve each congruence for x:

Because 3 ∙ 3 = 1 mod 8, x ≡ 21 ≡ 5 (mod 8)

Because 3 ∙ 2 = 1 mod 5, x ≡ 4 (mod 5)

Summary:

x ≡ 5 (mod 8)

x ≡ 4 (mod 5)

5. CRT involves finding something which is congruent to 1 with respect to one modulus, and zero with respect to the product of the other moduli.

In this case, we first look for a number congruent to 1 (mod 8) and 0 (mod 5), so we look among multiples of 5 for a number which is one more than a multiple of 8. This process is then repeated for the other moduli - look amongst multiples of 8 for a number which is one more than a multiple of 5.

25 ≡ 1 (mod 8) AND 25 ≡ 0 (mod5)

16 ≡ 1 (mod 5) AND 16 ≡ 0 (mod 8)

6. Get the congruence relationship for x mod 8 and x mod 5.

From:

x ≡ 5 (mod 8)

x ≡ 4 (mod 5)

and: 

25 ≡ 1 (mod 8) AND 25 ≡ 0 (mod5)

16 ≡ 1 (mod 5) AND 16 ≡ 0 (mod 8)

Because multiplication by an integer does not affect congruence in a given modulus, we can multiply 25 (mod 8) by 5 to get a number that is 5 (mod 8) but is still 0 (mod 5):

Get the congruence of 5 (mod 8), such that congruence mod 5 is zero:
125 ≡ 5 (mod 8) AND 125 ≡ 0 (mod5)

Similarly, we can get the congruence of 4 (mod 5), such that the congruence mod 8 is zero:
64 ≡ 4 (mod 5) AND 64 ≡ 0 (mod 8)

If we add these numbers, neither of the congruences will be changed. This provides a solution for both congruences:

125 + 64 = 189

189 ≡ 5 (mod 8)

189 ≡ 4 (mod 5)

The smallest solution is the remainder modulo (5 ∙ 8):

189 = 40 ∙ 4 + 29

Which means the answer for this example is 29.


>The basic intuition behind the Chinese Remainder Theorem is this: If you’ve found one solution to x ≡ a mod p, then you can add p and still have a solution.
>
>Consider the system of congruences x ≡ 5 mod 7, x ≡ 4 mod 11, and x ≡ 4 mod 8.
>
>The first congruence has solution x = 5. But (since it’s a congruence mod 7), it will also have solutions x = 12, 19, 26, 33, and so on.
>
>Look among these for a solution to the second congruence: we see x = 26 solves the first and second congruences.
>
>To keep this as a solution, we need to add multiples of 7 × 11 = 77 : 7, because adding a multiple of 7 won’t undo our solution to the first congruence; and 11, for the same reason.
>
>So solutions to the first two congruences are x = 26, 103, 180, and so on. We keep going until we find a solution to the third congruence: x = 180 solves the third congruence and, because of the way we’ve constructed it, it will also solve the other two.
>
>Jeff Suzuki, Mathematician and teacher of mathematics (20+ years).
>
>[Quora answer][1]

Resources
---------
* [Very good video explanation][3], Jeff Suzuki
* [Wikipedia, CRT][4]

[1]: https://www.quora.com/How-can-I-understand-the-Chinese-remainder-theorem-What-are-some-examples
[2]: https://www.youtube.com/watch?v=TnJPNRxu8mM
[3]: https://www.youtube.com/watch?v=oKMYNKbFHBE
[4]: https://en.wikipedia.org/wiki/Chinese_remainder_theorem
