#Funnet på nett
import time
start_time = time.time()

coins = [1,5,10,20,50,100,200]
amount = 200 
memo = {}

def ways(target, avc): 
	#If we reach leaf
	if avc == 0:
		return 1

	t = target
	if (t, avc) in memo:
		return memo[t,avc]

	#Number of ways
	res = 0

	while target >= 0:
		res = res + ways(target,avc-1)
		target = target - coins[avc] 

	memo[t, avc] = res 
	return res

print(ways(amount,6))
print(memo)
print("--- %s seconds ---" % (time.time() - start_time))
