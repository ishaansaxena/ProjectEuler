#!/usr/bin/python
from time import *
start = time()

def sumcount(x):
	if x == 0:
		return 0
	else:
		return x%10 + sumcount(x//10)

m_sum = 0
xy = (0,0)

for i in range(1,100):
	for j in range(1,100):
		c_sum = sumcount(i**j)
		if c_sum > m_sum:
			m_sum = c_sum
			xy = (i,j)

print xy, m_sum

print time() - start, "seconds"