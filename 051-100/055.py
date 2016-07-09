#!/usr/bin/python

from time import time
start = time()

LIMIT = 10000

def isPallindrome(number):
    return str(number)[::-1] == str(number)

def reverseNumber(number):
    return int(str(number)[::-1])

def recursiveSum(number, iteration):
    intermediate = number + reverseNumber(number)
    if iteration == None:
        iteration = 0
    if isPallindrome(number) and iteration > 0:
        return iteration
    elif iteration > 50:
        return -1
    else:
        return 0 + recursiveSum(intermediate, iteration + 1)

count = 0
for i in range(1, LIMIT):
    if recursiveSum(i, None) == -1:
        count += 1

print count
print time() - start, "seconds"