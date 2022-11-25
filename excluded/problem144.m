clc
clear all
LazerSlope = -19.7/1.4;
currentPoint = [0, 10.1];
nextPoint = [0,0];
numberOfBounds = 0;
syms x y
ellipse = 4*x^2 + y^2 == 100;

while ((numberOfBounds == 0) || (abs(currentPoint(1)) >= 0.01) || (currentPoint(2) < 0))
	clear LazerBeam setOfEquations interSectionOne interSectionTwo
    clear NextPointNormalSlope angleDifference reflectionAngle
    
    %Create Lazerbeam function
    LazerBeam = y == currentPoint(2) + (LazerSlope*(x - currentPoint(1)));
    disp(numberOfBounds);
    disp(double(currentPoint));
    
    %solve set of equations
    setOfEquations = solve([ellipse,LazerBeam],[x,y]);
    
    %Intersections
    interSectionOne = [setOfEquations.x(1),setOfEquations.y(1)];
    interSectionTwo = [setOfEquations.x(2),setOfEquations.y(2)];
    
    %set first point
    if numberOfBounds == 0
        currentPoint = interSectionTwo;
    end
    
    %Find next Intersection
    if currentPoint(1) == interSectionOne(1)
        nextPoint = interSectionTwo;
    else 
        nextPoint = interSectionOne;
    end
    
    disp(double(nextPoint));
    
    NextPointNormalSlope = -1/((-4 * nextPoint(1)) / nextPoint(2));
    angleDifference = atan(abs((LazerSlope - NextPointNormalSlope)/(1+(NextPointNormalSlope * LazerSlope))));
    %disp(double(angleDifference));
    
    reflectionAngle = atan(NextPointNormalSlope) + angleDifference;
    %disp(double(reflectionAngle));
    
    LazerSlope = tan(reflectionAngle);
    currentPoint = nextPoint;
    
    numberOfBounds = numberOfBounds + 1;
end
   
disp(numberOfBounds);