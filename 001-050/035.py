#!/usr/bin/python

from time import *
from math import *
start = time()

def retCircular(num):
	circ = [num]
	digits = 0
	while (num!=0):
		num/=10
		digits += 1
	i = 1
	while (i < digits):
		circ.append(circ[i-1]/10+(circ[i-1]%10)*10**(digits-1))
		i+=1
	return circ

sieve = [True] * 1000000

def mark(sieve, x):
	for i in xrange(x+x, len(sieve), x):
		sieve[i] = False 

for x in xrange(2, int(sqrt(len(sieve))) + 1):
	if sieve[x]: mark(sieve, x)

arr = []

for i in range(2, len(sieve)):
	if sieve[i]:
		sub_arr = retCircular(i)
		count = len(sub_arr)
		carry = 0
		for j in sub_arr:
			if sieve[j]:
				carry += 1
				sieve[j] = False
			else:
				break
		if carry == count:
			for j in sub_arr:
				arr.append(j)

print arr
print "Number of circular primes =", len(arr)

print time() - start, "seconds"