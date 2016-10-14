#!/usr/bin/python

from time import *

start = time()

i = 1
sum = 0

while(i<1000):
	if (i%3 == 0 or i%5 == 0):
		sum += i;
		print i, sum
	i+=1

print sum

print time() - start, "seconds"