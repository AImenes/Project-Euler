/*
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
 we can see that the 6th prime is 13.

What is the 10 001st prime number?
*/

#include "stdio.h"
#include "math.h"

int main() {
	long long int i = 2;
	int j, k = 1, counter;
	while (1){
		for (j = 2; j < i; j++) {
			if ((i % j) != 0) {
				counter++;
				if ((i-2) == counter){
					k++;
					printf("k: %i\n", k);
					if (k == 10001) {
						printf("%lli\n", i);
						break;
					}
				}
			}
		}
		counter = 0;
	i++;
}

return 0;
}