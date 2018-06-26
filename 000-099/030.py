#!/usr/bin/python

from time import *
start = time()

def powerSum(n):
	x = 0
	while n != 0:
		x += (n%10)**5
		n = n//10
	return x

s = 0
for i in range(2, 355000):
	if i == powerSum(i):
		s += i

print s

print time() - start, "seconds"