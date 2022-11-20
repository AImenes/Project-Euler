import math
from sympy import symbols, Eq, solve

currentPoint = [0.00000, 10.10000];
newPoint = [0,0];
startingAngleRad = -19.7/1.4;
InAngle = startingAngleRad;
numberOfBounds = 0;
x, y = symbols('x y');
ellipse  = Eq(4*x**2 + y**2 - 100);

while ((numberOfBounds == 0) or ((abs((currentPoint[0]))>=0.01) or currentPoint[1]<0)):
	print("Current point: ");
	print(currentPoint);
	print("Number: ",numberOfBounds);
	#print("Current slope: ");
	#print(InAngle);

	tangentLine = Eq(y - currentPoint[1] - (InAngle*(x - currentPoint[0])));
	holder = solve((ellipse, tangentLine), (x,y));
	#print(holder);

	cross1 = [0,0]
	cross1[0] = holder[0][0];
	cross1[1] = holder[0][1];

	cross2 = [0,0]
	cross2[0] = holder[1][0];
	cross2[1] = holder[1][1];

	if numberOfBounds == 0:
		currentPoint = cross1;

	if (abs(cross1[0] - (currentPoint[0])) < abs(cross2[0] - (currentPoint[0]))):
		newPoint[0] = cross2[0];
		newPoint[1] = cross2[1];
	else:
		newPoint[0] = cross1[0];
		newPoint[1] = cross1[1];

	print("Next point: ");
	print(newPoint);
	NextPointNormalSlope = -1 / ((-4 * newPoint[0]) / newPoint[1]);
	print(NextPointNormalSlope, InAngle);
	angleDifference = math.atan(abs((NextPointNormalSlope - InAngle)/(1+(NextPointNormalSlope * InAngle))));
	print(angleDifference);
	reflectionAngle = math.atan(NextPointNormalSlope) + angleDifference;
	print(reflectionAngle);
	InAngle = math.tan(reflectionAngle);
	currentPoint = newPoint;
	numberOfBounds = numberOfBounds + 1;

	#a = input('').split(" ")[0]
	#print(a)

print(numberOfBounds);