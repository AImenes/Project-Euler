import math
import time

def prob123():
	n, r = 21000, 0
	prime_list = primes(int(3e5))
	
	while r < 1e10:
		p_n = prime_list[n]
		r = 2 * p_n * n	
		n += 1
	return n	


#sieve of Eratosthenes
def primes(n):
	if n > 2:
		numbers = [True for i in range(n+1)]
		numbers[0], numbers[1] = False, False
		primes = [0]

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


def main():
	start = time.time()
	print(prob123())
	end = time.time()
	print(end-start,"s")

if __name__ == "__main__":
	main()

