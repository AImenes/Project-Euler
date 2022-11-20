#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using problem42.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?'''

words =[];
with open('problem42.txt') as inputfile:
    for line in inputfile:
        words.append(line.strip().split('","'));
print(words);      
triNum =[];
numbOfTri = 0;

for n in range(1,25):
    temp = (n * (n+1))/2;
    triNum.append(temp);
    
for x in range(len(words[0])):
    wordSum = 0;
    for y in range(len(words[0][x])):
        temp = ord(words[0][x][y]) - 64;
        wordSum += temp;
        
    for z in range(len(triNum)):
        if(wordSum == triNum[z]):
            numbOfTri += 1;
            
print(numbOfTri)
            