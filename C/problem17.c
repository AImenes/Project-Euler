/*
If all the numbers from 1 to 1000 (one thousand) were written out in words, how many letters would be used?
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
*/

#include "string.h"
#include "stdio.h"

int main(){
	char one[] = "one";
	char two[] = "two";
	char three[] = "three";
	char four[] = "four"; 
	char five[] = "five";
	char six[] = "six";
	char seven[] = "seven";
	char eight[] = "eight";
	char nine[] = "nine";
	char ten[] = "ten";
	char eleven[] = "eleven";
	char twelve[] = "twelve";
	char thirteen[] = "thirteen";
	char fourteen[] = "fourteen";
	char fifteen[] = "fifteen";
	char sixteen[] = "sixteen";
	char seventeen[] = "seventeen";
	char eighteen[] = "eighteen";
	char nineteen[] = "nineteen";

	char twenty[] = "twenty";
	char thirty[] = "thirty";
	char forty[] = "forty";
	char fifty[] = "fifty";
	char sixty[] = "sixty";
	char seventy[] = "seventy";
	char eighty[] = "eighty";
	char ninety[] = "ninety";

	char hundred[] = "hundred";
	char thousand[] = "thousand";

	
	int i, num, sum = 0;
	for(i = 1; i <= 1000; i++){
		if((i % 20) == 1) printf("%s\n", one);
		else if((i % 20) == 2) printf("%s\n", two);
		else if((i % 20) == 3) printf("%s\n", three);
		else if((i % 20) == 4) printf("%s\n", four);
		else if((i % 20) == 5) printf("%s\n", five);
		else if((i % 20) == 6) printf("%s\n", six);
		else if((i % 20) == 7) printf("%s\n", seven);
		else if((i % 20) == 8) printf("%s\n", eight);
		else if((i % 20) == 9) printf("%s\n", nine);
		else if((i % 20) == 10) printf("%s\n", ten);
		else if((i % 20) == 11) printf("%s\n", eleven);
		else if((i % 20) == 12) printf("%s\n", twelve);
		else if((i % 20) == 13) printf("%s\n", thirteen);
		else if((i % 20) == 14) printf("%s\n", fourteen);
		else if((i % 20) == 15) printf("%s\n", fifteen);
		else if((i % 20) == 16) printf("%s\n", sixteen);
		else if((i % 20) == 17) printf("%s\n", seventeen);
		else if((i % 20) == 18) printf("%s\n", eighteen);
		else if((i % 20) == 19) printf("%s\n", nineteen);


	}
	return 0;
}