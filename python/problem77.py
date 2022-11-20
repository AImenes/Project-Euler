# It is possible to write ten as the sum of primes in exactly five different ways:

# 7 + 3
# 5 + 5
# 5 + 3 + 2
# 3 + 3 + 2 + 2
# 2 + 2 + 2 + 2 + 2

# What is the first value which can be written as 
# the sum of primes in over five thousand different ways?

#Anders Imenes
#12.04.2022

#Approach DP Bottom up
import sympy 

targetValue = 72
primes = list(sympy.primerange(0, targetValue))
#print(primes)
numberOfPrimes = [0 for x in range(0, targetValue+1)]
numberOfPrimes[0] = 1

#Expected
# 2 - 1
# 3 - 1
# 4 - 1
# 5 - 2
# 6 - 2
# 7 - 3
# 8 - 3
# 9 - 4
# 10 - 5

searching = True

for i in range(len(primes)):
	j = primes[i]
	while j < targetValue and searching:
		numberOfPrimes[j] = numberOfPrimes[j] + numberOfPrimes[j - primes[i]]
		j += 1

for n in range(len(numberOfPrimes)):
	if numberOfPrimes[n] >= 5000:
		print("%i - %i" % (n, numberOfPrimes[n]))
		break
