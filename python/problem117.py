# Problem 116
# 25/11/2022
# Dynamic Programming Bottom up approach.
# See PDF for thought process.


def prob117(length_of_gray_tiles):
	combinations = [0 for i in range(length_of_gray_tiles+1)]
	combinations[0], combinations[1], combinations[2] = 0,1,2
	for i in range(length_of_gray_tiles+1):
		if i > 2:
			combinations[i] = 1 + combinations[i-1] + combinations[i-2] + combinations[i-3]
	return combinations[length_of_gray_tiles]
	

def main():
	number_of_gray_tiles = 6
	print(prob117(number_of_gray_tiles))

if __name__ == "__main__":
	main()

