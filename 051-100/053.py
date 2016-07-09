#!/usr/bin/python
from time import *
from math import *
start = time()

def C(n,r):
	return factorial(n)/(factorial(r)*factorial(n-r))

count = 0
for i in range(1,101):
	j = i//2
	switch = 0
	while j >= 0:
		if C(i,j) > 1000000:
			count += 2
			print i, j
			switch = 1
		else:
			break
		j -= 1
	if i%2 == 0 and switch == 1:
		count -= 1
	print count

print count

print time() - start