#!/usr/bin/env python
# -*- coding: utf-8 -*-


###############################################
#            Dijkstras algoritme              #
###############################################
import sys

# coding=utf-8

sizeOfMat = 80;

'''LAST INN ARRAY MED PATHS'''
matrix = [];
with open('problem83.txt') as inputfile:
    for line in inputfile:
        matrix.append(line.strip().split(','));

for x in range(len(matrix)):
    matrix[x] = list(map(int, matrix[x]))       
''''''''''''''''''''''''''''''


# Array for kortest mulig vei
Paths = []
i = 1 
while i < sizeOfMat+1:
    Paths.append([1599840 for y in range(0,sizeOfMat)]);
    i += 1;

Paths[0][0] = matrix[0][0]    
#.............................

#Array for om det er besokt
Visited = []
i = 1 
while i < sizeOfMat+1:
    Visited.append([0 for y in range(0,sizeOfMat)]);
    i += 1;
    
#''''''''''''''''''''''''''''''

## Print ut arrayene
for x in range(len(matrix)):
    print(matrix[x]);

print("\n")

for x in range(len(Paths)):
    print(Paths[x]);

print("\n")

for x in range(len(Visited)):
    print(Visited[x]);

print("\n")


#LOGIKKEN

##Gjenta helt til maalnoden er besokt
while Visited[sizeOfMat-1][sizeOfMat-1] != 1:

    ###Se etter laveste ubesokte verdi
    xPos = 0
    yPos = 0
    lavestPath = 999999
    for i in range(0,sizeOfMat):
        for j in range(0,sizeOfMat):
            if Paths[i][j]<lavestPath:
                if Visited[i][j] == 0:
                    lavestPath = Paths[i][j];
                    xPos = i;
                    yPos = j;
    print(xPos, yPos, lavestPath)

    ###Hvis naboen eksisterer, er ubesokt, og hvis veien er kortere (4mulige), overskriv 
    ####Venstre
    if(yPos > 0):
        if(lavestPath + matrix[xPos][yPos-1])<Paths[xPos][yPos-1]:
            Paths[xPos][yPos-1] = lavestPath + matrix[xPos][yPos-1];
            
    ####Høy
    if(yPos < sizeOfMat-1):
        if(lavestPath + matrix[xPos][yPos+1])<Paths[xPos][yPos+1]:
            Paths[xPos][yPos+1] = lavestPath + matrix[xPos][yPos+1];
   
    ####Opp
    if(xPos > 0):
        if(lavestPath + matrix[xPos-1][yPos])<Paths[xPos-1][yPos]:
            Paths[xPos-1][yPos] = lavestPath + matrix[xPos-1][yPos];

    ####Ned
    if(xPos < sizeOfMat-1):
        if(lavestPath + matrix[xPos+1][yPos])<Paths[xPos+1][yPos]:
            Paths[xPos+1][yPos] = lavestPath + matrix[xPos+1][yPos];

    ##Sett noden som besokt, og se etter neste laveste verdi
    Visited[xPos][yPos] = 1;
    
print(Paths[sizeOfMat-1][sizeOfMat-1])


