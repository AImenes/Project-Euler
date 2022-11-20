import math

counter = 0;
number = 11;

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

liste = [];

for grunntall in range(2,100):
	for eksponent in range(2,50):
		tall = grunntall ** eksponent;
		sumOfNumber = sum_digits(tall);
		if(sumOfNumber ** eksponent == tall):
			liste.append(tall);

liste = sorted(liste);

for x in range(0,len(liste)):
	print(x+1,":", liste[x]);