/*
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
*/

#include "stdio.h"

int main(){
	long long int i, j, sumOfFact, fact = 1, rest, mente, lagtSammen = 0;

	for (i = 3; i < 100000000; i++)
	{
		rest = i%10;
		mente = i/10;

		for (j = rest; j > 0; j--)
		{
			fact *= j;
		}
		sumOfFact = fact;
		fact = 1;

		while(mente){
			rest = mente % 10;
			for (j = rest; j > 0; j--)
			{
				fact *= j;
			}
			mente /= 10;
			sumOfFact += fact;
			fact = 1;
		}

		fact = 1;
		if (i == sumOfFact)
		{
			printf("%lli\n", i);
			lagtSammen += i;
		}
		//printf("%i - %i\n", i, sumOfFact);
	}
	printf("\n%lli\n", lagtSammen);

	return 0;
}