/*
A Pythagorean triplet is a set of three 
natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which 
a + b + c = 1000.
Find the product abc.
*/

#include "stdio.h"
#include "math.h"

int main(){
	float katet1, katet2, hypotenus; 
	float test = 10;
	float i, j;
	float sum;

	for (i = 1; i < 1000; i++){
		for (j = i+1; j<1000;j++){
			katet1 = i;
			katet2 = j;
			//if(sqrt((i*i)+(j*j)) )
			hypotenus = sqrt((i*i) + (j*j));
			//printf("%i, %i, %i\n", katet1, katet2, hypotenus);


			if (((katet1 + katet2 + hypotenus) == 1000) && ((katet1 < katet2) && (katet2 < hypotenus))) {
				printf("%g, %g, %g\n", katet1, katet2, hypotenus);
				sum = katet1 * katet2 * hypotenus;
				printf("%f\n", sum);
			}
		}
	}
		printf("%g\n", sqrt(test));


	
return 0;
}