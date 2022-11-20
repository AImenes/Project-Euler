import math


#Definere variabler
radius = 1;
antallSirkler = 2;
bredde = antallSirkler * 2*radius;
hoyde = 2 * radius;
Lsection = ((hoyde*hoyde) - (math.pi * (radius ** 2)))/4;

crossing = 0;

crossingX = ((2/antallSirkler) + 2) + math.sqrt(((((1/(antallSirkler ** 2))+1)**2)-4*(1/(antallSirkler ** 2))+1))/2*((1/(antallSirkler ** 2))+1)
crossingY = ((2/antallSirkler) + 2) - math.sqrt(((((1/(antallSirkler ** 2))+1)**2)-4*(1/(antallSirkler ** 2))+1))/2*((1/(antallSirkler ** 2))+1)

print(crossingX, crossingY)

print(Lsection);