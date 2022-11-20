import math

counter = 0;
everyT = 0;

layer = 200000;

for i in range(0,layer+1):
    currentRow = layer + 1 - i;
    for j in range(0,currentRow):
        
        numerator = math.factorial(((currentRow-1)-j)+i+(j));
        denumerator = math.factorial((currentRow-1)-j)*math.factorial(i)*math.factorial(j);
        
        total=numerator/denumerator;
        #print(total);
        #print(" ");
        
        if (total%(pow(10,12))==0):
            counter += 1;
            
            
    everyT += 1;
    if (everyT % 100==0):
        print(everyT);
        print(" ");
    #print("\n");
print(counter);