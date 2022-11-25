#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''The decimal number, 585(10) = 1001001001(2) (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)'''

total = 0;

for i in range(0,1000000):
    palindromicB10 = True;
    palindromicB2 = True;

    base10 = i;
    base2 = "{0:b}".format(i);
    base2= int(base2);
    
    b10 = [int(j) for j in str(base10)]
    b2 = [int(j) for j in str(base2)]
    
    #check base10
    for k in range((len(b10))/2):
        if (b10[k] != b10[((len(b10))-1)-k]):
            palindromicB10 = False;

                
    #check base2
    for k in range(len(b2)):
        if (b2[k] != b2[((len(b2))-1)-k]):
            palindromicB2 = False;

    
    if (palindromicB2 == True and palindromicB10 == True):
        print(base10,base2)
        total += i;
        
print(total);