#!/usr/bin/python

from time import *
from math import *
start = time()

def getPandigital(n):
	count = 0
	digits = [1,2,3,4,5,6,7,8,9,10]
	while(n > 0):
		if n%10 in digits:
			digits.remove(n%10)
		count += 1
		n = n//10
	if digits[0] == count + 1:
		return True
	else:
		return False

sieve = [True] * 10000000

def mark(sieve, x):
	for i in xrange(x+x, len(sieve), x):
		sieve[i] = False 

for x in xrange(2, int(sqrt(len(sieve))) + 1):
	if sieve[x]: mark(sieve, x)

arr = [i for i in xrange(2, len(sieve)) if sieve[i]]
arr.reverse()

for n in arr:
	if getPandigital(n):
		print n
		break

print time() - start, "seconds"