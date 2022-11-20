/*
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
*/

#include "stdio.h"
#include "math.h"

void checkNumber(int number);

int main() {
	int number[200]  = {0};
	int sum = 0, mente, rest;
	int i, count = 0, j = 1, sumOfPower;

	for (i = 2; i < 10000000; i++){
		rest = i % 10;
		mente = i / 10;
		while (mente){
			number[j] = mente % 10;
			mente /= 10;
			j++;
		}
		number[0] = rest;

		/*for (count = 6; count >= 0; count--)
		{
			printf("%i,", number[count]);
		}*/


		sumOfPower = (number[0] * number[0] * number[0] * number[0] * number[0]) + (number[1] * number[1] * number[1] * number[1] * number[1]) + (number[2] * number[2] * number[2] * number[2] * number[2]) + (number[3] * number[3] * number[3] * number[3] * number[3]) + (number[4] * number[4] * number[4] * number[4] * number[4]) + (number[5] * number[5] * number[5] * number[5] * number[5]);

		if (i == sumOfPower){
			printf("\n\n%i\n\n", i);
			sum += i;
		}

		j = 1;
	}
	printf("%i\n", sum);


	return 0;
}

void checkNumber(int number){

}