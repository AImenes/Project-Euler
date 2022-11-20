# coding=utf-8


#Endre denne variablen for størrelsen på trekanten
sizeOfTriangle = 15;



#PathsCOST Bellham Ford
size = sizeOfTriangle + 1;
triangle = [];
with open('problem18.txt') as inputfile:
    for line in inputfile:
        triangle.append(line.strip().split(' '));
        
#Gjør arrayet om til et int
for x in range(len(triangle)):
    triangle[x] = list(map(int, triangle[x]))
                        

#Definerer et tomt array X
V = [[0]];
i = 1 
while i < size:
    V.append([0 for y in range(i)]);
    i += 1;
#.....................................................
#LOGISTIKKUTGJØRELSE
#V[0][0] sier
V[1][0] = V[0][0] + triangle[0][0];
j=1;
k=0;
while j < size-1:
    while k < j:
        if((V[j][k] + triangle[j][k])>V[j+1][k]):
            V[j+1][k] = V[j][k] + triangle[j][k];
        if((V[j][k] + triangle[j][k+1])>V[j+1][k+1]):
            V[j+1][k+1] = V[j][k] + triangle[j][k+1];
            
            k += 1;
    k = 0;
    j += 1;
#......................................................    

#Print tomt array        
for x in range(len(V)):
    print(V[x])
    
#Print tomt array        
for x in range(len(triangle)):
    print(triangle[x])
    
maxSum = 0;
for x in range(size-1):
    if V[size-1][x]>maxSum:
        maxSum = V[size-1][x];
        
print(maxSum)
   
    