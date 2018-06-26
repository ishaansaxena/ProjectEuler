#!/usr/bin/python
from time import *
from math import *
start = time()

LIMIT = 100000000

def mark(s, n):
	if s[n]:
		for i in range(n + n, len(s), n):
			s[i] = False

sieve = [True] * (LIMIT * 11/10)
sieve[0] = sieve[1] = False

for i in range(len(sieve)):
	mark(sieve, i)

def is_valid_divisor(n, d):
	return n % d == 0 and not sieve[d + n / d]

count = sum(
   	n for n in range(1, LIMIT)
    if not any(is_valid_divisor(n, d) for d in range(1, int(sqrt(n)) + 1))
)

print count

print time() - start, "seconds"