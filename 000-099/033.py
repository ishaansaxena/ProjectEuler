#!/usr/bin/python

from time import *
from collections import namedtuple
start = time()

fraction = namedtuple("fraction", "n d")

def numToList(x):
	n = []
	while(x!=0):
		n.append(x%10)
		x = x//10
	n.reverse()
	return n

def listToNum(n):
	x = 0
	n.reverse()
	for i in range(len(n)):
		x += n[i] * (10**i)
	return x


def simplifyFraction(x):
	num = numToList(x.n)
	den = numToList(x.d)
	l = []
	for i in den:
		if i in num and i!=0:
			den.remove(i)
			num.remove(i)
	r = fraction(listToNum(num), listToNum(den))
	return r

def evaluateFraction(x):
	if x.d != 0:
		num = float(x.n)
		den = float(x.d)
	else:
		num = 0
		den = 1
	return num/den

s = [] 

for a in range(10, 100):
	for b in range(a+1, 100):
		cur = fraction(a, b)
		if cur != simplifyFraction(cur):
			if evaluateFraction(cur)-evaluateFraction(simplifyFraction(cur)) == 0.0:
				s.append(simplifyFraction(cur))

print s

print time() - start, "seconds"