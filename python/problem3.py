import math

def IfPrime(n, listen):
	limit = math.ceil(math.sqrt(abs(n)));
	for i in range(2, limit):
		if (n % i == 0):
			listen.append(n/i);
	return listen;

tall = 600851475143;
liste = [];
print(IfPrime(tall, liste));
