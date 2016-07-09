#!/usr/bin/python

from time import *
start = time()

def sum_of_n(n):
	return n*(n+1)/2

def sum_of_sq(n):
	return n*(n+1)*(2*n+1)/6

print sum_of_n(100)**2 - sum_of_sq(100)

print time() - start, "seconds"