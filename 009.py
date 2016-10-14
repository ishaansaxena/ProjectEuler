#!/usr/bin/python

from time import *
from math import *
start = time()

factors = []
num = 500

i = 1
while (i<int(sqrt(num))+1):
	if(num%i == 0):
		factors.append(i)
	i+=1

i = 0
c = len(factors)
while(i < c):
	factors.append(num//factors[i])
	i+=1

factors.sort()

i = 0
fact_a = 0
fact_b = 0
c = len(factors)
while(i < c):
	m = factors[i]
	j = 0
	while(j < c):
		n = factors[j]
		if (n == 500//m - m):
			fact_a = m
			fact_b = n
			break
		j+=1
	i+=1

a = fact_a**2 - fact_b**2
b = 2*fact_a*fact_b
c = fact_a**2 + fact_b**2

print "a =", a
print "b =", b
print "c =", c
print "abc =", a*b*c

print time()-start, "seconds"