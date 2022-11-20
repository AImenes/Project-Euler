import math

targetValue = 101;


ways = [];

for x in range(0,targetValue+1):
	ways.append(0);

ways[0] = 1;

for i in range(1, targetValue-1):
	for j in range(i, targetValue):
		ways[j] = ways[j] + ways[j - i];

print(ways); 