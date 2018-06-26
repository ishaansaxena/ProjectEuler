#!/usr/bin/python

from time import *
from math import *
start = time()

constraint = 1000

triplet_sum = []

def get_py(a,b):
	return 2*a*(a+b)

for n in range(1,constraint//2):
	if n <= 23:
		for m in range(n, 24):
			p = get_py(m,n)
			if p <= constraint:
				triplet_sum.append(p)
	else:
		for m in range(1, 24):
			p = get_py(m,n)
			if p <= constraint:
				triplet_sum.append(p)

max_n = 0
max_p = 0
for p in range(2,constraint+1,2):
    n = 0
    for a in range(2, int(p/3.4142) + 1):
        if  p*(p - 2*a) % (2*(p - a)) == 0: 
            n += 1
            if n >= max_n:
            	max_n = n
            	max_p = p
 
print max_p

print time() - start, "seconds"