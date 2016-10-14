#!/usr/bin/python
# Code similar to 031, 076 and 078

from time import *
from math import *
start = time()

target_number = 1000

sieve = [True] * target_number
def mark(sieve, x):
	for i in xrange(x+x, len(sieve), x):
		sieve[i] = False

for x in xrange(2, int(sqrt(len(sieve))) + 1):
	if sieve[x]: mark(sieve, x)

sieve[0] = False
sieve[1] = False

number_pool = [i for i in xrange(2, len(sieve)) if sieve[i]]

solutions = [1] + [0]*target_number

for i in number_pool:
	for j in range(i, target_number+1):
		solutions[j] += solutions[j-i]

i = 0
while solutions[i] < 5000:
	i+=1

print i, solutions[i]

print time() - start