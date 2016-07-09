#!/usr/bin/python
from time import *
from math import *
start = time()

sieve = [1]*10000000
sieve[0] = 0

def markChain(x,e_sieve):
	s = x
	while s>=x:
		if s==1 or s==89:
			break;
		clone = s
		s = 0
		while clone != 0:
			s += (clone%10)**2
			clone = clone/10
	if s == 1 or s == 89:
		return s
	else:
		return e_sieve[s]

count = 0
for i in range(2,len(sieve)):
	sieve[i] = markChain(i,sieve)
	if sieve[i] == 89:
		count += 1

print count

print time() - start, "seconds"