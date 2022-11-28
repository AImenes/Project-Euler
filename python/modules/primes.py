#sieve of Eratosthenes
def primes(n):
	if n > 2:
		numbers = [True for i in range(n+1)]
		numbers[0], numbers[1] = False, False
		primes = list()

	elif n == 2:
		numbers = [2]
	else:
		return -1

	for i in range(n+1):
		k = 2
		if numbers[i]:
			primes.append(i)

			while (k * i) <= n:
				numbers[k*i] = False
				k += 1

	return primes
