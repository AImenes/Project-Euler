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
with open('problem82.txt') as inputfile:
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

#.............................

#Array for om det er besokt
Visited = []
i = 1 
while i < sizeOfMat+1:
    Visited.append([0 for y in range(0,sizeOfMat)]);
    i += 1;
    
#''''''''''''''''''''''''''''''



#LOGIKKEN
minPath = 264442;
combleft = 20;
while combleft < 80:  
    combright = 0;
    if combleft < 20:
        target = 40;
    elif combleft > 19 and combleft < 60:
        target = 80;
    else:
        target = 80;
    while combright < target:
        
        ##Resett
        for x in range(len(Paths)):
            for y in range(len(Paths[x])):
                Paths[x][y] = 9599840;
        for x in range(len(Visited)):
            for y in range(len(Visited[x])):
                Visited[x][y] = 0;

        Paths[combleft][0] = matrix[combleft][0];   
        
        ##Gjenta helt til maalnoden er besokt
        while Visited[combright][sizeOfMat-1] != 1:

            ###Se etter laveste ubesokte verdi
            xPos = 0
            yPos = 0
            lavestPath = 9099840
            for i in range(0,sizeOfMat):
                for j in range(0,sizeOfMat):
                    if Paths[i][j]<lavestPath:
                        if Visited[i][j] == 0:
                            lavestPath = Paths[i][j];
                            xPos = i;
                            yPos = j;

            ###Hvis naboen eksisterer, er ubesokt, og hvis veien er kortere (4mulige), overskriv 
            ####Høyre
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
            
        ##Hvis det er den minste, lagre
        if Paths[combright][sizeOfMat-1]<minPath:
            minPath = Paths[combright][sizeOfMat-1];

        print("Start: Paths(%d)(0) \n Finish: Paths(%d)(79) \n currentPath: %d \n minPath: %d \n" % (combleft, combright, Paths[combright][sizeOfMat-1], minPath))
        
        combright += 1;

        
    combleft += 1;

