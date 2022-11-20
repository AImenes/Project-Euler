#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?'''

upper = 100;
lower = 0;

primes =[];

total = 0;

#Generer primtall
for i in range(lower,upper):
    for j in range(2,i):
        if(i%j==0):
            break;
        else:
            if(i in primes):
                break;
            else:
                primes.append(i);


for x in range(len(primes)):
    counter = 0;
    temp = [int(y) for y in str(primes[x])];

    for y in range((len(temp))-1):
        numb = 0
        print(temp)

        bound = (len(temp)) - 1;
        first = temp[bound];

        for z in range(bound):
            if z<bound:
                temp[bound-z]= temp[bound-z-1];
        temp[0] = first;

        for x in range(len(temp)):
            numb = (temp[x] * (10 ** (bound-x))) + numb;

        if numb in primes:
            counter += 1;
            temp = [int(y) for y in str(numb)];          
        else:
            break;
            
    if (counter == (len(temp) - 1)):
        total += 1;
        
print(total);
        
        
            
            
            
        
            
             