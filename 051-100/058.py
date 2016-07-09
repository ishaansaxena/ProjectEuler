#!/usr/bin/python

from time import time
from math import sqrt
start = time()

def isPrime(number):
    if number <= 1:
        return false
    i = 2
    while(i < int(sqrt(number)) + 1):
        if(number%i ==0):
            return False
        else:
            pass
        i+=1
    return True

diagonal_list = [1]

counter = 1
length = -1
prime_count = 0
while True:
    while counter < length*length:
        counter += length - 1
        if isPrime(counter):
            prime_count += 1.0
        diagonal_list.append(counter)
    if prime_count/len(diagonal_list) < 0.1 and length > 1:
        break
    length += 2

print length, "|", prime_count/len(diagonal_list)
print time() - start, "seconds"