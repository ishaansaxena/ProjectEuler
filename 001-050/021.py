#!/usr/bin/python

from time import *
start = time()

def d(n):
	x = 0
	i = 1
	while(i < n):
		if (n%i == 0):
			x+=i
		i+=1
	return x

s = 0
n = 0
while(n < 10000):
	a = d(n)
	if(d(a) == n and a != n):
		print n
		s+=n
	else: pass
	n+=1

print s

print time() - start, "seconds"