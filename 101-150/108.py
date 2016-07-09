#!/usr/bin/python
from time import *
from math import *
start = time()

def numOfFactors(x):
	factors = 1
	for i in range(2, int(sqrt(x))+1):
		if x%i == 0:
			factors += 1
	if x % sqrt(x) == 0:
		factors = 2*factors - 1
	else:
		factors = 2*factors
	return factors

for x in range(1,100000):
	print x, numOfFactors(x)

print time() - start, "seconds"