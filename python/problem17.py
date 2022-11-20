'''If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.'''


numbers = ["","one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety","hundred", "thousand"];

summen = 0;
lengde = 0

for i in range(len(numbers)):
    print(i,numbers[i])

for y in range(1,1001):
    lengde = 0;
    numb = [int(i) for i in str(y)];
    
    for x in range(len(numb)):
        lengde += 1;
    
    
    if (lengde == 4):
        for z in range(len(numbers[numb[0]])):
            summen += 1;
        for z in range(len(numbers[29])):
            summen += 1;
        print("%s %s" % (numbers[numb[0]],numbers[29]));
        
              
    if (lengde == 3):
        for z in range(len(numbers[numb[0]])):
            summen += 1;
        for z in range(len(numbers[28])):
            summen += 1;
        print("%s %s" % (numbers[numb[0]],numbers[28]));
    

    if ((y > 100) and (y<1000) and (y != 200 and y != 300 and y != 400 and y != 500 and y != 600 and y != 700 and y != 800 and y != 900)):
        summen += 3;
        print(" and ");
        
    if (y % 100 < 20):
        for z in range(len(numbers[y%100])):
            summen += 1;
        print(numbers[y%100])
    elif y % 100 > 19 and y % 100 < 30:
        for z in range(len(numbers[20])):
            summen += 1;
        for z in range(len(numbers[y%10])):
            summen += 1;
        print("%s %s" % (numbers[20],numbers[y%10]))
    elif y % 100 > 29 and y % 100 < 40:
        for z in range(len(numbers[21])):
            summen += 1;
        for z in range(len(numbers[y%10])):
            summen += 1;
        print("%s %s" % (numbers[21],numbers[y%10]))
    elif y % 100 > 39 and y % 100 < 50:
        for z in range(len(numbers[22])):
            summen += 1;
        for z in range(len(numbers[y%10])):
            summen += 1;
        print("%s %s" % (numbers[22],numbers[y%10]))
    elif y % 100 > 49 and y % 100 < 60:
        for z in range(len(numbers[23])):
            summen += 1;
        for z in range(len(numbers[y%10])):
            summen += 1;
        print("%s %s" % (numbers[23],numbers[y%10]))
    elif y % 100 > 59 and y % 100 < 70:
        for z in range(len(numbers[24])):
            summen += 1;
        for z in range(len(numbers[y%10])):
            summen += 1;
        print("%s %s" % (numbers[24],numbers[y%10]))
    elif y % 100 > 69 and y % 100 < 80:
        for z in range(len(numbers[25])):
            summen += 1;
        for z in range(len(numbers[y%10])):
            summen += 1;
        print("%s %s" % (numbers[25],numbers[y%10]))
    elif y % 100 > 79 and y % 100 < 90:
        for z in range(len(numbers[26])):
            summen += 1;
        for z in range(len(numbers[y%10])):
            summen += 1;
        print("%s %s" % (numbers[26],numbers[y%10]))
    elif y % 100 > 89 and y % 100 < 100:
        for z in range(len(numbers[27])):
            summen += 1;
        for z in range(len(numbers[y%10])):
            summen += 1;
        print("%s %s" % (numbers[27],numbers[y%10]))
        
    print("\n")
    
print(summen)