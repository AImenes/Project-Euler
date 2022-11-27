import time


def prob40(number_of_decimals):
	digits = list()
	i = 0
	while len(digits) < (number_of_decimals + 1):
		for digit in str(i):
			digits.append(int(digit))
		i += 1
	return digits[1] * digits[10] * digits[100] * digits[1000] * digits[10000] * digits[100000] * digits[1000000]

def main():
	number_of_decimals = 1e6
	start = time.time()
	print(prob40(number_of_decimals))
	end = time.time()
	print("Running time: ", end-start, "s")

if __name__ == "__main__":
	main()
