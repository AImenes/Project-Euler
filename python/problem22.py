names = []
with open('problem22.txt') as inputfile:
    for line in inputfile:
        names.append(line.strip().split('","'));
names[0].sort()        


total = 0
temp = 0
for x in range(len(names[0])):
    nameValue = 0
    for y in range(len(names[0][x])):
        nameValue = nameValue + (ord(names[0][x][y]) - 64);
    temp = nameValue * (x+1);
    total += temp;
    
print(total)
