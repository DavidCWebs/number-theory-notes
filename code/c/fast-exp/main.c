#include <stdio.h>
#include "integer-input.h"

int square (int x)
{
	return x * x;
}

int fastModExp(int a, int n, int m)
{
	if (n == 0)
		return 1;
	if (n & 1) {
		return (a * fastModExp(a, n - 1, m)) % m;
	} else {
		return square(fastModExp(a, n / 2, m)) % m;
	}
}

int main()
{
	int a, n, m, res;

	printf("Fast exponentiation for aⁿ (mod m)\n");
	puts("Enter a:");
	getIntegerFromStdin(&a);
	puts("Enter exponent n:");
	getIntegerFromStdin(&n);
	puts("Enter modulus m:");
	getIntegerFromStdin(&m);
	printf("Computing %d ^ %d (mod %d)...\n", a, n, m);

	res = fastModExp(a, n, m);
	printf("result: %d\n", res);
	
	return 0;
}
