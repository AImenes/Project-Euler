import math


def IfPrime(n):
	if n == 0:
		return False;
	if n > 0:
		limit = math.ceil(math.sqrt(n));
	elif n < 0:
		limit = math.ceil(math.sqrt(abs(n)));
	if abs(n) > 2:
		for i in range(2, limit):
			if (n % i == 0):
				return False;
	return True;

largestValue = [0,0,0];

for a in range(-999,1000):
	for b in range(-1000,1001):
		Counter = 0;
		StillPrime = True;
		n = 0;

		while (StillPrime):
			IsThisPrime = math.pow(n, 2) + (a * n) + b;
			#print(IsThisPrime);
			if (IfPrime(IsThisPrime)):
				#print(n, Counter);
				Counter += 1;
				n += 1;
			else:
				StillPrime = False;

		if (Counter > largestValue[0]):
			largestValue[0] = Counter;
			largestValue[1] = a;
			largestValue[2] = b;

		print(a,b,largestValue[0]);

print(largestValue);