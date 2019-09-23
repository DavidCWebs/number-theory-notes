---
title: Divisibility
---
Divisibility
============
Division is not always possible with integers.

We need to identify the cases for which division is possible.

What do we mean when we say _a_ is divisible by _b_?

Naive answer:

For a rational number _a/b_,  if the number is an integer, then _a_ is divisible by _b_.

Not a good definition, since it is dependent upon a more complex notion, that of _rational numbers_.

Definition
----------
What does it mean if _a/b_ is an integer?

It means that the denominator cancels out.

_a_ can be represented as a product of two integers: _b_ and some other integer _k_:

```
a = b × k
```
Also:

```
a/b = (b × k)/b = k
```

__The number _a/b_ is an integer if _a_ can be represented as a product of two integers: _b_ and some other integer.__

This definition is better because it is simpler - it only relies on the notion of _product_.

### TLDR; Divisibility Definition
_a_ is divisible by _b_ (or _b_ divides _a_) denoted by _b_ │ _a_ if there is an integer _k_ such that _a_ = _k_ × _b_.

If _b_ does not divide _a_ it is denoted by _b_ ∤ _a_

### Lemma
If _c_ divides _a_ and _c_ divides _b_, then _c_ divides _a_ ± _b_

Since _c_ divides _a_ and _c_ divides _b_, then:

_a_ = _c_ × _k₁_ and
_b_ = _c_ × _k₂_

Then:
_a_ ± _b_ = _c_ × _k₁_ ± _c_ × _k₂_ = _c_ × (_k₁_ ± _k₂_) 

This means that _a_ ± _b_ is divisible by _c_.

### Example
Suppose:

_b_ │ _a_

(b divides a)

Is it true that _b_ │ 3 × _a_?

Yes: _a_ = _b_ × _k_ for some integer _k_.

For 3 × _a_ = 3(_b_ × _k_) = 3 × _b_ × _k_ = _b_ × 3 _k_

...so 3 _a_ satisfies the defintion of divisibility by _b_:

_b_ │ 3 _a_

More generally:

### Lemma
If _b_ │ _a_, then for any integer _c_ we have _b_ │ (_a_ × _c_) 

Divisibility by Zero
--------------------
Not forbidden by number theory. Zero (unlike any other integer number) is divisible by zero.

0 = 0 × _k_, where _k_ can be any integer number.

