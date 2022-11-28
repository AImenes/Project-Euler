'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''
def prob32():
	count = 0
	sum_of_pandigitals = 0
	products = list()
	for x in range(2,99):
		for y in range(101,5000):
			valid = True
			utilized = [False for i in range(10)]
			utilized[0] = True
			x_str = [int(i) for i in str(x)]

			for digit in x_str:
					if utilized[digit] == False:
						utilized[digit] = True
					else:
						valid = False

			y_str = [int(i) for i in str(y)]
			for digit in y_str:
				if utilized[digit] == False:
					utilized[digit] = True
				else:
					valid = False

			product = x * y
			product_str = [int(i) for i in str(product)]
			
			for digit in product_str:
				if utilized[digit] == False:
					utilized[digit] = True
				else:
					valid = False

			if valid and False not in utilized:
				if product not in products:
					count += 1
					products.append(product)
					print(x,y,product)
					sum_of_pandigitals += product

	return count, sum_of_pandigitals

def main():
	print(prob32())

if __name__ == "__main__":
	main()