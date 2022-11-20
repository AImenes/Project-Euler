/*
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
*/

#include "stdio.h"

int fibb(int array[], int lengde);

int main(){
	int array[1000] = {0};
	int i, j;

	//indeksering
	int lengde = 1;
	array[0] = 1;


	for(i = 0; i<10; i++){
		lengde = fibb(array, lengde);
		for(j = 10; j >= 0; j--) printf("%i", array[j]);
			printf("\n");
	}


	return 0;
}
int temp = 1, temp2 = 1;

int fibb(int array[], int lengde){
	int i, j = 1, umOfFibb, mente = 0, rest = 0;


	for(i = 0; i < lengde; i++){
		array[0] = temp;
		temp = temp2;
		temp2 = array[0] + temp;

		rest = temp2 % 10;
		mente = temp2 / 10;

		while(mente){
			array[j] = mente % 10;
			mente /= 10;
			j++;
		}

		array[0] = rest;
	}

	return j;
}