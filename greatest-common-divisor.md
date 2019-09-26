---
title: Greatest Common Divisor
---
Greatest Common Divisor
=======================
The Greatest Common Divisor (GCD) of _a_ and _b_ where _a_ and _b_ are integers that are not equal to zero is the largest number that divides both _a_ and _b_.

::: tip Definition
The __greatest common divisor__, gcd(_a_, _b_) of the non-zero integers _a_ and _b_ is the largest integer that divides both _a_ and _b_
:::

By convention, it is assumed that _a_ and _b_ are non-negative.

Applications
------------
### Computing Inverses
Given integers _a_ and _n_, find integer _k_ such that:

_ak_ ≡ 1 mod _n_

This is a basic primitive in modern crypto protocols.

### Computing Fractions
Fractions can be simplified using greatest common divisors (used by the `fraction` library in Python.

Naive Algorithm
---------------
Find the greatest common divisor by trying all possible numbers and selecting the largest.

```python
def naive_gcd(a, b):
  assert a > 0 and b > 0 and a + b > 0
  
  if a == 0 or b == 0:
    return max(a, b)
  
  # Range backwards from the smaller of a and b,
  # stopping at 1.
  for d in range(min(a, b), 0, -1):
    if a % d == 0 and b % d == 0:
      return d

```

This has severe efficiency limits as the numbers become large.

For example, if _a_ and _b_ consist of hundreds of digits (typical in the case of cryptographic protocols) -  a supercomputer with a quadrillion operations per second might take a thousand years to compute a result using this algorithm.

Euclidean Algorithm
-------------------
If _a_ and _b_ are integers such that _a_ ≥ _b_ > 0, the greatest common divisor can be found by:

1. Applying the division algorithm: _a_ = _bq_ + _r_, 0 ≤ _r_ < _b_
2. Set _a_ to be the previous _b_ and _b_ to be the previous _r_
3. Repeat until _r_ = 0
4. The last non-zero remainder id the greatest common divisor of _a_ and _b_.

This works because the final gcd must divide all intermediate remainders. The algorithm keeps reducing the complexity of the problem until a solution is found.

To compute the greatest common divisor of _a_ and _b_, we make a recursive call that computes the greatest common divisor of _b_ and _a_ mod _b_ (the remainder of _a_ divided by _b_).


::: tip Lemma
_d_ divides _a_ and _b_ if and only if _d_ divides _a_ - _b_ and _b_.

If _a_ = _bq_ + _r_, then gcd(_a_, _b_) = gcd(_b_, _r_)
:::



::: tip Proof 2
Show that if _a_ = _bq_ + _r_, then an integer _d_ is a common divisor of _a_ and _b_ iff _d_ is a common divisor of _b_ and _r_.

Let _d_ be a common divisor of _a_ and _b_. It follows that _d_ │ _a_ and _d_ │ _b_. Therefore _d_ │ (_a_ - _bq_).

Because _r_ = _a_ - _bq_, _d_ │ _r_.

This proves that _d_ is a common divisor of _b_ and _r_.

If _d_ is a common divisor of _b_ and _r_, then _d_ │ _b_ and _d_ │ _r_. Thus _d_ │ (_bq_ + _r_), so _d_ │ _a_.

The set of common divisors of _a_ and _b_ are the same as the set of common divisors of _b_ and _r_.

If _d_ is the greatest common divisor of _b_ and _r_, then it must be the greatest common divisor of _a_ and _b_.

Reference: [Florida State University Course Notes, Discrete Mathematics I][1]
::: 
 

Extended Euclidean Algorithm
----------------------------
Once GCD has been determined for numbers _a_ and _b_ by means of the Euclidean Algorithm, we may need to determine _x_ and _y_ where:

_ax_ + _by_ = gcd(_a_, _b_)

gcd(_a_, _b_) = _d_

Check that _d_ divides both _a_ and _b_, but this just demonstrates that _d_ is a common divisor of _a_ and _b_ - it does not guarantee that it is the __greatest__ common divisor. We have not excluded the possibility that a larger common divisor exists.

::: tip Lemma
If _d_ divides _a_ and _b_ and:

_d_ = _ax_ + _by_ for integers _x_ and _y_, then:

_d_ = gcd(_a_, _b_)
:::

In a sense, in this case _x_ and _y_ certify that _d_ is the greatest common divisor of _a_ and _b_.

::: tip Proof
* _d_ is a common divisor of _a_ and _b_, hence _d_ ≤ gcd(_a_, _b_)
* If a number _d_ divides _a_ and _b_, it also divides _a_ + _b_
* If a number _d_ divides _a_, it also divides _k_ × _a_, where _k_ is an integer
* gcd(_a_, _b_) divides both _a_ and _b_, hence it also divides _ax_ + _by_
* No number larger than _d_ can divide _d_
:::

References & Resources
----------------------
* [Euclidean Algorithm][1], FSU Course Notes, Discrete Mathematics
* [Extended Euclidean Algorithm][2], TODO include review of this, good description
* [Khan academy, Euclidean Algorithm][3]
* [Blog post with worked example][4]

[1]: https://www.math.fsu.edu/~pkirby/mad2104/SlideShow/s5_2.pdf
[2]: https://www.math.cmu.edu/~bkell/21110-2010s/extended-euclidean.html
[3]: https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
[4]: https://forthright48.com/extended-euclidean-algorithm/
