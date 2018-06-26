#!/usr/bin/python

from time import time
start = time()

L = 1000000

totient = range(L + 1)
totient[1] = 0

for n in range(2, L + 1):
	if totient[n] == n:
		for m in range(n, L + 1, n):
			totient[m] -= totient[m] / n

print sum(totient)

print time() - start, "seconds"