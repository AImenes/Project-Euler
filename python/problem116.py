# Problem 116
# 25/11/2022
# Dynamic Programming Bottom up approach.
# See PDF for thought process.


def red(length_of_gray_tiles):
	number_of_combinations = [0 for i in range(length_of_gray_tiles+1)]
	for i in range(length_of_gray_tiles+1):
		if i < 2:
			number_of_combinations[i] = 0
		elif i == 2:
			number_of_combinations[i] = 1
		else:
			number_of_combinations[i] = number_of_combinations[i-1] + number_of_combinations[i-2] + 1
	return number_of_combinations[length_of_gray_tiles]

def green(length_of_gray_tiles):
	number_of_combinations = [0 for i in range(length_of_gray_tiles+1)]
	for i in range(length_of_gray_tiles+1):
		if i < 3:
			number_of_combinations[i] = 0
		elif i == 3:
			number_of_combinations[i] = 1
		else:
			number_of_combinations[i] = number_of_combinations[i-1] + number_of_combinations[i-3] + 1
	return number_of_combinations[length_of_gray_tiles]

def blue(length_of_gray_tiles):
	number_of_combinations = [0 for i in range(length_of_gray_tiles+1)]
	for i in range(length_of_gray_tiles+1):
		if i < 4:
			number_of_combinations[i] = 0
		elif i == 4:
			number_of_combinations[i] = 1
		else:
			number_of_combinations[i] = number_of_combinations[i-1] + number_of_combinations[i-4] + 1
	return number_of_combinations[length_of_gray_tiles]


def prob116(length_of_gray_tiles):
	r, g, b = red(length_of_gray_tiles), green(length_of_gray_tiles), blue(length_of_gray_tiles)
	return r+g+b
	

def main():
	number_of_gray_tiles = 50
	print(prob116(number_of_gray_tiles))

if __name__ == "__main__":
	main()


