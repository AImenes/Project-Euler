/*
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
*/

#include "stdio.h"
#include "math.h"

void checkNumber(int number);

int main() {
	int number[200]  = {0};
	int sum = 0, mente, rest;
	int i, count = 0, count2, j = 1, k = 0, tempSum = 1, sumOfPower, sumOfFac;

	for (i = 2; i < 1000; i++){
		rest = i % 10;
		mente = i / 10;
		while (mente){
			number[j] = mente % 10;
			mente /= 10;
			j++;
		}

		number[0] = rest;
		sumOfPower = 0;

		for (count = 6; count >= 0; count--)
		{
			for (count2 = number[count]; count2 > 0; count2--)
			{
				tempSum *= count2;
				k++;
			}
			if(k == (number[count])) {
			sumOfPower += tempSum;
			tempSum = 1;
			}
			k = 0;

		}

		if (sumOfPower == i){
			printf("%i\n", i);
		}

		j = 1;
	}


	return 0;
}

void checkNumber(int number){

}