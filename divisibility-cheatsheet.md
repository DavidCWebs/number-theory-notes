---
title: Divisibility Cheatsheet
---
{{$page.title}}
===============

__The number _a/b_ is an integer if _a_ can be represented as a product of two integers: _b_ and some other integer.__

Divisibility Definition
-----------------------
_a_ is divisible by _b_ (or _b_ divides _a_) denoted by _b_ │ _a_ if there is an integer _k_ such that _a_ = _k_ × _b_.

If _b_ does not divide _a_ this is denoted by _b_ ∤ _a_

::: tip Lemma
If _c_ divides _a_ and _c_ divides _b_, then _c_ divides _a_ ± _b_

_a_ ± _b_ = _c_ × (_k₁_ ± _k₂_)

where _k₁_ and _k₂_ are integers that are divisors of _a_/_c_ and _b_/_c_ respectively.
:::

Proof:
Since _c_ divides _a_ and _c_ divides _b_, then:

_a_ = _c_ × _k₁_ and
_b_ = _c_ × _k₂_

Then:
_a_ ± _b_ = _c_ × _k₁_ ± _c_ × _k₂_ = _c_ × (_k₁_ ± _k₂_) 

This means that _a_ ± _b_ is divisible by _c_.

::: tip Lemma
If _b_ │ _a_, then for any integer _c_ we have _b_ │ (_a_ × _c_) 
:::

