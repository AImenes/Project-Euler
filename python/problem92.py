#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import time

'''A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?'''

counter89 = 0;
counter1 = 0;
current = 0;
temp = []

for i in range(1, 10000000):
    current = 0;
    temp = [int(q) for q in str(i)]
    
    while ((current != 1) and (current != 89)):
        current = 0;
        for y in range(len(temp)):
            current += (temp[y] ** 2);
        
        current = int(current);
        
        #print(current)
        #time.sleep(3)
        
        temp = [int(z) for z in str(current)]       
        #print(temp)

        if (current == 89):
            counter89 += 1;
        if (current == 1):
            counter1 += 1;
            
    if (i % 100000 == 0):
        print("%d%%" % (i/100000))


            
print("Antall 89: %d \nAntall 1: %d" % (counter89, counter1));