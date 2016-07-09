# -*- coding: utf-8 -*-
#!/usr/bin/python

from time import *
start = time()

sieve = [True] * 1000000
sieve[0] = sieve[1] = False
for i in xrange(len(sieve)):
	if sieve[i]:
		for j in xrange(2*i, len(sieve), i):
			sieve[j] = False

primes = [i for i in range(len(sieve)) if sieve[i]]

def npf(x):
	primeFacts = []
	for i in primes:
		if x <= 1:
			break
		if x%i == 0:
			while x%i == 0:
				x = x//i
				primeFacts.append(i)
	return primeFacts


m = 4
l = [0]*m

for i in range(10**5,10**6):
	dpf = []
	check = True
	for j in range(m):
		if check:
			dpf.append(len(set(npf(i+j))))
			dpf = list(set(dpf))
			check = dpf[0] == m and len(dpf) == 1
			check = len(dpf) == 1
	if dpf[0] == m and check:
		print i, dpf
		break

print time() - start, "seconds"