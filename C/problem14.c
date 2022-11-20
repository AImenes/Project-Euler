/*The following iterative sequence is defined for the set of
 positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate 
the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this 
sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

3  10  5  16  8  4  2  1  
9 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1

NOTE: Once the chain starts the terms are allowed to go above one million.
*/
#include "stdio.h"
#include "math.h"

int main(){
	long long int startingNumber, chainLength = 1, i, j, counter= 2, highestChain = 0, highestNumber;

	while (counter < 1000000){
		startingNumber = counter;

		start:
		if((startingNumber%2) != 0) {
		startingNumber = (3 * startingNumber) + 1;
		chainLength++;
		}

		while ((startingNumber%2) == 0){
		startingNumber = startingNumber / 2;
		chainLength++;
		}
		if ((startingNumber != 1) && (startingNumber%2 != 0)) goto start;
	
		if(chainLength > highestChain){
			highestChain = chainLength;
			highestNumber = counter;
		}

	chainLength = 1;
	counter++;
	}

	printf("%lli - %lli\n", highestNumber, highestChain);

	return 0;
}
