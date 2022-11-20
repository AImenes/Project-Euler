'''The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.'''

tempArr = []
containingNumb = [0,0,0,0,0,0,0,0,0,0]
storage = [];

for i in range(1, 10000):
    temp = i * i * i;
    tempArr = [int(d) for d in str(temp)]
    for elem in tempArr:
        containingNumb[elem] += 1;
        
    for x in range(len(storage)):
        if containingNumb == storage[x]:
            print(x+1, i);
            print("\n");
            
    storage.append(containingNumb);

    containingNumb = [0,0,0,0,0,0,0,0,0,0]


