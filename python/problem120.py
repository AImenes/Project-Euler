import math

def prob120():
	sum_r_max = 0
	for a in range(3,1000+1):
		sum_r_max += (2 * a * math.floor((a-1)/2))
		#print(a, math.floor((a-1)/2), ((2 * a * ((a-1)/2))))

	return int(sum_r_max)

def main():
	print(prob120())

if __name__ == "__main__":
	main()