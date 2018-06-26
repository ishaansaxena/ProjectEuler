#!/usr/bin/python

from time import *
from math import *
start = time()

def factSum(n):
	x = 0
	while n != 0:
		x += factorial((n%10))
		n = n//10
	return x

s = 0
for i in range(3, 2541000):
	if i == factSum(i):
		s += i

print s

print time() - start, "seconds"