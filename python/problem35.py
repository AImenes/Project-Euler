'''The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?'''
import sympy as sp
import time


#Works
def prob35_spaceefficient(upper):
    start = time.time()
    counter = 4
    if upper < 10:
        return "Please input something bigger than 10"

    for i in range(10, upper):
        digits = set(str(i))
        if not ('0' in digits or '2' in digits or '4' in digits or '6' in digits or '8' in digits or '5' in digits):
            if sp.isprime(i):
                number = i
                number_of_cycles = len(str(i))
                is_cycled = True
                for k in range(number_of_cycles-1):
                    number = (number%10)*10**(number_of_cycles-1)+number//10
                    if not sp.isprime(number):
                        is_cycled = False
                if is_cycled:
                    counter += 1
    end = time.time()

    return counter, end-start

#Not working yet      
def prob35_timeefficient(upper):
    start = time.time()
    is_visited = [False for i in range(upper+1)]
    counter = 4

    for i in range(10, upper):
        if is_visited[i] == False:
            digits = set(str(i))
            if not ('0' in digits or '2' in digits or '4' in digits or '6' in digits or '8' in digits or '5' in digits):
                if sp.isprime(i):
                    number = i
                    number_of_cycles = len(str(i))
                    is_cycled = True
                    numbers = [number]
                    for k in range(number_of_cycles-1):
                        number = (number%10)*10**(number_of_cycles-1)+number//10
                        if not sp.isprime(number):
                            is_cycled = False

                    if is_cycled:
                        number = i
                        for k in range(number_of_cycles-1):
                            is_visited[number] = True
                            number = (number%10)*10**(number_of_cycles-1)+number//10
                        counter += number_of_cycles
    
    end = time.time()

    return counter, end-start


def main():
    upper = 1000000
    print(prob35_spaceefficient(upper))
    #print(prob35_timeefficient(upper))

if __name__ == "__main__":
    main()


        
        
        
            
            
            
        
            
             