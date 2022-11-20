/*
2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible 
by all of the numbers from 1 to 20?
*/

#include "stdio.h"
#define LIMIT 20

int main() {
int i, j, times = 0;
i = LIMIT;
while (1){
for (j = 1; j <= LIMIT; j++){
	if ((i % j) == 0) {
		times++;
	}
	}
	if (times == LIMIT) {
		printf("%i\n", i);
		break;
	}
	times = 0;
	i++;
}
}