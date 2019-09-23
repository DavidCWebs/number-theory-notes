---
title: Modular Arithmetic
---
{{$page.title}}
===============
Congruence Relations
--------------------
::: tip Congruence Definition
Two numbers _a_ and _b_ are __congruent__ modulo _m_ if they have the same remainder when divided by _m_.

This is written as:

_a_ ≡ _b_ (mod _m_)
:::

* _a_ ≡ _b_ (mod _m_) iff _a_ - _b_ is divisible by _m_
* Every number _a_ is congruent modulo _m_ to all numbers _a_ + _k_ × _m_ for all integers _k_
* In particular if _r_ is a remainder of _a_ when divided by _m_, then _a_ ≡ _r_ (mod _m_)

Add Constant to Congruent Values
--------------------------------
::: tip Addition of Constant
If _a_ ≡ _b_ (mod _m_) then _a_ + _c_ ≡ _b_ + _c_ (mod _m_) for any _c_
:::

* Add the same number to two congruent values, the results will also be congruent
* Congruence of _a_ and _b_ modulo _m_ means that _m_ │ (_a_ - _b_)
* Note that (_a_ + _c_) - (_b_ + _c_) = _a_ - _b_, so it is also divisible by _m_

Addition
--------
::: tip Congruence is Preserved Under Addition
If _a_ ≡ _b_ (mod _m_) and _c_ ≡ _d_ (mod _m_), then:

_a_ + _c_ ≡ _b_ + _d_ (mod _m_)
:::

Proof:

Because _c_ ≡ _d_, adding a constant to _c_ and _d_ maintains congruence:

_a_ + _c_ ≡ _a_ + _d_

Because _a_ ≡ _b_, adding a constant to _a_ and _b_ maintains congruence:

_a_ + _d_ ≡ _b_ + _d_

Then:

_a_ + _c_ ≡ _a_ + _d_ ≡ _b_ + _d_

So:

_a_ + _c_ ≡ _b_ + _d_

Multiplication
--------------
::: tip Multiplication by a Constant
If _a_ ≡ _b_ (mod _m_) then _a_ × _c_ ≡ _b_ × _c_ (mod _m_) for any _c_
:::

* Multiply two congruent numbers by the same number, the results will also be congruent
* Congruence of _a_ and _b_ modulo _m_ means that _m_ │ (_a_ - _b_)
* Also _m_ │ _c_ × (_a_ - _b_)

Extending the previous rule:

::: tip Multiplication
If _a_ ≡ _b_ (mod _m_) and _c_ ≡ _d_ (mod _m_), then:

_a_ × _c_ ≡ _b_ × _d_ (mod _m_)
:::

Proof:

Multiply _c_ and _a_ by a constant _a_:

_a_ × _c_ ≡ _a_ × _d_

and multiply _a_ and _b_ by a constant _d_:

_a_ × _d_ ≡ _b_ × _d_

Then:

_a_ × _c_ ≡ _a_ × _d_ ≡ _b_ × _d_

So:

_a_ × _c_ ≡ _b_ × _d_



