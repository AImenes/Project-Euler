#include "stdio.h"

int flipAble(int n);

int main(){
int fakA, fakB, i, prod;
fakA = fakB = 999;

while(fakA > 100){
	fakB = 999;
	while (fakB > 100) {
		prod = fakB * fakA;
		if (flipAble(prod) != 0) {
			printf("%i * %i = %i\n", fakA, fakB, prod);
		}
		fakB--;
	}
	fakA--;
}
}

int flipAble(int n){
	 int i, reversedNumber = 0, remainder;

    i = n;

    while(n != 0)
    {
        remainder = n%10;
        reversedNumber = reversedNumber*10 + remainder;
        n /= 10;
    }

    if (i == reversedNumber) {
    	return i;
    }

    return 0;
}