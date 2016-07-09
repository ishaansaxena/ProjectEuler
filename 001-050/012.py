#!/usr/bin/python

from time import *
from math import *
start = time()

def nof_divisor(n):
	x = 1
	i = 2
	while (i < int(sqrt(n))+1):
		if(n%i == 0):
			x+=1
		i+=1
	i = 0
	if (int(sqrt(n))**2 == n):
		return 2*x-1
	else:
		return 2*x

def triangular_no(n):
	return n*(n+1)/2

i = 1
while (True):
	j = triangular_no(i)
	k = nof_divisor(j)
	if(k > 500):
		print j, k
		break
	i+=1

print time() - start, "seconds"