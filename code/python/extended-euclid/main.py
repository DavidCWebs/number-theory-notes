#!/usr/bin/env python3
iteration = 0

def detailed_extended_gcd(a, b):
    global iteration
    iteration += 1
    i = iteration
    assert a >= b and b >= 0 and a + b > 0
    print_vals(a, b, i)

    if b == 0:
        # The deepest level - the algorithm has finished.
        # The current a is the gcd. (1, 0) are the starting 
        # values for x and y respectively.
        d, x, y = a, 1, 0
#        print_vals(d, x, y, i)
    else:
        # Run another iteration - the new a is the old b,
        # the new b is the old remainder (i.e. a % b).
        # Because this is a recursive function call, we 
        # continue to call extended_gcd() from within until
        # b == 0
        (d, p, q) = detailed_extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)
#        print_vals(d, x, y, i)

    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y
    return (d, x, y)

def print_vals(a, b, i):
    print("-"*80)
    print("Iteration {}".format(i))
    print("a\tb")
    print("{}\t{}".format(a, b))
    print("-"*80)

def extended_gcd(a, b):
    assert a >= b and b >= 0 and a + b > 0

    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y
    return (d, x, y)

def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(detailed_extended_gcd(a, b))

if __name__ == '__main__':
    main()

