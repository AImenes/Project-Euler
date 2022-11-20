import math

holder1= 2;
holder2= 1;
sumOfNumbers = 2;
Limit = 4e6;

while (holder1 < Limit):

	#Next Fiboonacci
	temp = holder1 + holder2;

	#Add to sum if even-number
	if (temp % 2 == 0):
		sumOfNumbers += temp;

	#Prepare next iteration
	holder2 = holder1;
	holder1 = temp;
#Loop closes

#Print result
print(sumOfNumbers);

