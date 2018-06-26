#!/usr/bin/python

from time import time
start = time()

HAMMING_TYPE = 100
LIMIT = 10**9

sieve = [True] * 100
sieve[0], sieve[1] = False, False
primes = []

for i in xrange(len(sieve)):
    if sieve[i]:
        primes.append(i)
        for j in xrange(2*i, len(sieve), i):
            sieve[j] = False

def count(product, index):
    if index < len(primes):
        sum = 0
        while product <= LIMIT:
            sum += count(product, index + 1)
            product *= primes[index]
        return sum
    else:
        return 0 if product > LIMIT else 1

print count(1, 0)

print time() - start, "seconds"
