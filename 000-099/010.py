#!/usr/bin/python

from time import *
from math import *
start = time()

# Refer to solution to problem 7 for explanation to code.
# sieve = [True] * 2000000 = Original Problem
sieve = [True] * 100000000 # New computation

def mark(sieve, x):
    for i in xrange(x+x, len(sieve), x):
        sieve[i] = False

for x in xrange(2, int(sqrt(len(sieve))) + 1):
    if sieve[x]: mark(sieve, x)

s = 0
for i in xrange(2, len(sieve)):
	if sieve[i]:
		s+=i
print s

print time() - start, "seconds"

"""
Old code:

from time import *
from math import *
start = time()

def isPrime(x):
	if(x == 2):
		return True
	elif(x < 2):
		return False
	i = 2
	while(i < int(sqrt(x)) + 1):
		if(x%i ==0):
			return False
		else:
			pass
		i+=1
	return True

sum = 2
i = 3

while(i < 2000000):
	if(isPrime(i)):
		sum += i
	i+=2

print sum

print time() - start, "seconds"

Execution:

Ishaans-MacBook-Pro:project euler Ishaan$ python 010.py
142913828922
76.4431910515 seconds # Takes 0.658559799194 seconds with new code.
"""