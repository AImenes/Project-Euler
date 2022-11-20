#include "stdio.h"
#include "math.h"

long long int isPrime[2000001];
long long int limit = 2000000;
long long int sum = 0;

int main(){
	long long int i, j;

	for (i = 0; i <= limit; i++){
		isPrime[i] = 1;
	}
	isPrime[0] = 0;
	isPrime[1] = 0;

	for (i = 2; i <= limit; i++)
	{
		if(isPrime[i] == 1){
			for (j = 2; (i*j) <= limit; j++)
			{
				isPrime[i*j] = 0;
			}
		}
	}

	for (i = 0; i <= limit; i++){
		if (isPrime[i] == 1){
			sum += i;
			printf("%lli\n", i);
		}
	}

	printf("%lli\n", sum);

	return 0;
}