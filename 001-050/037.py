#!/usr/bin/python

from time import *
start = time()

sieve = [True] * 1000000
sieve[0] = False
sieve[1] = False 

def truncLR(p):
	clone = p
	check = 1
	i = 1
	while clone > 10**i:
		if not sieve[clone%(10**i)]:
			check = 0
			break
		elif not sieve[clone//(10**i)]:
			check = 0
			break
		else:
			i+=1
	if check == 0:
		return False
	else:
		return True

def mark(e_sieve, x):
	for i in range(2*x, len(e_sieve), x):
		e_sieve[i] = False

count = 0
s = -17
for i in range(len(sieve)):
	if sieve[i]:
		mark(sieve, i)
		if truncLR(i):
			count += 1
			s += i
	if count == 15:
		break

print s

print time() - start, "seconds"