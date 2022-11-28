fractions = list()
product = 1
for numerator in range(10,99):
	if not numerator % 10 == 0:
		for denumerator in range(numerator+1,100):
			if not denumerator % 10 == 0:
				utilized = [False for i in range(10)]
				num_str = [int(i) for i in str(numerator)]
				denum_str = [int(i) for i in str(denumerator)]

				for digit in num_str:
					if digit in denum_str:
						num_str.remove(digit)
						denum_str.remove(digit)
						
						#print(num_str, denum_str)
						if numerator / denumerator == num_str[0] / denum_str[0]:
							print(numerator, denumerator, num_str, denum_str)
							fractions.append([int(numerator),int(denumerator)])

for fraction in fractions:
	product *= (fraction[0]/fraction[1])
print(product.as_integer_ratio()) 
