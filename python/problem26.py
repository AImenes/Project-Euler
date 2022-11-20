'''A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.'''
from decimal import *
import math

getcontext().prec = 100;
maxN = [0,0];

for i in range(1,1001):
	x = Decimal(1) / Decimal(i);

	if len(str(x)) > 5:
		if (i <= 10):
			numberAsString = str(x);
			numberAsString = numberAsString[2:];
		elif (i > 10 and i <= 100):
			numberAsString = str(x);
			numberAsString = numberAsString[3:];
		else:
			numberAsString = str(x);
			numberAsString = numberAsString[4:];

		reci = [numberAsString[0],numberAsString[1],numberAsString[2]];

		y = 3;
		length = 0;

		while (numberAsString[y] != reci[0] and numberAsString[y+1] != reci[1] and numberAsString[y+2] != reci[2]):
			length += 1;
			y += 1;

		if (length > maxN[0]):
			maxN[0] = length;
			maxN[1] = i;

print(maxN);
