#!/usr/bin/python

from time import *
from math import *
start = time()

sieve = [True] * 10000

def mark(sieve, x):
	for i in xrange(x+x, len(sieve), x):
		sieve[i] = False

i = 3
l = len(sieve) + len(sieve)**2	# Upper bound

mark(sieve,2)

while i < l:
	if i < len(sieve):
		if sieve[i]:
			mark(sieve, i)
	if not sieve[i]:
		# Number - 2n^2
		p = []
		j = 1
		while j <= int(sqrt(i//2)):
			p.append(i-2*j**2)
			j += 1
		# Checking
		count = 0
		for el in p:
			if sieve[el]:
				count += 1
			else:
				pass
		if count == 0:
			print i
			break
	i += 2

print time() - start, "seconds"