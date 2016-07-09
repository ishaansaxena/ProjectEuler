#!/usr/bin/python

from time import *
from math import *
start = time()

def isPrime(n):
	i = 2
	while i < int(sqrt(n))+1:
		if n%i == 0:
			return False
		i += 1
	return True

def isPermutation(arr):
	clone = []
	for i in range(len(arr)):
		clone.append(arr[i])
	a = [0,0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9]
	b = [0,0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9]
	c = [0,0,0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9]
	while clone[0] != 0:
		a.remove(clone[0]%10)
		clone[0] = clone[0]//10
	while clone[1] != 0:
		b.remove(clone[1]%10)
		clone[1] = clone[1]//10
	while clone[2] != 0:
		c.remove(clone[2]%10)
		clone[2] = clone[2]//10
	if a == b == c:
		return True
	else:
		return False

fourDigitPrimes = []

for i in range(1000,10000):
	if isPrime(i):
		fourDigitPrimes.append(i)

trueFor = []

i = 0
print "Processing primes..."
while i < len(fourDigitPrimes):
	j = i + 1
	while j < len(fourDigitPrimes):
		if (fourDigitPrimes[i] + fourDigitPrimes[j])/2 in fourDigitPrimes:
			trueFor.append([fourDigitPrimes[i], (fourDigitPrimes[i]+fourDigitPrimes[j])/2, fourDigitPrimes[j]])
		j += 1
	i += 1

for triad in trueFor:
	if isPermutation(triad):
		print triad

print time() - start, "seconds"