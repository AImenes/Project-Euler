# ProjectEuler - Problem 31.
# Anders Imenes

# Hvor mange kombinasjoner av 1, 2, 5, 10, 20, 50, 100 og 200 gir totalt 200?

# 1 - mynt (1 * 200)
# 2 - mynt (2 * 100)
# 3 - mynt (1x 100, 2x 50)

#Variabler
antallKomb = 0;
currentMynter = 1;
maxAntallMynter = 200;
summen = 0;
i = 0;
moneyArr = [200, 100, 50, 20, 10, 5, 2, 1];

#Går gjennom antallmynter
for i in range(0, 2):
	for j in range(0, 3):
		for k in range(0, 5):
			for l in range(0, 11):
				for m in range(0, 21):
					for n in range(0, 41):
						for o in range(0, 101):
							for p in range(0, 201):
									summen = 200*i + 100*j + 50*k + 20*l + 10*m + 5*n + 2*o + p;
									if (summen == 200):
										antallKomb += 1;
										print("(%d) Funn på %d, %d, %d, %d, %d, %d, %d, %d" % (antallKomb,i,j,k,l,m,n,o,p));



# Løkke som teller til 200
	#Sjekker



