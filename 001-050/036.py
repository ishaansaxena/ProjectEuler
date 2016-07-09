#!/usr/bin/python

from time import *
start = time()

def numToArray(n, base):
	x = []
	while n != 0:
		x.append(n%base)
		n = n//base
	x.reverse()
	return x

def isPallindrome(arr):
	x = []
	i = len(arr)
	while i > 0:
		x.append(arr[i-1])
		i -= 1
	return arr == x

s = 0
for i in range(1,1000000):
	if isPallindrome(numToArray(i, 10)):
		if isPallindrome(numToArray(i, 2)):
			s += i

print s

print time() - start, "seconds"