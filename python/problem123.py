import math
import sympy

def prob123():
	for n in range(3,100):
		p_n = sympy.prime(n)
		if not n % 2 == 0:
			rest = (((p_n - 1)**n)+((p_n + 1)**n)) % (p_n**2)
			print(n, p_n, rest)

			if rest > 1e5:
				print("Yo", n)	

def main():
	prob123()

if __name__ == "__main__":
	main()


# 32
# 48
# 64
# 