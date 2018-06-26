#!/usr/bin/python
from time import *
start = time()

def countdigits(x):
	if x == 0:
		return 0
	else:
		return 1 + countdigits(x//10)

_base = range(2,10)
count = 0

for base in _base:
	n = 1
	exponent = 1
	while exponent <= countdigits(n) + 1:
		n = base**exponent
		if countdigits(n) == exponent:
			count += 1 
		exponent +=1

print count + 1 # for 1,1

print time() - start, "seconds"