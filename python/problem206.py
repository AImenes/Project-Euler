#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sqrt

'''Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.'''

arr = [1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0,0]

for i in range(len(arr)):
    print(i, arr[i])
    
for j in range(1385640646,1390000009):
    k = j ** 2;
    numb = [int(i) for i in str(k)];
    
    print(j,k, arr)
    if (numb[0] == arr[0] and numb[2] == arr[2] and numb[4] == arr[4] and numb[6] == arr[6] and numb[8] == arr[8] and numb[10] == arr[10] and numb[12] == arr[12] and numb[14] == arr[14] and numb[16] == arr[16] and numb[18] == arr[18]):
        print(j,k);
        break;


    

