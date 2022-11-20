
targetValue = 200;

coins = [1, 2, 5, 10, 20, 50, 100, 200];
combinations = [0 for x in range(0,targetValue+1)];
combinations[0] = 1;

for i in range(0, len(coins)):
	for j in range(coins[i], targetValue+1):
		combinations[j] = combinations[j] + combinations[j - coins[i]];

print(combinations);