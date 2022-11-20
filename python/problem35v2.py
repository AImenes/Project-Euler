#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?'''

upper = 1000000;
lower = 3;
total = 0;

#Looper gjennom tallene i lower,upper
for i in range(lower,upper):
    print(i)
    prime = True;
    current = i;
    startingPoint = [int(y) for y in str(i)];
    length = len(startingPoint);
    counter = 0;
    
    
    #En ny løkke starter så lenge vi har et primtall.
    while prime==True:
        
        #Sjekker om det er primtall
        for k in range(2,current):
            if(current % k == 0):
                #Hvis det ikke er primtall
                prime = False;
                
        if prime:
            counter += 1;

        #Hvis tallet er en triprosal
        if (counter == length):
            total += 1;
            prime = False;
        
        #Hvis tallet er primtall, roter det en gang, og bytt current
        if prime==True:
            #Legger tallet inn i et array, og nullstiller current
            temp = [int(j) for j in str(current)];
            current = 0;
            bound = (len(temp)) - 1;
            
            #Roterer tallet
            first = temp[bound];
            for z in range(bound):
                if z<bound:
                    temp[bound-z]= temp[bound-z-1];
            temp[0] = first;
            
            #Gjør det om til en int
            for x in range(len(temp)):
                current = (temp[x] * (10 ** (bound-x))) + current;
                
print(total+1);
            
            
            