#!/usr/bin/python

from time import *
from math import *
start = time()

n = factorial(100)

def digitsum(x):
	if(x == 0):
		return 0;
	else:
		return x%10+digitsum(x//10)

print digitsum(n)

print time() - start, "seconds"