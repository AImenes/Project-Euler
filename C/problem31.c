/*
In England the currency is made up of pound, £, and pence, p, and 
there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
*/

// a1P + b2P + c5P + d10P + e50P + f100P +g200P = 200

#include "stdio.h"
#define POUNDS 200

int main() {
	int a, b, c, d, e, f, g;
	int array[7] = {200, 100, 50, 10, 5, 2, 1};
	int kombinasjoner = 0, sum, factor;
	int i = 0, j;

	for (i = 0; i<7; i++){
		sum = array[i];
		if(sum  == POUNDS) kombinasjoner++;
		while(sum != POUNDS){
			factor = POUNDS / array[i];
			
		}
	}





	return 0;
}



