#ifndef INTEGER_INPUT_H
#define INTEGER_INPUT_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

#define MAX_DIGITS 12

/**
 * This function removes surplus characters from the input buffer.
 * Otherwise, if more than the permitted number of characters have been entered during the
 * call to fgets(), the surplus characters (after MAX_DIGITS chars) remain in the input buffer
 * and will be wrongly accepted as input on the next iteration of the loop.
 * */
static inline void ClearInputBuffer() 
{
	char c = 0;
	// Loop over input buffer and consume chars until buffer is empty
	while ((c = getchar()) != '\n' && c != EOF);
}

void getIntegerFromStdin(int *inputInteger)
{
	char *inputBuffer = malloc(sizeof(char) * MAX_DIGITS);
	memset(inputBuffer, 0, MAX_DIGITS);
	char *input = NULL;
	while (input == NULL) {
		// Note that fgets returns inputBuffer on success.
		// This becomes important when freeing - free either `input` or
		// `inputBuffer` to avoid an attempted double-free error.
		input = fgets(inputBuffer, MAX_DIGITS, stdin);
		
		// If fgets() receives less than MAX_DIGITS, the last char in the array is '\n'.
		// Therefore if the last char is not '\n', too many characters were entered.
		if (inputBuffer[strlen(inputBuffer) - 1] != '\n') {
			fprintf(stderr, "[ERROR]: Too many characters: max input is %d chars.\n", MAX_DIGITS);
			ClearInputBuffer();
			input = NULL;
			continue;
		}

		// Check that the input can be intepreted as an integer

		// Convert to integer using `strtol()`
		errno = 0;
		char *endptr = NULL;
		*inputInteger = strtol(input, &endptr, 10);
		if (input == endptr) {
			// Remove trailing newline by adding NUL at the index of the
			// terminating '\n' character. See man strcspn - this function
			// gets the length of a prefix substring.
			input[strcspn(input, "\n")] = 0;
			printf("Invalid input: no integer found in %s.\n", input);
			input = NULL;
		}
		if (errno != 0) {
			fprintf(stderr, "[ERROR]: That doesn't look like an integer.\n");
			input = NULL;
		}
	}
	free(inputBuffer);
}

/**
 * Alternative example using `scanf()` with some crude checking
 *
 * */

int getIntScanf(int maxDigits)
{
	char check1[maxDigits], check2[maxDigits];
	int input;
	do {
		puts("Enter int: ");
		// Save stdin into a char array `check1`
		scanf(" %s", check1);
		// Convert to an int
		input = strtol(check1, NULL, 10);
		// For checking purposes, convert the saved int into a string
		sprintf(check2, "%d", input);
	// Loop while the string from the int doesn't match the input,
	// or if input is not greater than 0
	} while (!(strcmp(check1, check2) == 0 && 0 < input));
	return input;
}

/**
 * Simple example using `fgets()` and `strtol()` with minimal feedback
 * and error checking.
 *
 * Writes to an integer pointer rather than returning an int.
 * */
void simpleInt(int *inputInteger)
{
	char *p;
	char s[MAX_DIGITS];
	while (fgets(s, MAX_DIGITS, stdin)) {
		*inputInteger = strtol(s, &p, 10);
		if (p == s || *p != '\n') {
			// Error reporting here is not granular. Either the input
			// could not be interpreted as an integer by `strtol()`
			// or the input was too long.
			printf("Enter an int: ");
		} else break;
	}
	// Remove trailing newline
//	*(inputInteger + strcspn(s, "\n")) = 0;
}

#endif
