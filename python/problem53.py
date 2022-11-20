import math

n= 1;
counter = 0;

for n in range(1,101):
	r = 1;
	while(r <= n):
		value = (math.factorial(n)/((math.factorial(r))*math.factorial(n-r)));
		if value > 1e6:
			counter += 1;
		r += 1;

print(counter);
