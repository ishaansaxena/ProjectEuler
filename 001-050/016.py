#!/usr/bin/python

from time import *
start = time()

p = 2**1000
s = 0
while(p != 0):
	s += p%10
	p = p//10

print s

print time() - start, "seconds"