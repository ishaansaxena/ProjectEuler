#!/usr/bin/python

from time import *
start = time()

def triangular_n(n):
	return n*(n+1)/2

def pentagonal_n(n):
	return n*(3*n-1)/2

def hexagonal_n(n):
	return n*(2*n-1)

triangular = []
pentagonal = []
hexagonal = []

i = 0
count = 0
while True:
	triangular.append(triangular_n(i+1))
	pentagonal.append(pentagonal_n(i+1))
	hexagonal.append(hexagonal_n(i+1))
	if triangular[i] in pentagonal and triangular[i] in hexagonal:
		print triangular[i]
		count +=1
		if count == 3:
			break
	i+=1

print time() - start, "seconds"