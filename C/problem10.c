/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
*/

#include "stdio.h"
#include "math.h"

int main() {
	long long int i = 2, sum = 2;
	int j, k = 1, counter;
	while (i<2000000){
		for (j = 1; j < i; j++) {
			if ((i % j) != 0) {
				counter++;
				if ((i-2) == counter){
					sum += i;
					printf("Primtallet er: %lli,  %lli\n", i, sum);
					}
				}
			}
		counter = 0;
		i++;
		}
		printf("%lli\n", sum);
	return 0;	
}

