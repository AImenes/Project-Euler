'''You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?'''

global numberOfStartingSundays, currentDay

currentYear = 1901;
goalYear = 2001;
currentDay = 2;
normYear = []
leap = []
numbOfStartingSundays = 0;

def normalYear():
    global numbOfStartingSundays, currentDay;
    for i in range(1,366):
        currentDay = currentDay % 7;
        
        if (i == 1 or i == 32 or i == 60 or i == 91 or i == 121 or i == 152 or i == 182 or i == 213 or i == 244 or i == 274 or i == 305 or i == 335) and currentDay == 6:
            numbOfStartingSundays += 1;
        currentDay += 1
 
    
def leapYear():
    global numbOfStartingSundays, currentDay;

    for i in range(1,367):
        currentDay = currentDay % 7;
        
        if ((i == 1 or i == 32 or i == 61 or i == 92 or i == 122 or i == 153 or i == 183 or i == 214 or i == 245 or i == 275 or i == 306 or i == 336) and currentDay == 6):
            numbOfStartingSundays += 1;
        currentDay += 1;

            
while currentYear < goalYear:
    
    if currentYear == 1901:
        print(currentDay)
    
    if currentYear%4 == 0:
        leapYear();
    else:
        normalYear();
    currentYear += 1;

print(numbOfStartingSundays)


    

