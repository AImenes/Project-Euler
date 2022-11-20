import math


def IfPrime(n):
	limit = math.sqrt(n);
	if n > 2:
		for i in range(2, limit):
			if (n % i == 0):
				print("%d is prime" % (n));
				return True;
	return False;

IfPrime(7);