/*
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of 
the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
*/

#include "stdio.h"
#include "math.h"

int calc(int number, int nummerLengde, int arrayNumber[], int arraySum[]);

int main(){
	unsigned short number, i, j;
	int arraySum[10000] = {0}; //Array for summen
	int arrayNumber[3001] = {0}; //Array for hvert tall oppover opphøyd i seg selv
	int mente, rest, nummerLengde;

	//Startverdi
	arrayNumber[0] = 1;
	arraySum[0] = 1;
	nummerLengde = 1;

	for(i = 1; i < 10; i++){//Løkke fra 0 til 1000
		nummerLengde = calc(i, nummerLengde, arrayNumber, arraySum)
	}

	//Legge sammen de to arrayene
	//Nullstille arrayNumber
	return 0;
}

int calc(int number, int nummerLengde, int arrayNumber[], int arraySum[]){
	int j, rest, mente;
	mente = 0; rest = 0;
	for(j = 0; j < nummerLengde; j++){
			arrayNumber[j] = (arrayNumber[j] * number) + mente;
			mente = arrayNumber[j] / 10;
			rest = arrayNumber[j] % 10;

			while(mente){
				arrayNumber[j] = mente % 10;
				mente /= 10; 
				nummerLengde++;
			}

			arrayNumber[j] = rest;
		}
		//Putte tallet resultatet i et array
}

int calcEachNum(){
	int j, rest, mente;
	mente = 0; rest = 0;
	for(j = 0; j < nummerLengde; j++){
			arrayNumber[j] = (arrayNumber[j] * number) + mente;
			mente = arrayNumber[j] / 10;
			rest = arrayNumber[j] % 10;

			while(mente){
				arrayNumber[j] = mente % 10;
				mente /= 10; 
				nummerLengde++;
			}

			arrayNumber[j] = rest;
		}
		//Putte tallet resultatet i et array
	return 0;
}