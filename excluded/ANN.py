weights = [0,0]
bias = 0;
inputPoints = [[-1,1],[0,-1],[10,1]];
outputPoints = [1,-1,1]
currentSum = [0,0];
true = 0;
counter = 0;

convergence = False;
n=0;

while convergence != True:
    wx = sum([weights[i]*inputPoints[n][i] for i in range(len(weights))]);
    #print("wk: %d, bias = %d" % (wx, bias))
    ywx = wx + bias;
    
    if ywx == 0 or ywx < 0:
        counter = 0;
        bias += outputPoints[n];
        
        for x in range(len(weights)):
            weights[x] += (outputPoints[n]*inputPoints[n][x])
   
    print("streak = %d, n = %d, ywx: %d, weights = (%d,%d), bias = %d" % (counter,n,ywx,weights[0],weights[1],bias))

    n += 1;
    n %= 3;
    counter += 1;
    
    
    if counter == len(inputPoints):
        convergence = True;
        
            
print(weights); #Skal bli 7,5
print(bias); #Skal bli 3
            