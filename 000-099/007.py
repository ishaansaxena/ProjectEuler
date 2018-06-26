#!/usr/bin/python

from time import *
from math import *
start = time()

sieve = [True] * 500000
def mark(sieve, x):
	for i in xrange(x+x, len(sieve), x):
		sieve[i] = False 

# Creates a 'sieve' of 500,000 True values
# Marks the composite sieve location values as False
# For i in range 2x to last value of sieve, marks 
# Starts from 2x to avoid removing first value
# all multiples as false. (Thus, an incrememnt of x)	

for x in xrange(2, int(sqrt(len(sieve))) + 1):
	if sieve[x]: mark(sieve, x)

# Marks all sieve values from 2 to the square root of the length to
# False. Thus, leaves out all prime locations in the sieve as True

arr = [i for i in xrange(2, len(sieve)) if sieve[i]]

# Creates an array of all location IDs with value True in them
# Thus, adding only prime numbers to this array

print arr[10000]

# Prints the 10001st prime number

print time() - start, "seconds"