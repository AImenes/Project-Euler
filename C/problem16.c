/*
2^(15) = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^(1000)?
*/

#include "stdio.h"

int multiply(int array[], int lengde);

int main(){
	int array[1000] = {0};
	int i, j = 1, k, l, rest, mente, sum = 0;
	int lengde = 1;
	 array[0] = 1;

	 for(i = 0; i < 1000; i++){
	 	lengde = multiply(array, lengde);
	 }

	 for (i = 0; i< lengde; i++){
	 	sum += array[i];
	 }
	 printf("%i (%i)\n", sum, lengde);


	return 0;
}

int multiply(int array[], int lengde){
	int l, mente = 0, rest;
	int produkt;

	for (l = 0; l < lengde; l++)
	{
		produkt = (array[l] * 2) + mente;
		array[l] = produkt % 10;
		mente = produkt / 10;
	}


	while (mente)
		{
			array[lengde] = mente % 10;
			mente /= 10;
			lengde++;
		}	


	

	return lengde;
}