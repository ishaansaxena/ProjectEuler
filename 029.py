#!/usr/bin/python

from time import *
start = time()

constraint = 100
exponents = []

for i in range(2, constraint + 1):
	for j in range(2, constraint + 1):
		if i**j in exponents:
			pass
		else:
			exponents.append(i**j)

print len(exponents)

print time() - start, "seconds"