'''A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.'''
import time 

def prob26(upper):
	highest_result = [0,0]
	for d in range(3,upper):
		used_remainders = list()

		if not (d & (d-1) == 0):
			if d < 10:
				numerator = 10
			elif d >= 10 and d < 100:
				numerator = 100
			else:
				numerator = 1000

			counter = 1
			rest = (numerator % d) * 10

			while (not (rest == numerator or rest == 0)) and rest not in used_remainders:
				used_remainders.append(rest)
				rest = (rest % d) * 10
				counter += 1

		if counter > highest_result[1]:
			highest_result[0], highest_result[1] = d, counter

	return highest_result

def main():
	upper = 1000
	start = time.time()
	print(prob26(upper))
	end = time.time()
	print(end-start,"s")

if __name__ == "__main__":
	main()
