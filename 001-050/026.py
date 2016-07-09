#!/usr/bin/python

from time import *
start = time()

def genUnitFrac(den):
	r_list = []
	top = 1
	while True:
		r = top%den
		if r == 0 or r in r_list:
			break
		else:
			r_list.append(r)
			top = r*10
	return len(r_list)

i_max = 0
c_max = 0
for i in range(1,1000):
	c_cur = genUnitFrac(i)
	if c_cur > c_max:
		c_max = c_cur
		i_max = i

print i_max

print time() - start, "seconds"