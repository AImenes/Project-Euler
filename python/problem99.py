import math

file = open('problem99.txt','r');

array = file.readlines();

print(array[0]);
biggestVal = 0;
biggestLine = 0;
print(len(array));

for i in range(len(array)):
	#print(array[i]);
	numbers= array[i].split(',');

	for j in range(len(numbers)):
		numbers[j] = int(numbers[j]);

	currentVal = numbers[1] * math.log(numbers[0]);

	if (currentVal > biggestVal):
		biggestVal = currentVal;
		biggestLine = i;

print(biggestLine, biggestVal);
