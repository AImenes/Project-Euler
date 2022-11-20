/*
2,357,207 digits: 28433×2^(7830457)+1.
*/
#include "stdio.h"
#include "math.h"

int main(){
	int delay[2400000] = {0};
	delay[0] = 1;
int tall = 1, i;
	for (i = 1; i < 10; i++){
		tall = tall * 2;
		printf("%i\n", tall);
	}
	return 0;
}