import math;

numbers = [];

for a in range(1,100):
	for b in range(1,100):
		numbers.append(math.pow(a,b));

for x in range(len(numbers)):
	numbers[x] = int(numbers[x]);

maxVal = 0;

for number in numbers:
	currentMax = 0;
	holder = str((number));
	for digit in holder:
		currentMax += int(digit);

	if currentMax > maxVal:
		maxVal = currentMax;
		MaxNum = number;

print(maxVal, MaxNum);

