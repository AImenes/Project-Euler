#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pprint
import time

def horisontalBlock():
    
    global sudokus;
    global currentBoard;
    
    for v in range(0,3):
        blockStart = 0 + (3*v);
        blockStop = 3 + (3*v);


        amountOfNum = [0,0,0,0,0,0,0,0,0]
        xPos = [0,0]
        yPos = [0,0]

        for n in range(1,10):
            for x in range(blockStart,blockStop):
            #Sjekke om det er to av et tall i tre første horisontale blokkene (3x3), som vil si (3x9)-området
                for y in range(0,9):
                    if (sudokus[currentBoard][x][y] == n):
                        amountOfNum[n-1] += 1;

            if (amountOfNum[n-1] == 2):
                counter = 0;
                for xx in range(blockStart,blockStop):
                    for yy in range(0,9):
                        if (sudokus[currentBoard][xx][yy] == n):
                            xPos[counter]=xx;
                            yPos[counter]=yy;
                            counter += 1;

                #Finne ledig x
                freeSpotX = [0,0,0];
                freeSpotX[xPos[0]%3] = 1;
                freeSpotX[xPos[1]%3] = 1;
                for r in range(len(freeSpotX)):
                    if(freeSpotX[r] == 0):
                        freeRow = r + blockStart;

                #Finne ledig block
                freeSpotY = [0,0,0];
                freeSpotY[(yPos[0])/3] = 1;
                freeSpotY[(yPos[1])/3] = 1;
                for s in range(len(freeSpotY)):
                    if(freeSpotY[s] == 0):
                        freeColomn = s;

                #Finne ledige celler
                startPos = freeColomn * 3;
                stopPos  = startPos + 3;
                possibleCell = 0;

                for t in range(startPos, stopPos):
                    if(sudokus[currentBoard][freeRow][t] == 0):
                        available = 0;
                        for u in range(0,9):
                            if(sudokus[currentBoard][u][t] == n):
                                available += 1;
                        if(available == 0):
                            possibleCell += 1;
                            finalX = t;
                if(possibleCell == 1):
                    sudokus[currentBoard][freeRow][finalX] = n;
                    print("(Brett %d) Horisontal: Satt inn %d i posisjon (%d, %d)" % (1+currentBoard,n,freeRow+1,finalX+1))

def verticalBlock():
    global sudokus;
    global currentBoard;
    
    for v in range(0,3):
        blockStart = 0 + (3*v);
        blockStop = 3 + (3*v);

        amountOfNum = [0,0,0,0,0,0,0,0,0]
        xPos = [0,0]
        yPos = [0,0]

        for n in range(1,10):
            for y in range(blockStart,blockStop):
            #Sjekke om det er to av et tall i tre første vertikale blokkene (3x3), som vil si (9x3)-området
                for x in range(0,9):
                    if (sudokus[currentBoard][x][y] == n):
                        amountOfNum[n-1] += 1;

            if (amountOfNum[n-1] == 2):
                counter = 0;
                for xx in range(blockStart,blockStop):
                    for yy in range(0,9):
                        if (sudokus[currentBoard][yy][xx] == n):
                            xPos[counter]=xx;
                            yPos[counter]=yy;
                            counter += 1;

                #Finne ledig x
                freeSpotX = [0,0,0];
                freeSpotX[(xPos[0])%3] = 1;
                freeSpotX[(xPos[1])%3] = 1;
                for s in range(len(freeSpotX)):
                    if(freeSpotX[s] == 0):
                        freeColomn = s + blockStart;
                
                #Finne ledig block
                freeSpotY = [0,0,0];
                freeSpotY[yPos[0]/3] = 1;
                freeSpotY[yPos[1]/3] = 1;
                for r in range(len(freeSpotY)):
                    if(freeSpotY[r] == 0):
                        freeRow = r;

                #Finne ledige celler
                startPos = freeRow * 3;
                stopPos  = startPos + 3;
                possibleCell = 0;

                for t in range(startPos, stopPos):
                    if(sudokus[currentBoard][t][freeColomn] == 0):
                        available = 0;
                        for u in range(0,9):
                            if(sudokus[currentBoard][t][u] == n):
                                available += 1;
                        if(available == 0):
                            possibleCell += 1;
                            finalX = t;
                if(possibleCell == 1):
                    sudokus[currentBoard][finalX][freeColomn] = n;
                    print("(Brett %d) Vertikal: Satt inn %d i posisjon (%d, %d)" % (1+currentBoard,n,finalX+1,freeColomn+1))

                    
def rowContaining8():
    for y in range(0,9):
        numbers = [0,0,0,0,0,0,0,0,0]
        countTo8 = 0;
        nextNum = 0;
        
        for x in range(0,9):
            numbers[(sudokus[currentBoard][y][x])-1] = 1;
            if(sudokus[currentBoard][y][x] != 0):
                countTo8 += 1;
                
        if(countTo8 == 8):
            for z in range(len(numbers)):
                if(numbers[z]==0):
                    nextNum = z + 1;         
            for s in range(0,9):
                if(sudokus[currentBoard][y][s]==0):
                    sudokus[currentBoard][y][s] = nextNum;
                    print("(Brett %d) HoriRow: Satt inn %d i posisjon (%d, %d)" % (1+currentBoard,nextNum,y+1,x+1));
                    
                    
def colomnContaining8(): 
    
    for y in range(0,9):
        numbers = [0,0,0,0,0,0,0,0,0]
        countTo8 = 0;
        nextNum = 0;
        for x in range(0,9):
            numbers[(sudokus[currentBoard][x][y])-1] = 1;
            if(sudokus[currentBoard][x][y] != 0):
                countTo8 += 1;
        if(countTo8 == 8):
            for z in range(len(numbers)):
                if(numbers[z]==0):
                    nextNum = z + 1;
            for x in range(0,9):
                if(sudokus[currentBoard][x][y]==0):
                    sudokus[currentBoard][x][y] = nextNum;
                    print("(Brett %d) HoriColomn: Satt inn %d i posisjon (%d, %d)" % (1+currentBoard,nextNum,x+1,y+1))
    
                    
                
            

def blockContaining8():
    
    for d in range(0,9):
        blockRow = 0 + 3 * (d / 3);
        blockCol = (d % 3) * 3;
        numbers = [0,0,0,0,0,0,0,0,0]
        countTo8 = 0;
        nextNum = 0;
      
        for y in range(blockRow,blockRow+3):
            for x in range(blockCol,blockCol+3):
                numbers[(sudokus[currentBoard][y][x])-1] = 1;
                if(sudokus[currentBoard][y][x] != 0):
                    countTo8 += 1;
            if(countTo8 == 8):
                for z in range(len(numbers)):
                    if(numbers[z] == 0):
                        nextNum = z + 1;
                for r in range(blockRow,blockRow+3):
                    for s in range(blockCol,blockCol+3):
                        if(sudokus[currentBoard][r][s]==0):
                            sudokus[currentBoard][r][s] = nextNum;
                            print("(Brett %d) BlockRemain: Satt inn %d i posisjon (%d, %d)" % (1+currentBoard,nextNum,r+1,s+1))
            
def xCross():    
     for d in range(0,9):
        
        #Nullstiller og velger block
        blockRow = 0 + 3 * (d / 3);
        blockCol = (d % 3) * 3;
        horNeighbor = [0,0]
        verNeighbor = [0,0]
        countTo8 = 0
        
        #Bestemme horisontalenaboblokker
        if blockCol == 0:
            horNeighbor[0] = 3;
            horNeighbor[1] = 6;
        elif blockCol == 3:
            horNeighbor[0] = 0;
            horNeighbor[1] = 6;
        else:
            horNeighbor[0] = 0;
            horNeighbor[1] = 3;
                
        #Bestemme vertikale naboblokker
        if blockRow == 0:
            verNeighbor[0] = 3;
            verNeighbor[1] = 6;
        elif blockRow == 3:
            verNeighbor[0] = 0;
            verNeighbor[1] = 6;
        else:
            verNeighbor[0] = 0;
            verNeighbor[1] = 3;        
        
        #Lokaliser alle nabotall i horisontale blokker
        for n in range(1,10):
            normalizedBlock = [[0,0,0],[0,0,0],[0,0,0]];
            numbers = [0,0,0,0,0,0,0,0,0]
            countTo8 = 0;

            #Hvilket tall mangler i blokken, og hvilket plasser er ledig
            for y in range(blockRow,blockRow+3):
                for x in range(blockCol,blockCol+3):
                    if(sudokus[currentBoard][y][x] != 0):
                        numbers[(sudokus[currentBoard][y][x])-1] = 1;
                        normalizedBlock[y%3][x%3] = 1;   
            
            for m in range(0,2):
                for r in range(blockRow,blockRow+3):
                    for s in range(horNeighbor[m],horNeighbor[m]+3): 
                        if ((sudokus[currentBoard][r][s] == n) and (numbers[(sudokus[currentBoard][r][s])-1] == 0)):
                            for t in range(0,3):
                                normalizedBlock[r%3][t] = 1;
        
            for m in range(0,2):                     
                for r in range(verNeighbor[m],verNeighbor[m]+3):
                    for s in range(blockCol,blockCol+3): 
                        if ((sudokus[currentBoard][r][s] == n) and (numbers[(sudokus[currentBoard][r][s])-1] == 0)):
                            for t in range(0,3):
                                normalizedBlock[t][s%3] = 1;
            
            for r in range(0,3):
                for s in range(0,3):
                    if normalizedBlock[r][s] == 1:
                        countTo8 += 1;
            
            if ((countTo8 == 8) and (numbers[n-1]==0)):
                 for r in range(0,3):
                    for s in range(0,3):
                        if normalizedBlock[r][s] == 0:
                            sudokus[currentBoard][blockRow + r][blockCol + s] = n;
                            numbers[n-1] = 1;    
                            print("(Brett %d) xCross: Satt inn %d i posisjon (%d, %d)" % (1+currentBoard,n,blockRow+r+1,blockCol+s+1))
            
            


                
                
                
                
            
                                   
                
                                
def printBoard():

    print("\n")
    print("  -------------------------------")
    print("  |           Brett %d          |" % (1 + currentBoard))
    print("  -------------------------------")
    for r in range(0,9):
        if(r%3==0 and r != 0):
            print("  -------------------------------")
        print("  | %d  %d  %d | %d  %d  %d | %d  %d  %d |" % (sudokus[currentBoard][r][0],sudokus[currentBoard][r][1],sudokus[currentBoard][r][2],sudokus[currentBoard][r][3],sudokus[currentBoard][r][4],sudokus[currentBoard][r][5],sudokus[currentBoard][r][6],sudokus[currentBoard][r][7],sudokus[currentBoard][r][8]))

    print("  -------------------------------")
    print("\n")

    
    
def isFinished():  
    global completedBoards;
    for r in range(0,9):
        for s in range(0,9):
            if(sudokus[currentBoard][r][s]==0):
                return False;
    completedBoards += 1;
    return True;


def xWing():
   
    #Går igjennom tallene 1-9
    for n in range(0,9):
        numOfRows = 0;
        xPos = [0,0,0,0,0,0,0,0,0];
        differentBlocks = [0,0,0,0,0,0,0,0,0,0];
        #Horisontal sjekk
        #Ser om det er akkurat to potensiale plasser for n
        for x in range(0,9):
            counter = 0;
            for y in range(0,9):
                if freeSpots[x][y][n] == 1:
                    counter += 1;

            if counter == 2:
                xPos[numOfRows] = x;
                differentBlocks[numOfRows] = x / 3;
                numOfRows += 1;
                
        yPos = [[0,0],[0,0]];
        if (numOfRows == 2 and (differentBlocks[0] != differentBlocks[1])):
            whatCell = 0;
            whatRow = 0;
            for x in range(0,numOfRows):
                for y in range(0,9):
                    if freeSpots[xPos[x]][y][n] == 1:
                        yPos[whatRow][whatCell] = y;
                        whatCell += 1;
                whatRow += 1;
                whatCell = 0;
        
        
        #Hvis ja, sjekker om det er det på noen andre rader
        if ((yPos[0][0] == yPos[1][0] and yPos[0][1] == yPos[1][1]) and (yPos[0][0] != yPos[0][1] and yPos[1][0] != yPos[1][1]) and (yPos[0][0] / 3 != yPos[0][1] / 3)):
            print("Vi har horisontal xWing med tallet %d på rad %d og rad %d" % (n+1, xPos[0]+1,xPos[1]+1));
            
            for y in range(0,2):
                for x in range(0,9):
                    if ((x != xPos[0] and x != xPos[1]) and (freeSpots[x][yPos[0][y]][n] == 1)):
                        freeSpots[x][yPos[0][y]][n] == 0;
                        print("Fjernet tallet %d fra posisjon (%d,%d)" % (n+1,x+1,yPos[0][y]+1))
                        
        #Vertikal sjekk
        numOfCols = 0;
        yPosVer = [0,0,0,0,0,0,0,0,0];
        differentBlocks = [0,0,0,0,0,0,0,0,0,0];
            #Ser om det er akkurat to potensiale plasser for n
        for y in range(0,9):
            counter = 0;
            for x in range(0,9):
                if freeSpots[x][y][n] == 1:
                    counter += 1;

            if counter == 2:
                yPosVer[numOfCols] = y;
                differentBlocks[numOfCols] = y / 3;
                numOfCols += 1;
                
        xPosVer = [[0,0],[0,0]];
        if (numOfCols == 2 and (differentBlocks[0] != differentBlocks[1])):
            whatCell = 0;
            whatCol = 0;
            for y in range(0,numOfCols):
                for x in range(0,9):
                    if freeSpots[x][yPosVer[y]][n] == 1:
                        xPosVer[whatCol][whatCell] = x;
                        whatCell += 1;
                whatCol += 1;
                whatCell = 0;
                #Hvis ja, sjekker om det er det på noen andre rader
        
        if ((xPosVer[0][0] == xPosVer[1][0] and xPosVer[0][1] == xPosVer[1][1]) and (xPosVer[0][0] != xPosVer[0][1] and xPosVer[1][0] != xPosVer[1][1]) and (xPosVer[0][0] / 3 != xPosVer[0][1] / 3)):
            print("Vi har vertikal xWing med tallet %d på kolonne %d og kolonne %d" % (n+1, yPosVer[0]+1,yPosVer[1]+1));
            
            for x in range(0,2):
                for y in range(0,9):
                    if ((y != yPosVer[0] and y != yPosVer[1]) and (freeSpots[xPosVer[0][x]][y][n] == 1)):
                        freeSpots[xPosVer[0][x]][y][n] == 0;
                        print("Fjernet tallet %d fra posisjon (%d,%d)" % (n+1,xPosVer[0][x]+1,y+1))
                
def justOnePossible():
    
    for x in range(0,9):
        for y in range(0,9):
            counter = 0;
            for z in range(0,9):
                if freeSpots[x][y][z] == 1:
                    number = z + 1;
                    counter += 1;
            if counter == 1:
                sudokus[currentBoard][x][y] = number;
                print("(Brett %d) onePossible: Satt inn %d i (%d,%d)" % (currentBoard+1,number, x+1,y+1))
                
                
def orientation(ifPri):
    global freeSpots;
    freeSpots = [[[1 for d in range(9)] for e in range(9)] for f in range(9)]
    
    for x in range(0,9):
        for y in range(0,9):
            if sudokus[currentBoard][x][y] == 0:
                
                for r in range(0,9):
                    if sudokus[currentBoard][x][r] != 0:
                        freeSpots[x][y][(sudokus[currentBoard][x][r])-1] = 0;
                for r in range(0,9):
                    if sudokus[currentBoard][r][y] != 0:
                        freeSpots[x][y][(sudokus[currentBoard][r][y])-1] = 0;
                
                for r in range(((x/3)*3),(((x/3)*3)+3)):
                    for s in range(((y/3)*3),(((y/3)*3)+3)):
                        if sudokus[currentBoard][r][s] != 0:
                            freeSpots[x][y][(sudokus[currentBoard][r][s])-1] = 0;
            else:
                 for r in range(0,9):
                        freeSpots[x][y][r]=0;
    if ifPri == 1:
        for x in range(0,9):
            for y in range(0,9):
                if sudokus[currentBoard][x][y] == 0:
                    print("Ledige tall i rute (%d,%d)" % (x+1,y+1));
                    for z in range(0,9):
                        if freeSpots[x][y][z] != 0:
                            print(z+1);
                        
                        
def hardCoded():
    
    i = 0;
    j = 0;
    for x in range(0,9):
        for y in range(0,9):
            counter = 0;
            if sudokus[currentBoard][x][y] == 0:
                i = x;
                j = y;
                for z in range(0,9):
                            
                    if freeSpots[x][y][z] == 1:
                        counter += 1;
                        sudokus[currentBoard][x][y] = z + 1;
                        orientation();
                        break;
                    sudokus[currentBoard][i][j] = 0;
                    orientation();

                        
                    
currentBoard = 0;
completedBoards = 0;
sudokus = [[[0 for i in xrange(9)] for t in xrange(9)] for l in xrange(50)];
freeSpots = [[[1 for d in range(9)] for e in range(9)] for f in range(9)]


#Importerer fra en tekstfil, inn i et midlertidig array
results = []
with open('problem96.txt') as f:
    results = f.readlines()
results = [x.strip() for x in results] 

#Gjør om tallene fra en 9-sifret string til 9 individuelle tall    
for x in range(len(results)):
    results[x] = [int(d) for d in str(results[x])]


#Legger importeringen over i sudokus arrayet. Første indeks er hvilket puzzle, andre er radnr, og tredje er plassen i raden
count = 0;
for x in range(len(results)):
    if ((x % 9 == 0) and x != 0):
        count += 1;
        
    sudokus[count][x%9] = results[x];

while currentBoard < 50:
    laps = 0;
    print("----- Log of the solvingphase -----")
    while (isFinished() == False and laps < 25):
        #horisontalBlock();
        #verticalBlock();
        rowContaining8();    
        colomnContaining8();
        blockContaining8();
        xCross();

        laps += 1;
        
        if laps == 15:
            orientation(1);
            xWing();
            justOnePossible();
            
    printBoard();
    currentBoard += 1;
    
print("%d/%d fullførte brett" % (completedBoards,50))

