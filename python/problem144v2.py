import math
from sympy import symbols, Eq, solve

currentPoint = [0.0, 10.1];
nextPoint = [0,0];
startingAngleRad = -1.499849612;
InAngle = startingAngleRad;
numberOfBounds = 0;
x, y = symbols('x y');
ellipse  = Eq(4*x**2 + y**2 - 100);
cross1 = [0,0];
cross2 = [0,0];

while ((numberOfBounds == 0) or ((abs((currentPoint[0]))>=0.01) or currentPoint[1]<0)):
	LazerBeam = Eq(y - currentPoint[1] - (math.tan(InAngle))*(x-currentPoint[0]));
	print(LazerBeam);

	holder = solve((ellipse, LazerBeam),(x,y));
	cross1[0] = holder[0][0];
	cross1[1] = holder[0][1];
	cross2[0] = holder[1][0];
	cross2[1] = holder[1][1];
	print(cross1, cross2);

	

	a = input('').split(" ")[0]
	print(a)