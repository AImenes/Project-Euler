#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
'''

limit = 100000;
T =[];
P =[];
H =[];

for n in range(0,limit):
    T.append((n*(n+1))/2);
    P.append((n*(3*n-1))/2);
    H.append((n*(2*n-1)));
    
for x in range(len(T)):
    if (T[x] in P and T[x] in H):
        print(T[x])
    