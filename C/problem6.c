/*
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the
 squares of the first ten natural numbers 
 and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of 
the squares of the first one hundred
 natural numbers and the square of the sum.
*/

#include "stdio.h"
#include "math.h"

int main() {
double sumOfSquares, sumSquared;
int i, n = 0, m;

for (i = 0; i <= 100; i++){
	n += i;
	sumOfSquares += (pow(i, 2));
}

sumSquared = pow(n, 2);
printf("sumSquared: %g, n = %i\nsumOfSquares: %g\n", sumSquared, n, sumOfSquares);
m = sumSquared - sumOfSquares;
printf("%i", m);

return 0;
}