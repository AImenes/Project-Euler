#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.'''


amicable = 0;
total = 0;
divisors = 0;
reDiv = 0;

for i in range(1,10000):
    divisors = 0;
    reDiv = 0;
    
    for j in range(1,i):
        if (i%j == 0):
            divisors += j;
            
    for k in range(1, divisors):
        if (divisors%k == 0):
            reDiv += k;
            
    if (reDiv == i and divisors != i):
        amicable += 1;
        total += i;
        print(i, divisors, reDiv)
        
print(amicable, total)
        
            
        
            