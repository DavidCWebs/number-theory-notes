#ifndef INPUT_H
#define INPUT_H

#include <stdlib.h>
#include <stdio.h>

/**
 * User input two integers, into an long array.
 * */
void inputInts(long *vars, size_t size)
{

	char *line = NULL;
	size_t len = 0;
	ssize_t lineSize = 0;
	char *inputs[] = {
		"Enter first integer: ",
		"Enter second integer: "
	};
	long tmp = 0;
	size_t i = 0;
	while (i < sizeof(inputs) / sizeof(inputs[0]) || i < size) {
		printf("%s\n", inputs[i]);
		lineSize = getline(&line, &len, stdin);
		if (lineSize == 0) {
			fprintf(stderr, "ERROR: getline failed.\n");
			exit(EXIT_FAILURE);
		}
		char *endPtr = NULL;
		tmp = strtol(line, &endPtr, 10);
		if (endPtr == line) {
			fprintf(stderr, "That doesn't contain digits...try again.\n");
			continue;
		}
		if (tmp <= 0) {
			fprintf(stderr, "%ld must be a positive integer...try again.\n", tmp);
			continue;
		}
		vars[i] = tmp;
		i++;
	}
	free(line);
}

/**
 * The largest value should be val1
 * */
void sortPair(long *val1, long *val2)
{
	if (*val2 > *val1) {
		long tmp = *val1;
		*val1 = *val2;
		*val2 = tmp;
	}
}	
#endif
