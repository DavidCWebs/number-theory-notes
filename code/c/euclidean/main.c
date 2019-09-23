#include <stdio.h>
#include "input.h"

/**
 * Compute the Greatest Common Divisor of two longegers.
 *
 * It is expected that a > b, and that a and b are positive longegers.
 *
 * */
long gcd(long a, long b)
{
	if (b == 0) {
		return a;
	} else {
		return gcd(b, a % b);
	}
}


int main()
{
	long vars[2];
	inputInts(vars, 2);
	sortPair(&vars[0], &vars[1]);
	long res = gcd(vars[0], vars[1]);
	printf("The GCD of %ld and %ld is %ld\n", vars[0], vars[1], res);
	return 0;
}
