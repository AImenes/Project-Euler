/*
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

*/

#include "stdio.h"
#define LIMIT 100

//Deklarasjon
void fakultet(int fakTall);
int gangeNyttTall(int faktor, int rest[], int storrelseRest);

//Globale variabler


int main() {
	fakultet(LIMIT);
	return 0;
}

void fakultet(int fakTall){
	int rest[200] = {0};
	int i, j, sum = 0;
	rest[0] = 1;
	int storrelseRest = 1;

	for(i = 2; i <= fakTall; i++){
		storrelseRest = gangeNyttTall(i, rest, storrelseRest);
	}

	for (i = storrelseRest - 1; i >= 0; i--){
		printf("%i", rest[i]);
		sum += rest[i];
	}

	printf("\n%i\n", sum);
}

int gangeNyttTall(int faktor, int rest[], int storrelseRest){
	int i, j;
	int produkt;

	int mente = 0;

	for(i = 0; i < storrelseRest; i++){
		produkt = (faktor * rest[i]) + mente;
		rest[i] = produkt % 10;
		mente = produkt / 10;
	}

	while(mente){
		rest[storrelseRest] = mente % 10;
		mente /= 10;
		storrelseRest++; 
	}

	return storrelseRest;
}
	