#!/usr/bin/python

from math import *
from time import *
start = time()

def routes(n): # For an n x n grid, possible routes = 2nCn
	return factorial(2*n)/(factorial(n)**2)

print routes(2)	# 2x2 Grid
print routes(20)

print time() - start, "seconds"