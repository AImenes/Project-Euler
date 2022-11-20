/*
A palindromic number reads the same both ways. 
The largest palindrome made from the 
product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
*/

#include "stdio.h"

int flipAble();

int main(){
	int number, i = 998001;
	while(i > 0){
		if(flipAble(i) != 0){
			int divident = 2;
			number = i;
			while (number > 1){
				if ((number % divident) == 0){
					number /= divident;
					divident--;
				}
				divident++;
			}
			if (divident < 1000){
			printf("%i  %i\n", i, divident);
			}

		}
	i--;	

	}
	return 0;
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