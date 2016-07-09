#!/usr/bin/python

from time import *
from math import *
start = time()

size = 2500

def returnRoots(n1,n2):
	if n1 < n2:
		temp = n1
		n1 = n2
		n2 = temp
	r1 = sqrt(1 + 12*(3*(n1**2 + n2**2) - (n1 + n2)))
	r2 = sqrt(1 + 12*(3*(n1**2 - n2**2) - (n1 - n2)))
	x = (1+r1)/6
	y = (1+r2)/6
	return (x,y)

def returnPentagonal(n):
	return (3*n - 1)*n/2

for i in range(1,size):
	for j in range(i,size):
		r1r2 = returnRoots(i,j)
		if r1r2[0]%1 == 0 and r1r2[1]%1 == 0:
			print abs(returnPentagonal(i) - returnPentagonal(j))
			print time() - start, "seconds"
			exit()