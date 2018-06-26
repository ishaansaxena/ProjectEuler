# -*- coding: utf-8 -*-
#!/usr/bin/python

from time import *
from math import *
start = time()

def isPandigital(n):
	counts = [0] * 9
	check = True
	clone = n
	while clone != 0:
		counts[clone%10 - 1] += 1
		clone = clone//10
	for i in counts:
		if i != 1:
			check = False
	return check

def toNum(s):
	num = 0
	for i in range(len(s)):
		num*=10
		num+=int(s[i])
	return num

def numCat(x, n, k=1):
	if k > n or n < 2:
		return -99
	elif k == n:
		return str(x*n)
	else:
		return str(x*k) + numCat(x, n, k+1)

pd_prod = []

for i in xrange(10000):
	j = 2
	while j < 10:
		p = toNum(numCat(i,j))
		if p > 10**9:
			break
		if isPandigital(p):
			pd_prod.append(p)
		j+=1

pd_prod.sort()
print pd_prod[len(pd_prod)-1]

print time() - start, "seconds"