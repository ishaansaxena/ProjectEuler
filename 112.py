#!/usr/bin/python

from time import time
start = time()

def inc(n):
	while n != 0:
		d1 = n % 10
		n /= 10
		d2 = n % 10
		if d2 > d1:
			return False
	return True

def dec(n):
	while n != 0:
		d1 = n % 10
		n /= 10
		if n == 0: break
		d2 = n % 10
		if d2 < d1:
			return False
	return True

i, d = 0, 0
n = 1

while (n - (i + d))/float(n) < 0.99 or n < 100:
	if inc(n):
		i += 1
	elif dec(n):
		d += 1
	n += 1
	print n, (n - (i + d))/float(n)

print n

print time() - start, "seconds"