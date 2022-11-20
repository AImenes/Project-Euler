import os
i = 0;
tall = 12;
id = 2;
arr = [12];

while i < 499:
    tall = tall + (26+16*i);
    arr.append(tall);
    i += 1;
    id += 1;
print(arr)

sum= 0
for i in range(len(arr)):
    sum = sum + (2*arr[i]);

print(sum)


''' 
a = 2;
b = 2;
i = 0;
numb = [];

for x in range(2,101):
    for y in range(2,101):
        exists = False;
        temp = x ** y;
        for z in range(len(numb)):
            if(temp == numb[z]):
                exists = True;
        if (exists == False):
            numb.append(temp);

print(len(numb), numb)


'''


