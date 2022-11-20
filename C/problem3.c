/*
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
*/

#include "stdio.h"

int main(){
	long long int testNumber = 600851475143;
	//int testNumber = 13195;
	int i,k, j = 0, candi[15] = {0}, prime[15] = {0}, complete[15] = {0};
	//printf("%lli\n", number);

	for (i = 2; i<testNumber; i++){
		if (testNumber%i == 0){
			candi[j] = testNumber/i;
			prime[j] = i;
			printf("%i, %i, ", candi[j],prime[j]);
			k = 1;
			while ((k<j)&&(j>0)){ 
				if ((i % prime[j-k]) == 0){
					complete[j] = i;
				}
				k++;
			}
			printf("  %i\n", complete[j]);
			j++;
		}
	}

	for (i = 0; i<15; i++){
		printf("%i, %i\n", candi[i],prime[i]);
	}
	return 0;
}