#!/usr/bin/python

from time import *
start = time()

constraint = 1000
s = 0

for i in range(1, constraint+1):
	s += i**i%(10**10)

print s%(10**10)

print time() - start, "seconds"